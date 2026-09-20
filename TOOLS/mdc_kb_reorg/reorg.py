"""Real entry: snapshot, classify, cite, match, hold unconfirmed, never delete."""

from __future__ import annotations

import json
import traceback
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from typesafe_sdk import Choice, Noul, Score

from .apply_rulings import apply_rulings
from .checklist import (
    escape_bare_block_ids,
    ghost_items,
    items_from_rulings,
    render_checklist,
    seeds_to_items,
)
from .review_state import (
    KEEP_TITLE_RE,
    attach_ruling,
    blob_key,
    enrich_keep_targets,
    load_review,
    parse_checklist,
    save_review,
    should_suppress_mismatch,
)
from .claims import apply_block_ids, extract_claims, load_alias_map
from .classify import (
    DOMAIN_AMBIGUOUS,
    DOMAIN_LABELS,
    DOMAIN_UNCLASSIFIABLE,
    FOUR_DOMAINS,
    classify_path,
    typesafe_classify_file,
)
from .inventory import (
    FileRecord,
    OriginMap,
    assert_preserved,
    relocate_file,
    rewrite_vault_links,
    snapshot,
    write_inventory,
)
from .match import ChecklistSeed, MatchReport, match_claims
from .navigation import (
    patch_index_text,
    patch_navigation_text,
    patch_readme_text,
    render_domain_page,
    render_hub,
)
from .typesafe_client import MissingApiKeyError, ask_system_one, build_client, redact

HOLDING = "_holding_unconfirmed"
HOLDING_FILES = f"{HOLDING}/files"
ORIGIN_NAME = "origin-map.json"
CHECKLIST_NAME = "问题确认清单.md"
DOMAINS_DIR = "_domains"


@dataclass
class ReorgReport:
    root: str
    before_count: int
    after_count: int
    missing: list[str]
    domain_counts: dict[str, int]
    relocated: list[tuple[str, str]] = field(default_factory=list)
    typesafe_calls: int = 0
    checklist_path: str = ""
    hub_path: str = ""
    smoke: dict = field(default_factory=dict)
    typed_used: bool = False
    exit_notes: list[str] = field(default_factory=list)

    def ok(self) -> bool:
        return not self.missing


def _read_md(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _write_md(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _excerpt(path: Path, limit: int = 2500) -> str:
    if path.suffix.lower() != ".md":
        return f"(binary or non-md: {path.suffix} size={path.stat().st_size})"
    return _read_md(path)[:limit]


def smoke_typesafe(client) -> dict:
    answers = ask_system_one(
        client,
        state={
            "note": "MDC-KB reorg smoke. A product card says SKU X100TEST IT load 100 kW. "
            "A project note says the same SKU is selected. No prices."
        },
        questions={
            "about_product": Noul(
                instructions="Does this state mention a product SKU and an IT load?",
            ),
            "kind": Choice(
                instructions="What is this snippet doing?",
                criteria={
                    "match_example": "It describes two notes that should match on the same SKU.",
                    "unrelated": "It is unrelated to a knowledge-base reorg.",
                    "price": "It is asking for a price.",
                },
            ),
            "readiness": Score(
                instructions="How ready is this snippet as a smoke-test input for System One?",
                criteria=[
                    "unusable",
                    "partial but enough for a typed answer",
                    "clear smoke-test input",
                ],
            ),
        },
    )
    return {
        "noul_about_product": answers.used_noul("about_product"),
        "choice_kind": answers.used_choice("kind"),
        "score_readiness": answers.used_score("readiness"),
        "choice_confidence": answers.choice_confidence.get("kind"),
    }


def run_reorg(
    root: Path,
    *,
    live_typesafe: bool = True,
    max_typesafe: int = 28,
    apply_moves: bool = True,
    log_dir: Path | None = None,
    nav_only: bool = False,
) -> ReorgReport:
    root = root.resolve()
    holding = root / HOLDING
    holding.mkdir(parents=True, exist_ok=True)
    origin_path = holding / ORIGIN_NAME
    origin = OriginMap.load(origin_path)

    before = snapshot(root)
    aliases = load_alias_map(root)
    checklist_path = holding / CHECKLIST_NAME
    review_path = holding / "review-state.json"
    existing_text = _read_md(checklist_path) if checklist_path.is_file() else ""
    if review_path.is_file():
        rulings = load_review(review_path)
    elif existing_text:
        rulings = parse_checklist(existing_text)
        save_review(review_path, rulings)
    else:
        rulings = []
    if rulings and not nav_only:
        enrich_keep_targets(root, rulings)
        save_review(review_path, rulings)
        apply_rulings(root, rulings=rulings)
    ghost_fixed = any(r.action == "ghost_fix" for r in rulings)
    client = None
    smoke: dict = {}
    notes: list[str] = []
    ts_calls = 0
    typed_used = False

    if live_typesafe:
        client = build_client()
        smoke = smoke_typesafe(client)
        ts_calls += 1
        typed_used = True
        if log_dir is not None:
            log_dir.mkdir(parents=True, exist_ok=True)
            payload = json.dumps(smoke, ensure_ascii=False, indent=2)
            (log_dir / "typesafe-call.log").write_text(
                redact(payload) + "\n", encoding="utf-8"
            )

    # Classify every file.
    domain_of: dict[str, str] = {}
    ambiguous: list[FileRecord] = []
    for rec in before:
        domain = classify_path(rec.relpath)
        if domain == DOMAIN_AMBIGUOUS:
            ambiguous.append(rec)
        else:
            domain_of[rec.relpath] = domain

    for rec in ambiguous:
        if client is not None and ts_calls < max_typesafe:
            try:
                chosen, _ans = typesafe_classify_file(
                    client,
                    relpath=rec.relpath,
                    excerpt=_excerpt(root / rec.relpath),
                )
                ts_calls += 1
                typed_used = True
                domain_of[rec.relpath] = chosen
            except Exception as exc:  # noqa: BLE001
                domain_of[rec.relpath] = DOMAIN_UNCLASSIFIABLE
                notes.append(f"typesafe-unavailable classify {rec.relpath}: {type(exc).__name__}")
        else:
            domain_of[rec.relpath] = DOMAIN_UNCLASSIFIABLE

    # Extract claims from four-domain markdown; attach block ids.
    claims = []
    source_texts: dict[str, str] = {}
    for rec in before:
        domain = domain_of.get(rec.relpath)
        if domain not in FOUR_DOMAINS:
            continue
        path = root / rec.relpath
        if path.suffix.lower() != ".md" or not path.is_file():
            continue
        text = _read_md(path)
        file_claims = extract_claims(text, rec.relpath, domain, aliases)
        if not file_claims:
            continue
        if not nav_only:
            new_text, file_claims, changed = apply_block_ids(text, file_claims)
            if changed and apply_moves:
                _write_md(path, new_text)
                text = new_text
        source_texts[rec.relpath] = text
        claims.extend(file_claims)

    match_report: MatchReport = match_claims(
        claims,
        client,
        max_typesafe=max(0, max_typesafe - ts_calls),
        source_texts=source_texts,
    )
    ts_calls += match_report.typesafe_calls
    if match_report.typed_sample is not None:
        typed_used = True

    seeds = list(match_report.seeds)
    skip_blob_ids = set()
    for ruling in rulings:
        if ruling.action in {"close", "drop", "conflict", "keep"}:
            skip_blob_ids.update(blob_key(b) for b in ruling.blobs)
    skip_blob_ids.discard("")
    filtered: list = []
    suppress_all_mismatch = any(should_suppress_mismatch(r) for r in rulings)
    for seed in seeds:
        hit = attach_ruling(seed.question, seed.files, seed.blobs, rulings)
        if seed.kind == "mismatch" and suppress_all_mismatch:
            continue
        if seed.kind == "unconfirmed":
            ids = {blob_key(b) for b in seed.blobs}
            ids.discard("")
            if ids & skip_blob_ids:
                continue
            if hit and hit.action in {"close", "drop", "conflict", "keep"}:
                continue
        filtered.append(seed)
    seeds = filtered
    keep_rulings = [r for r in rulings if r.action == "keep"]
    for ruling in keep_rulings:
        title = ""
        m = KEEP_TITLE_RE.search(ruling.ruling_full or "")
        if m:
            title = m.group(1)
        question = ruling.question or (
            f"{ruling.item_id} {title or '仍待确认'}。选项：仍待确认 / 已可关闭 / 改为 conflict"
        )
        seeds.append(
            ChecklistSeed(
                kind="unconfirmed",
                question=question,
                files=list(ruling.files) or ["_holding_unconfirmed/问题确认清单.md"],
                blobs=list(ruling.blobs) or ["no blob"],
            )
        )
    if not ghost_fixed:
        for item in ghost_items():
            seeds.append(
                ChecklistSeed(
                    kind=item.kind,
                    question=item.question,
                    files=item.files,
                    blobs=item.blobs,
                )
            )

    relocated: list[tuple[str, str]] = []
    holding_files_dir = root / HOLDING_FILES
    if holding_files_dir.is_dir():
        for path in holding_files_dir.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(root).as_posix()
            original = origin.original_of(rel) or rel
            seeds.append(
                ChecklistSeed(
                    kind="unclassifiable",
                    question=(
                        f"holding 中的 `{original}`（现 `{rel}`）应归哪一类？"
                        "选项：产品设计 / 解决方案 / 项目 / 采购询价 / 其他 / 保持 holding"
                    ),
                    files=[original, rel],
                    blobs=["no blob", "no blob"],
                )
            )
    for rec in before:
        if domain_of.get(rec.relpath) != DOMAIN_UNCLASSIFIABLE:
            continue
        if rec.relpath.startswith(HOLDING + "/"):
            continue
        # Do not relocate well-known other buckets that slipped through.
        dest = f"{HOLDING_FILES}/{rec.relpath}"
        seeds.append(
            ChecklistSeed(
                kind="unclassifiable",
                question=(
                    f"`{rec.relpath}` 未能归入四域。迁入 holding 后应归哪一类？"
                    "选项：产品设计 / 解决方案 / 项目 / 采购询价 / 其他 / 保持 holding"
                ),
                files=[rec.relpath],
                blobs=["no blob"],
            )
        )
        if apply_moves and (root / rec.relpath).is_file():
            new_rel = relocate_file(root, rec.relpath, dest, origin)
            rewrite_vault_links(root, rec.relpath, new_rel)
            relocated.append((rec.relpath, new_rel))
            domain_of[new_rel] = DOMAIN_UNCLASSIFIABLE
            domain_of.pop(rec.relpath, None)

    # Write navigation + checklist.
    files_by_domain: dict[str, list[str]] = {d: [] for d in FOUR_DOMAINS}
    files_by_domain["other"] = []
    files_by_domain[DOMAIN_UNCLASSIFIABLE] = []
    # Re-snapshot paths after moves for domain pages.
    live_files = []
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(root).as_posix()
        live_files.append(rel)
        d = domain_of.get(rel)
        if d is None:
            d = classify_path(rel)
        files_by_domain.setdefault(d, []).append(rel)

    for d in files_by_domain:
        files_by_domain[d].sort()

    counts = {d: len(files_by_domain.get(d, [])) for d in list(FOUR_DOMAINS) + ["other", DOMAIN_UNCLASSIFIABLE]}
    domains_dir = root / DOMAINS_DIR
    domains_dir.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    _write_md(domains_dir / "index.md", render_hub(counts=counts, generated=today))
    for domain in FOUR_DOMAINS:
        page = render_domain_page(
            domain,
            files=files_by_domain.get(domain, []),
            linked=match_report.linked,
            root=root,
            generated=today,
        )
        _write_md(domains_dir / f"{DOMAIN_LABELS[domain]}.md", page)

    if rulings:
        items = items_from_rulings(rulings)
    else:
        items = seeds_to_items(seeds)
        for item in items:
            hit = attach_ruling(item.question, item.files, item.blobs, rulings)
            if hit is None and item.kind == "unconfirmed":
                for ruling in keep_rulings:
                    if ruling.item_id and ruling.item_id in item.question:
                        hit = ruling
                        break
            if hit and hit.ruling_full:
                item.compass = hit.ruling_full.lstrip(" -")
            elif item.kind == "unconfirmed" and not item.compass:
                item.compass = "🧭 **建议裁定：仍待确认** — 等外部交付物，vault 内无法闭环"
    checklist_body = render_checklist(items, generated=today)
    applied_lines = ["", "## 已按🧭落地（不再作为未决冲突重开）", ""]
    for ruling in rulings:
        if ruling.action in {"close", "conflict", "drop", "ghost_fix", "suppress_mismatch"}:
            applied_lines.append(
                f"- `{ruling.item_id}` · {ruling.action} · {escape_bare_block_ids(ruling.ruling_full)}"
            )
    if len(applied_lines) > 3:
        checklist_body = checklist_body.rstrip() + "\n" + "\n".join(applied_lines) + "\n"
    _write_md(holding / CHECKLIST_NAME, checklist_body)

    # Patch ghost indexes in place (keep all other lines).
    for rel, patcher in (
        ("index.md", patch_index_text),
        ("_navigation.md", patch_navigation_text),
        ("README.md", patch_readme_text),
    ):
        path = root / rel
        if path.is_file():
            original = _read_md(path)
            updated = patcher(original)
            if updated != original:
                _write_md(path, updated)

    origin.save(origin_path)
    (holding / "domain-map.json").write_text(
        json.dumps(domain_of, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    after = snapshot(root)
    missing = assert_preserved(before, after, origin)
    report = ReorgReport(
        root=str(root),
        before_count=len(before),
        after_count=len(after),
        missing=missing,
        domain_counts=counts,
        relocated=relocated,
        typesafe_calls=ts_calls,
        checklist_path=f"{HOLDING}/{CHECKLIST_NAME}",
        hub_path=f"{DOMAINS_DIR}/index.md",
        smoke=smoke,
        typed_used=typed_used,
        exit_notes=notes,
    )
    (holding / "last-report.json").write_text(
        json.dumps(
            {
                "before_count": report.before_count,
                "after_count": report.after_count,
                "missing": report.missing,
                "domain_counts": report.domain_counts,
                "relocated": report.relocated,
                "typesafe_calls": report.typesafe_calls,
                "typed_used": report.typed_used,
                "smoke": report.smoke,
                "notes": report.exit_notes,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return report
