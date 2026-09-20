"""问题确认清单 — Yuri marks by hand. Never auto-close."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from .classify import DOMAIN_LABELS
from .match import ChecklistSeed
from .review_state import KEEP_TITLE_RE, Ruling


@dataclass
class ChecklistItem:
    question: str
    files: list[str]
    blobs: list[str]
    kind: str
    options: str = ""
    compass: str = ""


def items_from_rulings(rulings: list[Ruling]) -> list[ChecklistItem]:
    """Rebuild Yuri's 265-item list from persisted 🧭 (checkboxes stay unchecked)."""
    items: list[ChecklistItem] = []
    for ruling in rulings:
        title = ""
        m = KEEP_TITLE_RE.search(ruling.ruling_full or "")
        if m:
            title = m.group(1)
        question = ruling.question or (
            f"{ruling.item_id} {title}".strip()
            if title
            else ruling.ruling or ruling.item_id
        )
        items.append(
            ChecklistItem(
                question=question,
                files=list(ruling.files),
                blobs=list(ruling.blobs) or ["no blob"],
                kind=ruling.kind,
                compass=escape_bare_block_ids(ruling.ruling_full),
            )
        )
    return items


def seeds_to_items(seeds: list[ChecklistSeed]) -> list[ChecklistItem]:
    items: list[ChecklistItem] = []
    seen: set[tuple] = set()
    for seed in seeds:
        key = (seed.kind, seed.question, tuple(seed.files), tuple(seed.blobs))
        if key in seen:
            continue
        seen.add(key)
        blobs = [b if b else "no blob" for b in seed.blobs] or ["no blob"]
        items.append(
            ChecklistItem(
                question=seed.question,
                files=list(seed.files),
                blobs=blobs,
                kind=seed.kind,
            )
        )
    return items


def render_checklist(items: list[ChecklistItem], *, generated: str | None = None) -> str:
    generated = generated or date.today().isoformat()
    lines = [
        "---",
        "tags:",
        '  - "#workspace/engineer"',
        '  - "#type/checklist"',
        '  - "#unconfirmed"',
        "  - #MDC",
        "generated: true",
        f"updated: {generated}",
        "status: 待 Yuri 手改确认",
        "---",
        "# 问题确认清单",
        "",
        "> 本清单由 `TOOLS/mdc_kb_reorg` 生成。**不得自动关闭。** 每一项都需要 Yuri 手改勾选。",
        "> TypeSafe 只做分类与引用核验，**不改写工程数字、不删除文件**。",
        "",
        f"生成日期：{generated} · 共 {len(items)} 项",
        "",
        "> 🧭 建议裁定来自既有核查，重跑不得抹掉。勾选框仍须 Yuri 手改。",
        "",
    ]
    by_kind: dict[str, list[ChecklistItem]] = {}
    order = [
        "ghost",
        "mismatch",
        "unconfirmed",
        "unsourced",
        "unclassifiable",
        "typesafe",
        "duplicate",
    ]
    labels = {
        "ghost": "幽灵索引",
        "mismatch": "跨域不一致",
        "unconfirmed": "已标 #unconfirmed",
        "unsourced": "无来源主张",
        "unclassifiable": "未分类文件（已迁入 holding 或待迁）",
        "typesafe": "TypeSafe 未能判定",
        "duplicate": "重复件（按目标保留，不得删除）",
    }
    for item in items:
        by_kind.setdefault(item.kind, []).append(item)
    for kind in order:
        group = by_kind.get(kind) or []
        if not group:
            continue
        lines.append(f"## {labels.get(kind, kind)}")
        lines.append("")
        for i, item in enumerate(group, start=1):
            lines.append(f"- [ ] **{kind}-{i:03d}** {item.question}")
            if item.compass:
                lines.append(f"  - {escape_bare_block_ids(item.compass)}")
            for path, blob in _zip_pad(item.files, item.blobs):
                blob_txt = format_blob_citation(blob)
                wiki = f"[[{path}]]" if path.endswith(".md") or "/" in path else path
                if path.endswith(".md"):
                    wiki = f"[[{path[:-3]}]]"
                lines.append(f"  - 文件: `{path}` {wiki}")
                lines.append(f"  - blob: {blob_txt}")
            lines.append("")
    leftover = [k for k in by_kind if k not in order]
    for kind in leftover:
        lines.append(f"## {kind}")
        lines.append("")
        for i, item in enumerate(by_kind[kind], start=1):
            lines.append(f"- [ ] **{kind}-{i:03d}** {item.question}")
            if item.compass:
                lines.append(f"  - {escape_bare_block_ids(item.compass)}")
            for path, blob in _zip_pad(item.files, item.blobs):
                lines.append(f"  - 文件: `{path}`")
                lines.append(f"  - blob: {format_blob_citation(blob)}")
            lines.append("")
    lines.append("## Changelog")
    lines.append("")
    lines.append("| 日期 | 变更 |")
    lines.append("|---|---|")
    lines.append(f"| {generated} | 首次由 mdc_kb_reorg 生成 |")
    lines.append("")
    return "\n".join(lines)


def escape_bare_block_ids(text: str) -> str:
    """Wrap bare ^ids so Obsidian does not treat checklist lines as block definitions."""
    if not text:
        return text
    parts = re.split(r"(`[^`]*`|\[\[[^\]]*\]\])", text)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(part)
        else:
            out.append(re.sub(r"\^[A-Za-z0-9_-]+", lambda m: f"`{m.group(0)}`", part))
    return "".join(out)


def format_blob_citation(blob: str) -> str:
    if not blob or blob == "no blob":
        return "no blob"
    raw = blob.strip().strip("[]")
    if raw.startswith("[[") and raw.endswith("]]"):
        raw = raw[2:-2]
    if raw.startswith("^") or re.match(r"mdc-[0-9a-f]+$", raw):
        token = raw if raw.startswith("^") else f"^{raw}"
        return f"`{token}`"
    if "#^" in raw or "#" in raw:
        return f"[[{raw}]]"
    return f"`{raw}`"


def _zip_pad(files: list[str], blobs: list[str]) -> list[tuple[str, str]]:
    n = max(len(files), len(blobs), 1)
    out = []
    for i in range(n):
        f = files[i] if i < len(files) else (files[-1] if files else "")
        b = blobs[i] if i < len(blobs) else (blobs[-1] if blobs else "no blob")
        out.append((f, b))
    return out


def ghost_items() -> list[ChecklistItem]:
    return [
        ChecklistItem(
            kind="ghost",
            question=(
                "`index.md` / `_navigation.md` / `README.md` 指向 `Solutions Design/`，"
                "但该目录不存在。是否将「解决方案」入口固定为 `Reference Architecture/` + `PUBLIC/`？"
                "选项：是，固定 / 否，我将重建 Solutions Design/"
            ),
            files=["index.md", "_navigation.md", "README.md"],
            blobs=["no blob", "no blob", "no blob"],
        ),
        ChecklistItem(
            kind="ghost",
            question=(
                "`index.md` 与 `README.md` 指向 `SupplyChain/`，但该目录不存在。"
                "是否将「采购询价」入口固定为各 `**/PROCUREMENT/**` 与项目 `RFI*` 包？"
                "选项：是，固定 / 否，我将重建 SupplyChain/"
            ),
            files=["index.md", "README.md"],
            blobs=["no blob", "no blob"],
        ),
    ]
