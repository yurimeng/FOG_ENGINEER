"""Four-domain navigation with working blob citations. Bind ghosts to real files."""

from __future__ import annotations

from collections import defaultdict
from datetime import date
from pathlib import Path

from .classify import DOMAIN_LABELS, FOUR_DOMAINS
from .match import LinkedFact

DOMAIN_ENTRIES = {
    "product": [
        ("KB/index", "KB 索引"),
        ("KB/_COMMON/PRODUCT_SPEC_BASELINE", "六 SKU 规格基准"),
        ("KB/NAMING_MAP", "命名映射"),
        ("KB/_COMMON/UNCONFIRMED_Convention", "#unconfirmed 规范"),
        ("KB/LIQUID/index", "Liquid Cooling"),
        ("KB/IMMERSION/index", "Immersion Cooling"),
        ("KB/3RD-PARTY/index", "第三方"),
        ("KB/Guideline/index", "Guideline"),
        ("KB/POWER/index", "电力舱（非 SKU）"),
    ],
    "solution": [
        ("Reference Architecture/index", "Reference Architecture 工作稿"),
        ("PUBLIC/README", "PUBLIC 对外入口"),
        ("PUBLIC/Reference_Architecture/RA-001_Immersion_0.4MW", "RA-001 Immersion 0.4MW"),
        ("PUBLIC/Reference_Architecture/RA-002_Liquid_1.2MW", "RA-002 Liquid 1.2MW"),
        ("PUBLIC/Tech_Spec", "Tech Spec 对外稿"),
    ],
    "project": [
        ("Projects/project_list", "项目总览"),
        ("Projects/index", "Projects 索引"),
        ("Projects/外发资料_最新/index", "外发资料"),
    ],
    "procurement": [
        ("KB/LIQUID/L1800C45/PROCUREMENT", "L1800C45 PROCUREMENT"),
        ("KB/3RD-PARTY/IT-PLATFORM/RFI", "IT-PLATFORM RFI"),
    ],
}

GHOST_NOTE = {
    "solution": "`Solutions Design/` 不存在；解决方案入口已固定为 `Reference Architecture/` + `PUBLIC/`。",
    "procurement": "`SupplyChain/` 不存在；采购询价入口已固定为 `**/PROCUREMENT/**` 与项目 `RFI*`。",
}


def _existing_target(root: Path, target: str) -> bool:
    rel = target if target.endswith(".md") else f"{target}.md"
    if (root / rel).exists() or (root / target).exists():
        return True
    # directory
    return (root / target).is_dir()


def render_domain_page(
    domain: str,
    *,
    files: list[str],
    linked: list[LinkedFact],
    root: Path,
    generated: str | None = None,
) -> str:
    generated = generated or date.today().isoformat()
    label = DOMAIN_LABELS[domain]
    lines = [
        "---",
        "tags:",
        '  - "#workspace/engineer"',
        '  - "#type/index"',
        "  - #MDC",
        "generated: true",
        f"domain: {label}",
        f"updated: {generated}",
        "---",
        f"# {label}",
        "",
        f"> 四域导航之一。引用走 Obsidian blob：`[[note#^block]]`。生成日期 {generated}。",
        "",
    ]
    if domain in GHOST_NOTE:
        lines.append(f"> [!warning] 幽灵索引 {GHOST_NOTE[domain]}")
        lines.append("")
    lines.append("## 入口")
    lines.append("")
    for target, title in DOMAIN_ENTRIES.get(domain, []):
        if _existing_target(root, target):
            lines.append(f"- [[{target}|{title}]]")
        else:
            lines.append(f"- `{target}` — 缺失，见 [[_holding_unconfirmed/问题确认清单]]（no blob）")
    lines.append("")
    lines.append("## 跨域已匹配（blob）")
    lines.append("")
    domain_links = [fact for fact in linked if domain in fact.domains]
    if not domain_links:
        lines.append("（本域暂无跨域匹配项）")
        lines.append("")
    else:
        lines.append("| 键 | 匹配 blob |")
        lines.append("|---|---|")
        for fact in domain_links[:80]:
            kind, ident = fact.key
            blobs = " · ".join(fact.blob_links)
            lines.append(f"| `{kind}:{ident}` | {blobs} |")
        lines.append("")
    lines.append("## 本域文件（抽样入口 + 计数）")
    lines.append("")
    md = [f for f in files if f.endswith(".md")]
    lines.append(f"共 {len(files)} 个文件，其中 markdown {len(md)}。")
    lines.append("")
    for rel in md[:40]:
        note = rel[:-3] if rel.endswith(".md") else rel
        lines.append(f"- [[{note}]]")
    if len(md) > 40:
        lines.append(f"- … 其余 {len(md) - 40} 个 md 见库存，不在此展开")
    lines.append("")
    lines.append("## Changelog")
    lines.append("")
    lines.append("| 日期 | 变更 |")
    lines.append("|---|---|")
    lines.append(f"| {generated} | mdc_kb_reorg 生成四域入口 |")
    lines.append("")
    return "\n".join(lines)


def render_hub(*, counts: dict[str, int], generated: str | None = None) -> str:
    generated = generated or date.today().isoformat()
    lines = [
        "---",
        "tags:",
        '  - "#workspace/engineer"',
        '  - "#type/index"',
        "  - #MDC",
        "generated: true",
        f"updated: {generated}",
        "---",
        "# 四域导航",
        "",
        "> 产品设计 / 解决方案 / 项目 / 采购询价。每域入口可跳到 **blob** 级引用。",
        "> 未确认项：[[_holding_unconfirmed/问题确认清单]]",
        "",
        "| 域 | 入口 | 文件数 |",
        "|---|---|---|",
    ]
    for domain in FOUR_DOMAINS:
        label = DOMAIN_LABELS[domain]
        lines.append(f"| {label} | [[_domains/{label}]] | {counts.get(domain, 0)} |")
    lines.append("")
    lines.append("幽灵路径 `Solutions Design/`、`SupplyChain/` 已绑定到上表真实目录，并列入确认清单。")
    lines.append("")
    lines.append("## Changelog")
    lines.append("")
    lines.append("| 日期 | 变更 |")
    lines.append("|---|---|")
    lines.append(f"| {generated} | 首次生成四域导航 |")
    lines.append("")
    return "\n".join(lines)


def patch_index_text(text: str) -> str:
    """Bind ghost folder bullets to real domain indexes. Do not delete other lines."""
    replacements = {
        "- Solutions Design/": (
            "- 解决方案 → [[_domains/解决方案]] "
            "（`Solutions Design/` 不存在，入口已固定为 Reference Architecture/ + PUBLIC/）"
        ),
        "- SupplyChain/": (
            "- 采购询价 → [[_domains/采购询价]] "
            "（`SupplyChain/` 不存在，入口已固定为 PROCUREMENT/ 与项目 RFI*）"
        ),
    }
    out = text
    for old, new in replacements.items():
        if old in out and new not in out:
            out = out.replace(old, new)
    out = out.replace(
        "（原 `Solutions Design/` 为幽灵路径，见 [[_holding_unconfirmed/问题确认清单]]）",
        "（`Solutions Design/` 不存在，入口已固定为 Reference Architecture/ + PUBLIC/）",
    )
    out = out.replace(
        "（原 `SupplyChain/` 为幽灵路径，见 [[_holding_unconfirmed/问题确认清单]]）",
        "（`SupplyChain/` 不存在，入口已固定为 PROCUREMENT/ 与项目 RFI*）",
    )
    if "- 产品设计 → [[_domains/产品设计]]" not in out:
        # Keep original KB/ Projects/ lines; add a four-domain pointer near the top list.
        marker = "## Workspaces" if "## Workspaces" in out else None
        inject = (
            "\n- 四域导航 → [[_domains/index]] · "
            "[[_domains/产品设计]] · [[_domains/解决方案]] · [[_domains/项目]] · [[_domains/采购询价]]\n"
        )
        if "- KB/" in out and inject.strip() not in out:
            out = out.replace("- KB/", "- 产品设计 → [[_domains/产品设计]]（实体仍在 `KB/`）\n- KB/", 1)
        if "- Projects/" in out and "[[_domains/项目]]" not in out:
            out = out.replace(
                "- Projects/",
                "- 项目 → [[_domains/项目]]（实体仍在 `Projects/`）\n- Projects/",
                1,
            )
        if "- Reference Architecture/" in out and "[[_domains/解决方案]]" not in out.split("Solutions Design")[0]:
            pass
        if inject.strip() not in out:
            out = out.replace("# FOG / index", "# FOG / index" + inject, 1)
    return out


def patch_navigation_text(text: str) -> str:
    old = "| 方案设计 | [[Solutions Design/index]] | 方案设计稿 |"
    new = (
        "| 解决方案 | [[_domains/解决方案]] · [[Reference Architecture/index]] · [[PUBLIC/README]] "
        "| `Solutions Design/` 不存在，入口已固定 |"
    )
    if old in text:
        text = text.replace(old, new)
    text = text.replace(
        "原 `Solutions Design/` 为幽灵路径，见 [[_holding_unconfirmed/问题确认清单]]",
        "`Solutions Design/` 不存在，入口已固定",
    )
    text = text.replace(
        "原 `SupplyChain/` 为幽灵路径；实体为 `**/PROCUREMENT/**` 与项目 `RFI*`",
        "`SupplyChain/` 不存在；入口已固定为 `**/PROCUREMENT/**` 与项目 `RFI*`",
    )
    extra = (
        "| 采购询价 | [[_domains/采购询价]] | `SupplyChain/` 不存在；入口已固定为 `**/PROCUREMENT/**` 与项目 `RFI*` |"
    )
    if extra not in text and "| 项目 |" in text:
        text = text.replace(
            "| 项目 | [[project_list]] → 各项目目录 | 客户项目（修改需 Yuri 确认）|",
            "| 项目 | [[_domains/项目]] · [[project_list]] | 客户项目（修改需 Yuri 确认）|\n" + extra,
        )
    if "| 产品 KB |" in text and "[[_domains/产品设计]]" not in text:
        text = text.replace(
            "| 产品 KB |",
            "| 产品设计 | [[_domains/产品设计]] | 四域入口 |\n| 产品 KB |",
        )
    return text


def patch_readme_text(text: str) -> str:
    text = text.replace(
        "├── Solutions Design/     ← 方案设计",
        "├── Reference Architecture/ + PUBLIC/  ← 解决方案（Solutions Design/ 不存在，入口已固定）",
    )
    text = text.replace(
        "SupplyChain、",
        "SupplyChain（目录不存在，采购询价见 PROCUREMENT/RFI*）、",
    )
    text = text.replace("为幽灵路径", "不存在，入口已固定")
    text = text.replace("幽灵路径，见", "不存在，入口已固定；见")
    text = text.replace("原 `Solutions Design/` 为幽灵路径，见 [[_holding_unconfirmed/问题确认清单]]",
                        "`Solutions Design/` 不存在，入口已固定为 Reference Architecture/ + PUBLIC/")
    text = text.replace("原 `SupplyChain/` 为幽灵路径", "`SupplyChain/` 不存在，入口已固定")
    pointer = (
        "四域导航 → [[_domains/index]] · [[_domains/产品设计]] · "
        "[[_domains/解决方案]] · [[_domains/项目]] · [[_domains/采购询价]]"
    )
    if "[[_domains/" not in text:
        if "# Engineer Workspace" in text:
            text = text.replace(
                "# Engineer Workspace",
                "# Engineer Workspace\n\n" + pointer,
                1,
            )
        else:
            text = pointer + "\n\n" + text
    return text
