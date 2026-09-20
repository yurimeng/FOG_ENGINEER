"""Cross-domain match. Exact values in code; TypeSafe on survivors. Never auto-confirm numbers."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from typesafe_sdk import Choice, Noul, Score

from .claims import Claim, wiki_blob
from .citations import AUTO_ACCEPT, check_citation
from .classify import DOMAIN_LABELS, FOUR_DOMAINS
from .typesafe_client import TypedAnswers, ask_system_one

PAIR_QUESTIONS = {
    "relation": Choice(
        instructions=(
            "Two excerpts from different library domains mention the same SKU, load, "
            "cooling selection, or RFI item. How do they relate?"
        ),
        criteria={
            "match": "They state the same fact (same SKU and compatible values/selection).",
            "mismatch": "They contradict each other on a number or a selection.",
            "unrelated": "They are not about the same fact.",
            "uncertain": "Not enough evidence to decide.",
        },
    ),
    "same_object": Noul(
        instructions="Do both excerpts refer to the same SKU or RFI item?",
        criteria={
            "true": "Same SKU/RFI identity",
            "false": "Different items",
        },
    ),
    "conflict_degree": Score(
        instructions="How serious is any disagreement between the excerpts?",
        criteria=[
            "no disagreement",
            "cosmetic wording only",
            "engineering values disagree",
            "cannot judge",
        ],
    ),
}


@dataclass
class LinkedFact:
    key: tuple[str, str]
    claims: list[Claim]
    domains: tuple[str, ...]
    blob_links: list[str]


@dataclass
class ChecklistSeed:
    kind: str  # mismatch | unconfirmed | unsourced | unclassifiable | ghost | typesafe
    question: str
    files: list[str]
    blobs: list[str]
    extra: dict = field(default_factory=dict)


@dataclass
class MatchReport:
    linked: list[LinkedFact]
    seeds: list[ChecklistSeed]
    typesafe_calls: int
    typed_sample: TypedAnswers | None = None


def _values_close(a: str, b: str, rel: float = 0.01) -> bool:
    try:
        x, y = float(a), float(b)
    except ValueError:
        return a.strip() == b.strip()
    if x == y:
        return True
    scale = max(abs(x), abs(y), 1e-9)
    return abs(x - y) / scale <= rel


def _canon_score(claim: Claim) -> tuple:
    """Lower is better. Prefer the card that owns the SKU/RFI, not the first mention."""
    path = claim.relpath.replace("\\", "/")
    if "_template" in path or "/_archive/" in path:
        return (9, len(path))
    sku = claim.sku or ""
    ident = claim.value if claim.kind == "rfi" else sku
    if claim.kind == "rfi":
        if ident and ident in path:
            return (0, len(path))
        if "PROCUREMENT" in path:
            return (2, len(path))
        return (5, len(path))
    if claim.domain == "product":
        if "PRODUCT_SPEC_BASELINE" in path:
            return (0, 0)
        if sku and f"/{sku}/" in f"/{path}":
            return (1, 0)
        if sku and sku in Path(path).name:
            return (2, 0)
        if "NAMING_MAP" in path:
            return (3, 0)
        if "_blocks" in path:
            return (7, 0)
        if "3RD-PARTY" in path:
            return (8, 0)
        return (4, len(path))
    if claim.domain == "solution":
        if sku and "Tech_Spec" in path and sku in path:
            return (0, 0)
        if "Reference_Architecture" in path or "Reference Architecture" in path:
            return (1, 0)
        if sku and sku in Path(path).name:
            return (2, 0)
        if "PUBLIC/README" in path:
            return (6, 0)
        return (4, len(path))
    if claim.domain == "project":
        if "Project_Record" in path:
            return (0, 0)
        if "project_list" in path:
            return (1, 0)
        return (3, len(path))
    if claim.domain == "procurement":
        if ident and ident in path:
            return (0, 0)
        if "PROCUREMENT" in path:
            return (1, len(path))
        return (4, len(path))
    return (9, len(path))


def _representative(claims: list[Claim]) -> list[Claim]:
    """One claim per domain; canonical card beats first-wins alias mentions."""
    by_domain: dict[str, Claim] = {}
    for claim in claims:
        prev = by_domain.get(claim.domain)
        if prev is None or _canon_score(claim) < _canon_score(prev):
            by_domain[claim.domain] = claim
    return [by_domain[d] for d in FOUR_DOMAINS if d in by_domain]


def match_claims(
    claims: list[Claim],
    client=None,
    *,
    max_typesafe: int = 24,
    source_texts: dict[str, str] | None = None,
) -> MatchReport:
    source_texts = source_texts or {}
    grouped: dict[tuple[str, str], list[Claim]] = defaultdict(list)
    for claim in claims:
        grouped[claim.match_key].append(claim)

    linked: list[LinkedFact] = []
    seeds: list[ChecklistSeed] = []
    calls = 0
    typed_sample: TypedAnswers | None = None

    for key, group in sorted(grouped.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        kind, ident = key
        if kind == "unconfirmed":
            for claim in group:
                seeds.append(
                    ChecklistSeed(
                        kind="unconfirmed",
                        question=f"{DOMAIN_LABELS.get(claim.domain, claim.domain)} 中 `{ident}` 标了 #unconfirmed。是否仍待厂家/站点确认？选项：仍待确认 / 已可关闭 / 改为 conflict",
                        files=[claim.relpath],
                        blobs=[claim.blob],
                    )
                )
            continue

        reps = _representative(group)
        domains = tuple(c.domain for c in reps)
        if kind == "sku_presence":
            if len(set(domains)) >= 2:
                linked.append(
                    LinkedFact(
                        key=key,
                        claims=reps,
                        domains=domains,
                        blob_links=[wiki_blob(c, ident) for c in reps],
                    )
                )
            continue

        if kind == "rfi":
            if len(set(domains)) >= 2:
                linked.append(
                    LinkedFact(
                        key=key,
                        claims=reps,
                        domains=domains,
                        blob_links=[wiki_blob(c, ident) for c in reps],
                    )
                )
            continue

        values = {c.domain: c.value for c in reps}
        multi = len(set(domains)) >= 2
        if kind == "sku_it_kw":
            by_domain_vals: dict[str, list[Claim]] = defaultdict(list)
            for claim in group:
                by_domain_vals[claim.domain].append(claim)
            for domain, dclaims in by_domain_vals.items():
                nums = {c.value for c in dclaims}
                if len(nums) > 1 and not all(
                    _values_close(dclaims[0].value, c.value) for c in dclaims[1:]
                ):
                    seeds.append(
                        ChecklistSeed(
                            kind="mismatch",
                            question=(
                                f"`{ident}` 在同一域 {DOMAIN_LABELS.get(domain, domain)} 内出现不同容量："
                                + " / ".join(sorted(nums))
                                + " kW。是否同一规格的冲突副本？选项：是冲突 / 不是同一指标 / 暂不裁定"
                            ),
                            files=[c.relpath for c in dclaims],
                            blobs=[c.blob for c in dclaims],
                        )
                    )

        if kind == "sku_it_kw" and multi:
            # Site-scale MW on a project vs SKU kW on a product card is not the same metric.
            product_vals = [c for c in reps if c.domain == "product"]
            other_vals = [c for c in reps if c.domain != "product"]
            comparable = True
            if product_vals and other_vals:
                pkw = float(product_vals[0].extra.get("kw", product_vals[0].value) or 0)
                for other in other_vals:
                    okw = float(other.extra.get("kw", other.value) or 0)
                    # 10x+ apart at MW vs kW scale → skip numeric conflict; presence already linked.
                    if pkw > 0 and (okw / pkw >= 8 or pkw / max(okw, 1e-9) >= 8):
                        comparable = False
                        break
            if not comparable:
                continue
            agree = all(_values_close(reps[0].value, c.value) for c in reps[1:])
            if agree:
                accepted = client is None
                if client is not None:
                    left, right = reps[0], reps[1]
                    src = source_texts.get(left.relpath, "")
                    if calls >= max_typesafe:
                        seeds.append(
                            ChecklistSeed(
                                kind="typesafe",
                                question=(
                                    f"`{ident}` 表面容量一致，但 TypeSafe 预算已用尽，不得自动算匹配。"
                                    "是否视为匹配？选项：匹配 / 不匹配 / 稍后重跑"
                                ),
                                files=[c.relpath for c in reps],
                                blobs=[c.blob for c in reps],
                                extra={"reason": "typesafe-budget"},
                            )
                        )
                    else:
                        try:
                            verdict = check_citation(
                                client,
                                source=src or left.raw,
                                claim=right.raw,
                                quote=left.raw,
                            )
                            calls += 1
                            typed_sample = verdict.answers or typed_sample
                            if verdict.verdict == "verified" and verdict.auto:
                                accepted = True
                            else:
                                seeds.append(
                                    ChecklistSeed(
                                        kind="mismatch",
                                        question=(
                                            f"`{ident}` 数值表面一致，但 TypeSafe 引用核验为 `{verdict.verdict}`。"
                                            f"不得列入跨域已匹配。是否仍视为匹配？选项：匹配 / 不匹配 / 需我重读原文"
                                        ),
                                        files=[left.relpath, right.relpath],
                                        blobs=[left.blob, right.blob],
                                        extra={"typesafe": verdict.verdict},
                                    )
                                )
                        except Exception as exc:  # noqa: BLE001 — park, do not invent
                            seeds.append(
                                ChecklistSeed(
                                    kind="typesafe",
                                    question=(
                                        f"`{ident}` 引用核验失败（{type(exc).__name__}）。"
                                        "不得自动算匹配。是否稍后重跑 TypeSafe？选项：是 / 否，保持未匹配"
                                    ),
                                    files=[left.relpath, right.relpath],
                                    blobs=[left.blob, right.blob],
                                    extra={"reason": "typesafe-unavailable"},
                                )
                            )
                if accepted:
                    linked.append(
                        LinkedFact(
                            key=key,
                            claims=reps,
                            domains=domains,
                            blob_links=[wiki_blob(c, f"{ident} {c.value} kW") for c in reps],
                        )
                    )
                continue
            # numeric mismatch
            seed = ChecklistSeed(
                kind="mismatch",
                question=(
                    f"`{ident}` 的 IT/容量在不同域不一致："
                    + "；".join(
                        f"{DOMAIN_LABELS[c.domain]}={c.value} kW"
                        for c in reps
                    )
                    + "。以哪一侧为准？选项：产品设计 / 解决方案 / 项目 / 采购询价 / 暂不裁定"
                ),
                files=[c.relpath for c in reps],
                blobs=[c.blob for c in reps],
            )
            if client is not None and calls < max_typesafe:
                try:
                    answers = ask_system_one(
                        client,
                        state={
                            "sku": ident,
                            "excerpts": [
                                {
                                    "domain": DOMAIN_LABELS[c.domain],
                                    "path": c.relpath,
                                    "text": c.raw,
                                    "value_kw": c.value,
                                }
                                for c in reps
                            ],
                        },
                        questions=PAIR_QUESTIONS,
                    )
                    calls += 1
                    typed_sample = answers
                    relation = answers.used_choice("relation")
                    conf = answers.choice_confidence.get("relation", 0.0)
                    seed.extra = {
                        "typesafe_relation": relation,
                        "confidence": conf,
                        "noul_same_object": answers.used_noul("same_object"),
                        "score": answers.used_score("conflict_degree"),
                    }
                    if relation == "unrelated" and conf >= AUTO_ACCEPT:
                        continue
                    if relation == "uncertain" or conf < AUTO_ACCEPT:
                        seed.kind = "mismatch"
                        seed.question += f"（TypeSafe={relation}, conf={conf:.2f}，不得自动确认）"
                except Exception as exc:  # noqa: BLE001
                    seed.extra = {"reason": "typesafe-unavailable", "error": type(exc).__name__}
            seeds.append(seed)
            continue

        if kind == "cooling" and multi:
            names = {c.value.lower() for c in reps}
            if len(names) == 1:
                linked.append(
                    LinkedFact(
                        key=key,
                        claims=reps,
                        domains=domains,
                        blob_links=[wiki_blob(c, f"{ident} {c.value}") for c in reps],
                    )
                )
            else:
                seed = ChecklistSeed(
                    kind="mismatch",
                    question=(
                        f"`{ident}` 冷却选型跨域不一致："
                        + "；".join(
                            f"{DOMAIN_LABELS[c.domain]}={c.extra.get('cooling_raw', c.value)}"
                            for c in reps
                        )
                        + "。以哪一侧为准？选项：产品设计 / 解决方案 / 项目 / 采购询价 / 暂不裁定"
                    ),
                    files=[c.relpath for c in reps],
                    blobs=[c.blob for c in reps],
                )
                if client is not None and calls < max_typesafe:
                    try:
                        answers = ask_system_one(
                            client,
                            state={
                                "sku": ident,
                                "excerpts": [
                                    {
                                        "domain": DOMAIN_LABELS[c.domain],
                                        "path": c.relpath,
                                        "text": c.raw,
                                        "cooling": c.value,
                                    }
                                    for c in reps
                                ],
                            },
                            questions=PAIR_QUESTIONS,
                        )
                        calls += 1
                        typed_sample = answers
                        relation = answers.used_choice("relation")
                        conf = answers.choice_confidence.get("relation", 0.0)
                        seed.extra = {
                            "typesafe_relation": relation,
                            "confidence": conf,
                            "noul_same_object": answers.used_noul("same_object"),
                            "score": answers.used_score("conflict_degree"),
                        }
                        if relation in {"match", "unrelated"} and conf >= AUTO_ACCEPT:
                            if relation == "match":
                                linked.append(
                                    LinkedFact(
                                        key=key,
                                        claims=reps,
                                        domains=domains,
                                        blob_links=[wiki_blob(c, ident) for c in reps],
                                    )
                                )
                            continue
                        seed.question += f"（TypeSafe={relation}, conf={conf:.2f}，不得自动确认）"
                    except Exception as exc:  # noqa: BLE001
                        seed.extra = {
                            "reason": "typesafe-unavailable",
                            "error": type(exc).__name__,
                        }
                seeds.append(seed)

    return MatchReport(linked=linked, seeds=seeds, typesafe_calls=calls, typed_sample=typed_sample)
