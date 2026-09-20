"""Apply 🧭 建议裁定: copy cited source onto the blob line, then ✅/⛔ + Changelog."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from .review_state import Ruling, parse_checklist

# Target file + blob for 🧭 closes (original 265-item checklist).
# Source block-ids in 🧭 text (e.g. baseline ^mdc-17e97f5584) are NOT targets.
CLOSE_TARGETS: dict[str, dict] = {
    "unconfirmed-016": {
        "files": ["KB/_COMMON/PRODUCTS_MDC.md"],
        "blobs": [
            "KB/_COMMON/PRODUCTS_MDC#^mdc-53377e92cf",
            "KB/_COMMON/PRODUCTS_MDC#^mdc-a4c1845fae",
        ],
    },
    "unconfirmed-121": {
        "files": ["KB/3RD-PARTY/3rd Party List.md"],
        "blobs": ["KB/3RD-PARTY/3rd Party List#^mdc-7352fb76ea"],
    },
    "unconfirmed-127": {
        "files": ["KB/3RD-PARTY/_blocks/STD_Supplier/02_Supplier_Table_Cooling_Power.md"],
        "blobs": [
            "KB/3RD-PARTY/_blocks/STD_Supplier/02_Supplier_Table_Cooling_Power#^mdc-71067ab178"
        ],
    },
    "unconfirmed-174": {
        "files": ["KB/3RD-PARTY/_blocks/3rd_Party_List/02_Cooling_Zone.md"],
        "blobs": [
            "KB/3RD-PARTY/_blocks/3rd_Party_List/02_Cooling_Zone#^mdc-91ee582d14",
            "KB/3RD-PARTY/_blocks/3rd_Party_List/02_Cooling_Zone#^mdc-65d4483355",
        ],
    },
    "unconfirmed-175": {
        "files": ["KB/3RD-PARTY/_blocks/3rd_Party_List/05_Changelog.md"],
        "blobs": [
            "KB/3RD-PARTY/_blocks/3rd_Party_List/05_Changelog#^mdc-473ef8fc22"
        ],
    },
    "unconfirmed-178": {
        "files": ["KB/_COMMON/PRODUCT_SPEC_BASELINE.md"],
        "blobs": [
            "KB/_COMMON/PRODUCT_SPEC_BASELINE#^mdc-311342bcd7",
            "KB/_COMMON/PRODUCT_SPEC_BASELINE#^mdc-cw320-l450-idx",
        ],
    },
    "unconfirmed-014": {
        "files": ["PUBLIC/Tech_Spec/I200C20_Tech_Spec_EN.md"],
        "blobs": [
            "PUBLIC/Tech_Spec/I200C20_Tech_Spec_EN#^mdc-64a9973cf1",
            "PUBLIC/Tech_Spec/I200C20_Tech_Spec_EN#^mdc-6e873c57fe",
        ],
    },
    "unconfirmed-052": {
        "files": ["PUBLIC/Tech_Spec/I200C20_Tech_Spec_CN.md"],
        "blobs": [
            "PUBLIC/Tech_Spec/I200C20_Tech_Spec_CN#^mdc-b5a5aef8f8",
            "PUBLIC/Tech_Spec/I200C20_Tech_Spec_CN#^mdc-290d058a5d",
        ],
    },
    "unconfirmed-053": {
        "files": ["PUBLIC/Tech_Spec/I200C20_Tech_Spec_EN.md"],
        "blobs": [
            "PUBLIC/Tech_Spec/I200C20_Tech_Spec_EN#^mdc-64a9973cf1",
            "PUBLIC/Tech_Spec/I200C20_Tech_Spec_EN#^mdc-6e873c57fe",
        ],
    },
    "unconfirmed-124": {
        "files": ["KB/3RD-PARTY/_blocks/3rd_Party_List/02_Cooling_Zone.md"],
        "blobs": ["KB/3RD-PARTY/_blocks/3rd_Party_List/02_Cooling_Zone#^mdc-ae56d585a0"],
    },
    "unconfirmed-128": {
        "files": ["KB/Guideline/_blocks/COOLING_SYSTEM_Guideline/08_G14_G15_Product_Lookup.md"],
        "blobs": ["KB/Guideline/_blocks/COOLING_SYSTEM_Guideline/08_G14_G15_Product_Lookup#^mdc-089b6a4cbe"],
    },
    "unconfirmed-151": {
        "files": ["PUBLIC/Tech_Spec/L1800C45_Tech_Spec_EN.md"],
        "blobs": ["PUBLIC/Tech_Spec/L1800C45_Tech_Spec_EN#^mdc-e439506972"],
    },
    "unconfirmed-194": {
        "files": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_EN.md"],
        "blobs": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_EN#^mdc-5b14f34fb7"],
    },
    "unconfirmed-195": {
        "files": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_EN.md"],
        "blobs": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_EN#^mdc-eb0d98c0af"],
    },
}

CLOSE_FILES: dict[str, list[str]] = {
    "unconfirmed-016": ["KB/_COMMON/PRODUCTS_MDC.md"],
    "unconfirmed-095": ["KB/3RD-PARTY/COOLING/index.md"],
    "unconfirmed-121": ["KB/3RD-PARTY/3rd Party List.md"],
    "unconfirmed-122": ["KB/3RD-PARTY/COOLING/Suppliers/PRD-STULZ-CRS560CW.md"],
    "unconfirmed-127": ["KB/3RD-PARTY/_blocks/STD_Supplier/02_Supplier_Table_Cooling_Power.md"],
    "unconfirmed-140": ["PUBLIC/Tech_Spec/L1800C45_Tech_Spec_CN.md"],
    "unconfirmed-159": ["PUBLIC/Tech_Spec/L1800C45_Tech_Spec_EN.md"],
    "unconfirmed-174": ["KB/3RD-PARTY/_blocks/3rd_Party_List/02_Cooling_Zone.md"],
    "unconfirmed-175": ["KB/3RD-PARTY/_blocks/3rd_Party_List/05_Changelog.md"],
    "unconfirmed-177": ["KB/_COMMON/PRODUCT_SPEC_BASELINE.md"],
    "unconfirmed-178": ["KB/_COMMON/PRODUCT_SPEC_BASELINE.md"],
    "unconfirmed-207": ["KB/3RD-PARTY/COOLING/DESIGN/Hybrid Chiller Requirement V6.md"],
    "unconfirmed-214": ["KB/_COMMON/MDCX_Connector_Standard_A1.md"],
    "unconfirmed-216": ["KB/_COMMON/MDCX_Connector_Standard_A1.md"],
    "unconfirmed-218": ["KB/_COMMON/PRODUCT_SPEC_BASELINE.md"],
    "unconfirmed-219": ["KB/_COMMON/PRODUCT_SPEC_BASELINE.md"],
    "unconfirmed-220": ["KB/_COMMON/PRODUCT_SPEC_BASELINE.md"],
    "unconfirmed-223": ["PUBLIC/Tech_Spec/L1800C45_Tech_Spec_EN.md"],
}

# 24 🧭 conflict items: recovered from 🧭 text + first apply Changelog paths.
CONFLICT_TARGETS: dict[str, dict] = {
    "unconfirmed-005": {
        "files": ["PUBLIC/Tech_Spec/I200C20_Tech_Spec_CN.md"],
        "blobs": ["PUBLIC/Tech_Spec/I200C20_Tech_Spec_CN#^mdc-1dceca2279"],
    },
    "unconfirmed-011": {
        "files": ["PUBLIC/Tech_Spec/I200C20_Tech_Spec_EN.md"],
        "blobs": ["PUBLIC/Tech_Spec/I200C20_Tech_Spec_EN#^mdc-adfe4ba9b3"],
    },
    "unconfirmed-021": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/05_Sec5_Cooling.md"],
        "blobs": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/05_Sec5_Cooling#^mdc-3b50fce49d"],
    },
    "unconfirmed-022": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/05_Sec5_Cooling.md"],
        "blobs": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/05_Sec5_Cooling#^mdc-3bb5bee382"],
    },
    "unconfirmed-031": {
        "files": [
            "PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/14_Sec14_Summary.md",
            "PUBLIC/Reference_Architecture/RA-001_Immersion_0.4MW.md",
        ],
        "blobs": [
            "PUBLIC/Reference_Architecture/RA-001_Immersion_0.4MW#^mdc-93e8366578",
        ],
    },
    "unconfirmed-032": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/14_Sec14_Summary.md"],
        "blobs": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/14_Sec14_Summary#^mdc-7df1a03380"],
    },
    "unconfirmed-037": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/05_Sec5_Cooling.md"],
        "blobs": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/05_Sec5_Cooling#^mdc-d2b7598593"],
    },
    "unconfirmed-038": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/05_Sec5_Cooling.md"],
        "blobs": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/05_Sec5_Cooling#^mdc-6ddaf9d626"],
    },
    "unconfirmed-047": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/14_Sec14_Summary.md"],
        "blobs": ["PUBLIC/Reference_Architecture/RA-001_Immersion_0.4MW#^mdc-93e8366578"],
    },
    "unconfirmed-048": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/14_Sec14_Summary.md"],
        "blobs": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/14_Sec14_Summary#^mdc-168b2323a0"],
    },
    "unconfirmed-050": {
        "files": ["PUBLIC/Reference_Architecture/RA-001_Immersion_0.4MW.md"],
        "blobs": ["PUBLIC/Reference_Architecture/RA-001_Immersion_0.4MW#^mdc-93e8366578"],
    },
    "unconfirmed-051": {
        "files": ["PUBLIC/Reference_Architecture/RA-003_Immersion_0.2MW_All-in-One.md"],
        "blobs": ["PUBLIC/Reference_Architecture/RA-003_Immersion_0.2MW_All-in-One#^mdc-9ec0383499"],
    },
    "unconfirmed-062": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/03_Sec3_IT_Capacity.md"],
        "blobs": ["PUBLIC/Reference_Architecture/RA-001_Immersion_0.4MW#^mdc-93e8366578"],
    },
    "unconfirmed-063": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/05_Sec5_Cooling.md"],
        "blobs": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/05_Sec5_Cooling#^mdc-87e9a7b4b0"],
    },
    "unconfirmed-064": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/03_Sec3_IT_Capacity.md"],
        "blobs": ["PUBLIC/Reference_Architecture/RA-001_Immersion_0.4MW#^mdc-93e8366578"],
    },
    "unconfirmed-065": {
        "files": ["PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/05_Sec5_Cooling.md"],
        "blobs": [],
    },
    "unconfirmed-108": {
        "files": ["KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec EN.md"],
        "blobs": [
            "KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec EN#^sec-12-service",
            "KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec EN#^sec-13-site",
        ],
    },
    "unconfirmed-168": {
        "files": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_CN.md"],
        "blobs": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_CN#^mdc-da0a45bd52"],
    },
    "unconfirmed-170": {
        "files": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_EN.md"],
        "blobs": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_EN#^mdc-ee741dedcc"],
    },
    "unconfirmed-222": {
        "files": ["PUBLIC/Tech_Spec/L1800C45_Tech_Spec_CN.md"],
        "blobs": ["PUBLIC/Tech_Spec/L1800C45_Tech_Spec_CN#^mdc-7f548b9f7e"],
    },
    "unconfirmed-224": {
        "files": ["PUBLIC/Tech_Spec/L1800C45_Tech_Spec_EN.md"],
        "blobs": ["PUBLIC/Tech_Spec/L1800C45_Tech_Spec_EN#^mdc-3388896cc2"],
    },
    "unconfirmed-225": {
        "files": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_CN.md"],
        "blobs": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_CN#^mdc-0fb77f0b32"],
    },
    "unconfirmed-226": {
        "files": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_EN.md"],
        "blobs": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_EN#^mdc-a81870e23f"],
    },
    "unconfirmed-227": {
        "files": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_EN.md"],
        "blobs": ["PUBLIC/Tech_Spec/L450C20_Tech_Spec_EN#^mdc-96418a1475"],
    },
}

PATH_IN_TEXT_RE = re.compile(
    r"(?:KB|PUBLIC|Projects|Reference Architecture)/[A-Za-z0-9_./ \u4e00-\u9fff-]+\.md"
)
ANCHOR_RE = re.compile(r"\^((?:mdc-[0-9a-f]+|sec-[A-Za-z0-9_-]+|baseline-[A-Za-z0-9_-]+))")
CHANGELOG_HEAD_RE = re.compile(r"^##\s+Changelog\b", re.M | re.I)
STRAY_ROW_RE = re.compile(r"^\| 20\d{2}-\d{2}-\d{2} \| 🧭 .+?\|\s*$")


@dataclass
class ApplyReport:
    closed: list[str] = field(default_factory=list)
    conflicted: list[str] = field(default_factory=list)
    dropped: list[str] = field(default_factory=list)
    ghosts: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    files_touched: list[str] = field(default_factory=list)


def apply_status_on_line(line: str, status: str) -> str:
    """Idempotent row-status rewrite. Does not touch frontmatter."""
    if line.lstrip().startswith("---") or line.lstrip().startswith("tags:"):
        return line
    newline = ""
    if line.endswith("\r\n"):
        core, newline = line[:-2], "\r\n"
    elif line.endswith("\n"):
        core, newline = line[:-1], "\n"
    else:
        core = line
    if status == "conflict":
        core = _swap_mark(core, "⛔ **conflict**")
    elif status == "not_provided":
        core = _swap_mark(core, "❌")
    else:
        core = _swap_mark(core, "✅")
    return core + newline


def _swap_mark(core: str, new_mark: str) -> str:
    patterns = (
        "⏳ **#unconfirmed**",
        "⏳ **unconfirmed**",
        "⏳ #unconfirmed",
        "⏳",
    )
    out = core
    replaced = False
    for pat in patterns:
        if pat in out:
            out = out.replace(pat, new_mark, 1)
            replaced = True
            break
    if "#unconfirmed" in out and new_mark != "⏳ #unconfirmed":
        out = out.replace(" #unconfirmed", "", 1).replace("#unconfirmed", "", 1)
        if not replaced:
            out = f"{out} {new_mark}" if new_mark not in out else out
            replaced = True
    if not replaced and new_mark not in out and ("unconfirmed" in core.lower() or "⏳" in core):
        out = f"{out} {new_mark}"
    if not replaced and new_mark.startswith("⛔") and "⛔" not in out:
        bm = re.search(r"(\s+\^[A-Za-z0-9_-]+)\s*$", out)
        if bm:
            out = out[: bm.start()].rstrip() + f" {new_mark}" + bm.group(1)
        else:
            out = f"{out} {new_mark}"
    return out


def _zh(line: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", line))


def source_value(ruling: Ruling, line: str) -> str | None:
    """Value copied from the 🧭-named source. Language follows the target line."""
    full = ruling.ruling_full
    zh = _zh(line)
    if re.search(r"9 柜|九柜|= 9 柜", full) and "L1800" in full:
        return (
            "**9**（8× 220 kW 液冷 + 1× 40 kW 风冷，站点 profile l1800.json）"
            if zh
            else "**9** (8× 220 kW liquid + 1× 40 kW air, site profile l1800.json)"
        )
    if "3× 150" in full or re.search(r"3 柜|三柜|= 3 柜", full):
        if "构成" in full or "composition" in full.lower() or "Rack count and composition" in line:
            return (
                "**3× 150 kW 液冷，无风冷柜**（站点 profile l450.json）"
                if zh
                else "**3× 150 kW liquid, no air rack** (site profile l450.json)"
            )
        return (
            "**3**（3× 150 kW 液冷、无风冷柜，站点 profile l450.json）"
            if zh
            else "**3** (3× 150 kW liquid, no air rack, site profile l450.json)"
        )
    if "5 kW" in full and ("风冷" in full or "air" in full.lower() or "Air branch" in full):
        return (
            "**1× 5 kW 风冷柜**（4× I50TS + 1× 5 kW；[[PRODUCT_SPEC_BASELINE]] §2.1 ✅ 站点 Designer；Changelog v2.1 关闭 KC-4）"
            if zh
            else "**1× 5 kW air-cooled rack** (4× I50TS + 1× 5 kW; baseline §2.1 / KC-4 closed)"
        )
    if "9 柜" in full or "九柜" in full:
        return "**9**" if zh else "**9**"
    if "3 柜" in full or "三柜" in full:
        return "**3**" if zh else "**3**"
    return None


def _replace_waiting_cell(line: str, value: str) -> str:
    if not line.lstrip().startswith("|"):
        return line
    parts = line.split("|")
    for i, cell in enumerate(parts):
        if len(cell.strip()) <= 3:
            continue
        if re.search(
            r"waiting|TBD|未列出|lists no air|因此不写风冷|expected TBD|预期 TBD",
            cell,
            re.I,
        ):
            parts[i] = f" {value} "
            return "|".join(parts)
    return line


def apply_source_value(line: str, ruling: Ruling) -> str:
    """Copy the cited source onto the row, then mark ✅. Must not leave 'waiting … TBD'."""
    full = ruling.ruling_full
    value = source_value(ruling, line)
    out = line
    if value:
        out = _replace_waiting_cell(out, value)
        # prose / leftover waiting
        out = re.sub(
            r"(✅\s*—\s*)?waiting on[^|]+?(expected TBD)?",
            value,
            out,
            flags=re.I,
        )
        out = re.sub(r"等[^|。]*预期 TBD", value, out)
        bid = ""
        bm = re.search(r"(\^[A-Za-z0-9_-]+)\s*$", out)
        if bm:
            bid = " " + bm.group(1)
        if "I400C45 and I400C40 each include one 10 kW" in out or "therefore does not claim one" in out:
            out = (
                "> ⚠️ **Note: I400C45 and I400C40 each include one 10 kW air-cooled rack; "
                "the I200C20 column of [[PRODUCT_SPEC_BASELINE]] lists 1× 5 kW air-cooled rack.** "
                "This document follows the baseline: I200C20 is **4× I50TS + 1× 5 kW air-cooled rack** "
                "(✅ site Designer; Changelog v2.1 closed KC-4)."
                f"{bid}\n"
            )
        elif "I400C45 / I400C40 各含 1 台 10 kW" in out or "是否配置风冷柜" in out:
            out = (
                "> ⚠️ **注意：I400C45 / I400C40 各含 1 台 10 kW 风冷机柜；"
                "[[PRODUCT_SPEC_BASELINE]] 的 I200C20 一列已列出 1× 5 kW 风冷柜。** "
                "本文档按基准表：I200C20 为 **4× I50TS + 1× 5 kW 风冷柜**"
                "（✅ 站点 Designer；Changelog v2.1 关闭 KC-4）。"
                f"{bid}\n"
            )
        elif "未列出风冷机柜" in out or "一列未列出风冷" in out or "因此不写风冷" in out:
            out = out.replace("未列出风冷机柜", "已列出 1× 5 kW 风冷柜")
            out = out.replace("因此不写风冷机柜", "按基准表写入 1× 5 kW 风冷柜")
    if "改❌" in full or "应由⏳改❌" in full:
        out = apply_status_on_line(out, "not_provided")
        out = out.replace("⏳", "❌")
    else:
        out = apply_status_on_line(out, "confirmed")
        out = out.replace("⏳", "✅")
    if "行需由 2 改 4" in full or "L450C20 CW320 规格" in full:
        out = re.sub(r"2×\s*CRS 320 CW", "4× CRS 320 CW", out)
        out = re.sub(r"L450C20\s*×\s*2", "L450C20 × 4", out)
        out = out.replace("user-supplied, 非厂家选型书", "PRD v2.0 2026-09-08 选型书")
        out = out.replace("**单台热工/水力/外形参数待厂家**, 预期 2026-08-31", "单台规格 ✅ PRD v2.0（净 29.1 kW / 风机 4.5 kW）")
        out = out.replace("单台规格待厂家, 预期 2026-08-31", "单台规格 ✅ PRD v2.0 2026-09-08")
        out = out.replace("待厂家, 预期 2026-08-31", "✅ PRD v2.0 2026-09-08")
        out = out.replace("预期 2026-08-31", "选型书 2026-09-08")
    if "CW330 占位" in full:
        out = out.replace("[[PRD-STULZ-CW330]]", "[[PRD-STULZ-CW320]]")
        out = out.replace(
            "**占位条目**: 全部规格参数未到, 厂家预期 2026-08-31(周一)提供; 归属 SKU 亦 ✅ 待定(倾向 L450C20, 依据见该 PRD §1)。§3.1.2 / §3.2 / §3.4 三处入表并统一标 ✅ `` —— **参数到位前不得入 BOM 或方案**",
            "CW320 参数已固化（PRD v2.0 / 2026-09-08 选型书，净 29.1 kW / 风机 4.5 kW；归属 L1800C45 × 6 + L450C20 × 4，已入 BOM）",
        )
        out = out.replace("占位条目", "参数已固化")
        out = out.replace("全部规格参数未到", "PRD v2.0 已固化")
        out = out.replace("厂家预期 2026-08-31(周一)提供", "选型书 2026-09-08")
        out = out.replace("参数到位前不得入 BOM 或方案", "已入 BOM")
        out = out.replace("2026-08-31", "2026-09-08")
    if "L450C20 末端构成" in full:
        out = out.replace(
            "✅ —— 等 L450C20 DESIGN，预期 TBD",
            "**冷板 + 4× CRS 320 CW** ✅ 站点 profile / PRD v2.0",
        )
        out = out.replace("等 L450C20 DESIGN，预期 TBD", "**4× CRS 320 CW** ✅")
        out = re.sub(r"CRS 320 CW × 2（N\+1）", "CRS 320 CW × 4", out)
        out = out.replace("CRS 320 CW × 2", "CRS 320 CW × 4")
        out = out.replace("规格参数待厂家提供（预期 2026-08-31）", "规格 ✅ PRD v2.0 2026-09-08")
    if "L450C20 台数改 4" in full or "CW320 单台规格" in full:
        out = re.sub(r"L450C20\s*×\s*2(?:\s*\(N\+1\))?", "L450C20 × 4", out)
        out = out.replace(
            "单台规格待厂家选型书，预期 2026-08-31，**到位前不得入 BOM**",
            "单台规格 ✅ PRD v2.0 2026-09-08（净 29.1 kW / 风机 4.5 kW，已入 BOM）",
        )
        out = out.replace("到位前不得入 BOM", "已入 BOM")
        out = out.replace("预期 2026-08-31", "选型书 2026-09-08")
    if "版本行需更新" in full or "CW320 参数/归属" in full:
        out = out.replace(
            "新增 STULZ CW320 占位条目，✅ 参数未到、归属 SKU 待定，厂家预期 2026-08-31 提供",
            "STULZ CW320 参数已固化（PRD v2.0 / 2026-09-08 选型书，净 29.1 kW / 风机 4.5 kW；归属 L1800C45 × 6 + L450C20 × 4）",
        )
        out = out.replace("参数未到、归属 SKU 待定", "参数已固化、归属已定")
        out = out.replace("厂家预期 2026-08-31 提供", "选型书 2026-09-08")
        out = out.replace("参数未到", "参数已固化")
    if "ulCompliant:false" in full or ("I400C40 UL" in full and "❌不提供" in full):
        out = out.replace("❌ ⛔", "❌")
        out = re.sub(r"(>\s*)⛔\s*", r"\1", out)
        out = out.replace(
            "I400C40 的 UL 状态未定义（站点该格为空白）",
            "I400C40 UL ❌不提供（站点 ac40.json ulCompliant:false）",
        )
        out = out.replace("UL 状态未定义", "UL ❌不提供")
        if "⛔" in out and "conflict" not in out.lower():
            out = out.replace("⛔ ", "").replace(" ⛔", "")
    if "29.1" in full or "34.3" in full:
        out = out.replace("34.3 kW", "29.1 kW")
        out = re.sub(r"(?<![\d.])34\.3(?![\d.])", "29.1", out)
        out = re.sub(r"L450C20\*\*\s*×\s*2(?:\(N\+1\))?", "L450C20** × 4", out)
        out = re.sub(r"L450C20\s*×\s*2(?:\(N\+1\))?", "L450C20 × 4", out)
        out = out.replace("厂家选型书预期 2026-08-31", "选型书 2026-09-08")
        out = out.replace("单台规格待厂家(2026-08-31)", "单台规格 ✅ PRD v2.0 2026-09-08")
        out = out.replace("待厂家(2026-08-31)", "✅ 2026-09-08 选型书")
    if "4.5 kW" in full:
        out = out.replace("1.49 kW", "4.5 kW")
    return out


def _insert_changelog_row(text: str, row: str) -> str:
    """Insert a Changelog table row under ## Changelog only — never the first spec table."""
    m = CHANGELOG_HEAD_RE.search(text)
    if m and row in text[m.start() :]:
        return text
    if not m:
        return (
            text.rstrip()
            + "\n\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n"
            + row
            + "\n"
        )
    rest = text[m.end() :]
    sep = re.search(r"\n(\|[-: ]+\|[-: ]+\|[-: |]*\n)", rest)
    if sep:
        at = m.end() + sep.end()
        return text[:at] + row + "\n" + text[at:]
    return text[: m.end()] + "\n\n| 日期 | 变更 |\n|---|---|\n" + row + "\n" + rest


def _append_changelog(text: str, item_id: str, note: str, today: str) -> str:
    row = f"| {today} | 🧭 {item_id} {note} |"
    return _insert_changelog_row(text, row)


def relocate_stray_changelog_rows(text: str) -> str:
    """Move `| date | 🧭 item |` rows that landed in spec tables into ## Changelog."""
    m = CHANGELOG_HEAD_RE.search(text)
    cut = m.start() if m else len(text)
    before, after = text[:cut], text[cut:]
    kept: list[str] = []
    stray: list[str] = []
    for ln in before.splitlines(keepends=True):
        core = ln.rstrip("\r\n")
        if STRAY_ROW_RE.match(core):
            stray.append(core)
        else:
            kept.append(ln)
    if not stray:
        return text
    rebuilt = "".join(kept) + after
    for row in stray:
        rebuilt = _insert_changelog_row(rebuilt, row)
    return rebuilt


def dedupe_changelog_compass(text: str) -> str:
    """Keep the first 🧭 unconfirmed-N Changelog row; drop later duplicates."""
    m = CHANGELOG_HEAD_RE.search(text)
    if not m:
        return text
    head, rest = text[: m.end()], text[m.end() :]
    seen: set[str] = set()
    kept: list[str] = []
    for ln in rest.splitlines(keepends=True):
        mm = re.search(r"🧭 (unconfirmed-\d+|ghost-\d+)", ln)
        if mm:
            key = mm.group(1)
            if key in seen:
                continue
            seen.add(key)
        kept.append(ln)
    return head + "".join(kept)


def repair_stray_changelogs(root: Path) -> list[str]:
    touched: list[str] = []
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        original = path.read_text(encoding="utf-8", errors="replace")
        if "🧭 unconfirmed-" not in original and "🧭 ghost-" not in original:
            continue
        updated = relocate_stray_changelog_rows(original)
        updated = dedupe_changelog_compass(updated)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            touched.append(path.relative_to(root).as_posix())
    return touched


def _block_id(blob: str) -> str | None:
    if "#^" in blob:
        return blob.split("#^", 1)[1].strip().rstrip("]")
    if blob.startswith("^"):
        return blob[1:]
    return None


def _line_has_block(line: str, block: str) -> bool:
    return bool(re.search(rf"\^{re.escape(block)}\s*$", line)) or f"^{block}" in line


def _edit_file(text: str, ruling: Ruling, blobs: list[str], status: str) -> tuple[str, bool]:
    lines = text.splitlines(keepends=True)
    changed = False
    blocks = {_block_id(b) for b in blobs if _block_id(b)}
    if not blocks:
        return text, False
    for i, line in enumerate(lines):
        hit = any(_line_has_block(line, b) for b in blocks if b)
        if not hit:
            continue
        if status == "conflict":
            new = apply_status_on_line(line, "conflict")
        else:
            new = apply_source_value(line, ruling)
        if new != line:
            lines[i] = new
            changed = True
    return "".join(lines), changed


def _paths_from_text(text: str) -> list[str]:
    return [m.group(0).strip() for m in PATH_IN_TEXT_RE.finditer(text or "")]


def _anchors_from_text(text: str) -> list[str]:
    return [m.group(1) for m in ANCHOR_RE.finditer(text or "")]


def _targets(ruling: Ruling) -> list[tuple[str, list[str]]]:
    known = CLOSE_TARGETS.get(ruling.item_id) or CONFLICT_TARGETS.get(ruling.item_id)
    files = list(ruling.files)
    raw_blobs = [b for b in ruling.blobs if b and b != "no blob"]
    if known:
        files = list(dict.fromkeys(files + known["files"]))
        raw_blobs = list(dict.fromkeys(raw_blobs + known["blobs"]))
    extra_files = CLOSE_FILES.get(ruling.item_id, [])
    files = list(dict.fromkeys(files + extra_files + _paths_from_text(ruling.ruling_full)))
    blobs = [b for b in raw_blobs if "#^" in b]
    pathless = []
    for b in raw_blobs:
        if "#^" in b:
            continue
        if b.startswith("^"):
            pathless.append(b[1:])
        elif re.match(r"(?:mdc-|sec-|baseline-)", b):
            pathless.append(b)
    if ruling.action == "conflict" and not blobs:
        for anc in _anchors_from_text(ruling.ruling_full):
            if anc not in pathless:
                pathless.append(anc)
    by_file: dict[str, list[str]] = {}
    for blob in blobs:
        rel = blob.split("#^", 1)[0]
        if not rel.endswith(".md"):
            rel = f"{rel}.md"
        by_file.setdefault(rel, []).append(blob)
    for f in files:
        by_file.setdefault(f, [])
        for anc in pathless:
            blob = f"{f}#^{anc}"
            if blob not in by_file[f]:
                by_file[f].append(blob)
    return list(by_file.items())


def apply_rulings(
    root: Path,
    checklist_text: str = "",
    rulings: list[Ruling] | None = None,
) -> ApplyReport:
    today = date.today().isoformat()
    report = ApplyReport()
    if rulings is None:
        rulings = parse_checklist(checklist_text)
    for ruling in rulings:
        action = ruling.action
        if action == "drop":
            report.dropped.append(ruling.item_id)
            continue
        if action == "ghost_fix":
            report.ghosts.append(ruling.item_id)
            continue
        if action in {"keep", "suppress_mismatch"}:
            continue
        status = "conflict" if action == "conflict" else "confirmed"
        if "改❌" in ruling.ruling_full or "应由⏳改❌" in ruling.ruling_full:
            status = "not_provided"
        note = (
            "改为 ⛔ conflict，未裁定赢家"
            if action == "conflict"
            else f"已可关闭，已回写来源值（{ruling.ruling}）"
        )
        touched = False
        for rel, blobs in _targets(ruling):
            path = root / rel
            if not path.is_file():
                report.skipped.append(f"{ruling.item_id}:{rel}:missing")
                continue
            original = path.read_text(encoding="utf-8", errors="replace")
            updated, did = _edit_file(original, ruling, blobs, status)
            if did:
                updated = _append_changelog(updated, ruling.item_id, note, today)
            relocated = relocate_stray_changelog_rows(updated)
            if relocated != original:
                path.write_text(relocated, encoding="utf-8")
                touched = True
                if rel not in report.files_touched:
                    report.files_touched.append(rel)
        if action == "conflict":
            report.conflicted.append(ruling.item_id)
        else:
            report.closed.append(ruling.item_id)
        if not touched:
            report.skipped.append(ruling.item_id)
    for rel in repair_stray_changelogs(root):
        if rel not in report.files_touched:
            report.files_touched.append(rel)
    return report
