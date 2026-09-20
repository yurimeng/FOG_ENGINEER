from __future__ import annotations

from pathlib import Path

from mdc_kb_reorg.apply_rulings import apply_rulings, apply_source_value, apply_status_on_line
from mdc_kb_reorg.claims import extract_claims
from mdc_kb_reorg.review_state import attach_ruling, parse_checklist, should_suppress_mismatch


def test_conflict_marks_heading_without_hourglass() -> None:
    from mdc_kb_reorg.apply_rulings import apply_status_on_line

    heading = "## 12. Service & Support ^sec-12-service"
    marked = apply_status_on_line(heading, "conflict")
    assert "⛔ **conflict**" in marked
    assert "^sec-12-service" in marked
    assert apply_status_on_line(marked, "conflict") == marked


def test_apply_status_close_and_conflict_are_idempotent() -> None:
    line = "IT 容量 100 kW ⏳ #unconfirmed —— 等 DESIGN ^mdc-aa\n"
    closed = apply_status_on_line(line, "confirmed")
    assert "⏳" not in closed
    assert "✅" in closed
    assert apply_status_on_line(closed, "confirmed") == closed
    conflicted = apply_status_on_line(line, "conflict")
    assert "⛔" in conflicted
    assert "#unconfirmed" not in conflicted or "conflict" in conflicted


def test_checklist_wraps_bare_block_ids_as_code() -> None:
    from mdc_kb_reorg.checklist import items_from_rulings, render_checklist
    from mdc_kb_reorg.review_state import parse_checklist

    text = """
- [ ] **unconfirmed-178** term
  - 🧭 **建议裁定：已可关闭**（末端）— PRD-STULZ-CW320 §3 ^mdc-fe6a35fbe5
  - 文件: `KB/_COMMON/PRODUCT_SPEC_BASELINE.md`
  - blob: ^mdc-fe6a35fbe5
"""
    body = render_checklist(items_from_rulings(parse_checklist(text)), generated="2026-09-20")
    # Trailing bare ^id would be an Obsidian block definition.
    for ln in body.splitlines():
        if ln.strip().endswith("^mdc-fe6a35fbe5"):
            raise AssertionError(f"bare block id at EOL: {ln}")
    assert "`^mdc-fe6a35fbe5`" in body


def test_items_from_rulings_preserve_compass_and_ids() -> None:
    from mdc_kb_reorg.checklist import items_from_rulings, render_checklist
    from mdc_kb_reorg.review_state import parse_checklist

    text = """
- [ ] **unconfirmed-002** layout
  - 🧭 **建议裁定：仍待确认**（浸没槽排布方式）— 等 DESIGN
  - 文件: `PUBLIC/I200.md`
  - blob: [[PUBLIC/I200#^mdc-838f17b721]]
"""
    items = items_from_rulings(parse_checklist(text))
    body = render_checklist(items, generated="2026-09-20")
    assert "浸没槽排布方式" in body
    assert "等外部交付物" not in body
    assert "mdc-838f17b721" in body
    assert "- [ ]" in body
    assert "- [x]" not in body


def test_parse_compass_actions(tmp_path: Path) -> None:
    text = """
- [ ] **ghost-001** 幽灵
  - 🧭 **建议裁定：是，固定**（Solutions Design/）— 收口注释
  - 文件: `index.md`
  - blob: no blob
- [ ] **mismatch-005** kW 冲突
  - 🧭 **建议裁定：不是同一指标**（I200C20 容量）— 200 vs 50
  - 文件: `KB/a.md`
- [ ] **unconfirmed-017** changelog
  - 🧭 **建议裁定：已可关闭**（Changelog V1.5 行）— 历史文字；建议从清单剔除
  - 文件: `PUBLIC/x.md`
- [ ] **unconfirmed-021** flow
  - 🧭 **建议裁定：改为 conflict**（二次侧流量）— 两套值
  - 文件: `PUBLIC/y.md`
- [ ] **unconfirmed-014** air
  - 🧭 **建议裁定：已可关闭**（风冷柜）— 基准表已 ✅
  - 文件: `PUBLIC/z.md`
"""
    rulings = parse_checklist(text)
    by_id = {r.item_id: r for r in rulings}
    assert by_id["ghost-001"].action == "ghost_fix"
    assert should_suppress_mismatch(by_id["mismatch-005"])
    assert by_id["unconfirmed-017"].action == "drop"
    assert by_id["unconfirmed-021"].action == "conflict"
    assert by_id["unconfirmed-014"].action == "close"


def test_close_copies_source_value_not_waiting_tbd(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "PUBLIC" / "Tech_Spec" / "X.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        "| Item | Parameter | Confidence |\n"
        "|---|---|---|\n"
        "| Rack quantity | ⏳ #unconfirmed — waiting on DESIGN/, expected TBD | ⏳ | ^mdc-rack\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-900** rack\n"
        "  - 🧭 **建议裁定：已可关闭**（L1800 机柜数量(EN)）— "
        "KB/_COMMON/PRODUCT_SPEC_BASELINE.md §1.1 = 9 柜；EN §4 漏改\n"
        "  - 文件: `PUBLIC/Tech_Spec/X.md`\n"
        "  - blob: [[PUBLIC/Tech_Spec/X#^mdc-rack]]\n"
    )
    report = apply_rulings(vault, checklist)
    assert "unconfirmed-900" in report.closed
    row = next(ln for ln in target.read_text(encoding="utf-8").splitlines() if "mdc-rack" in ln)
    assert "✅" in row
    assert "9" in row
    assert "waiting" not in row.lower()
    assert "TBD" not in row
    assert "⏳" not in row


def test_air_close_does_not_touch_sibling_switch_row(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "PUBLIC" / "Tech_Spec" / "I200.md"
    target.parent.mkdir(parents=True)
    switch = (
        "| Switch mounting location | ⏳ **#unconfirmed** | "
        "Waiting on the site side or I200C20 DESIGN/ to state the switch mounting location; expected TBD |"
    )
    target.write_text(
        "| Loop | Role | Confidence |\n"
        "|---|---|---|\n"
        "| Air branch | ⏳ #unconfirmed — lists no air-cooled rack; waiting on DESIGN/, expected TBD | ⏳ | ^mdc-air\n"
        f"{switch}\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-901** air\n"
        "  - 🧭 **建议裁定：已可关闭**（I200C20 air rack）— "
        "基准表 §2.1 4× I50TS + 1× **5 kW** 风冷柜；Air branch\n"
        "  - 文件: `PUBLIC/Tech_Spec/I200.md`\n"
        "  - blob: [[PUBLIC/Tech_Spec/I200#^mdc-air]]\n"
    )
    apply_rulings(vault, checklist)
    text = target.read_text(encoding="utf-8")
    air = next(ln for ln in text.splitlines() if "mdc-air" in ln)
    sw = next(ln for ln in text.splitlines() if "Switch mounting" in ln)
    assert "5 kW" in air and "waiting" not in air.lower() and "TBD" not in air
    assert "⏳" in sw
    assert "#unconfirmed" in sw
    assert "5 kW" not in sw
    assert "air-cooled rack" not in sw
    assert "Waiting on the site side or I200C20 DESIGN/" in sw


def test_cn_section2_note_rewrites_to_clean_baseline(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "PUBLIC" / "Tech_Spec" / "I200CN.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        "> ⚠️ **注意：I400C45 / I400C40 各含 1 台 10 kW 风冷机柜，"
        "[[PRODUCT_SPEC_BASELINE]] 的 I200C20 一列未列出风冷机柜。** "
        "本文档因此不写风冷机柜。I200C20 是否配置风冷柜 ⏳ #unconfirmed —— 等 DESIGN，预期 TBD。 "
        "^mdc-note\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-902** air cn\n"
        "  - 🧭 **建议裁定：已可关闭**（I200C20 风冷柜）— "
        "基准表 §2.1 4× I50TS + 1× **5 kW** 风冷柜\n"
        "  - 文件: `PUBLIC/Tech_Spec/I200CN.md`\n"
        "  - blob: [[PUBLIC/Tech_Spec/I200CN#^mdc-note]]\n"
    )
    apply_rulings(vault, checklist)
    note = next(
        ln for ln in target.read_text(encoding="utf-8").splitlines() if "mdc-note" in ln
    )
    assert "是否配置风冷柜" not in note
    assert "未列出" not in note
    assert "因此不写" not in note
    assert "预期 TBD" not in note
    assert "4× I50TS + 1× 5 kW" in note
    assert "按基准表" in note


def test_changelog_inserts_under_changelog_not_spec_table(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "PUBLIC" / "Tech_Spec" / "X.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        "| Drawing | Status |\n"
        "|---|---|\n"
        "| TOP view | ⏳ #unconfirmed waiting TBD | ^mdc-flow\n"
        "\n## Changelog\n\n| Date | Change |\n|---|---|\n| older | x |\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-921** flow\n"
        "  - 🧭 **建议裁定：改为 conflict**（二次侧流量）— 两套值\n"
        "  - 文件: `PUBLIC/Tech_Spec/X.md`\n"
        "  - blob: [[PUBLIC/Tech_Spec/X#^mdc-flow]]\n"
    )
    from mdc_kb_reorg.apply_rulings import apply_rulings

    apply_rulings(vault, checklist)
    text = target.read_text(encoding="utf-8")
    spec, _, log = text.partition("## Changelog")
    assert "🧭 unconfirmed-921" not in spec
    assert "🧭 unconfirmed-921" in log
    row = next(ln for ln in text.splitlines() if "mdc-flow" in ln)
    assert "⛔" in row
    assert "TOP view" in row


def test_relocate_stray_changelog_out_of_spec_table() -> None:
    from mdc_kb_reorg.apply_rulings import relocate_stray_changelog_rows

    text = (
        "| Drawing | Status |\n|---|---|\n"
        "| 2026-09-20 | 🧭 unconfirmed-170 改为 ⛔ conflict，未裁定赢家 |\n"
        "| TOP | ⏳ |\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n"
    )
    out = relocate_stray_changelog_rows(text)
    spec, _, log = out.partition("## Changelog")
    assert "unconfirmed-170" not in spec
    assert "unconfirmed-170" in log
    assert "| TOP | ⏳ |" in spec


def test_conflict_recovers_path_from_ruling_full(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "PUBLIC" / "y.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        "| flow | 87.8 m³/h ⏳ #unconfirmed waiting TBD | ^mdc-ab12\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-922** flow\n"
        "  - 🧭 **建议裁定：改为 conflict**（二次侧流量）— "
        "PUBLIC/y.md ^mdc-ab12 vs 基准表 88–96\n"
    )
    from mdc_kb_reorg.apply_rulings import apply_rulings

    apply_rulings(vault, checklist)
    text = target.read_text(encoding="utf-8")
    row = next(ln for ln in text.splitlines() if "mdc-ab12" in ln)
    assert "⛔" in row
    spec, _, log = text.partition("## Changelog")
    assert "🧭 unconfirmed-922" not in spec
    assert "🧭 unconfirmed-922" in log


def test_patch_readme_adds_domains_pointer() -> None:
    from mdc_kb_reorg.navigation import patch_readme_text

    out = patch_readme_text("# Engineer Workspace\n\nhello\n")
    assert "[[_domains/index]]" in out
    assert "[[_domains/采购询价]]" in out
    assert "幽灵路径" not in out


def test_close_174_cooling_zone_copies_4x_prd(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "KB/3RD-PARTY/_blocks/3rd_Party_List/02_Cooling_Zone.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        "> - **L450C20(IT 450kW · 双环路)**→ 列间侧 **2× CRS 320 CW**(N+1)。"
        "✅ CRS 320 CW 单台规格待厂家, 预期 2026-08-31。 ^mdc-65d4483355\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-174** cw\n"
        "  - 🧭 **建议裁定：已可关闭**（L450C20 CW320 规格）— 单台规格 PRD-STULZ-CW320.md v2.0 §2"
        "（2026-09-08）；台数已改 4×，行需由 2 改 4\n"
        "  - 文件: `KB/3RD-PARTY/_blocks/3rd_Party_List/02_Cooling_Zone.md`\n"
        "  - blob: [[KB/3RD-PARTY/_blocks/3rd_Party_List/02_Cooling_Zone#^mdc-65d4483355]]\n"
    )
    apply_rulings(vault, checklist)
    row = next(ln for ln in target.read_text(encoding="utf-8").splitlines() if "mdc-65d4483355" in ln)
    assert "4× CRS 320" in row or "L450C20 × 4" in row
    assert "2× CRS 320" not in row
    assert "2026-08-31" not in row
    assert "待厂家" not in row


def test_close_175_changelog_placeholder_rewritten(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "KB/3RD-PARTY/_blocks/3rd_Party_List/05_Changelog.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        "| 2026-08-30 | V2.1 | 新增 [[PRD-STULZ-CW330]] **占位条目**: 全部规格参数未到, "
        "厂家预期 2026-08-31(周一)提供; **参数到位前不得入 BOM 或方案**。 | ^mdc-473ef8fc22\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-175** cl\n"
        "  - 🧭 **建议裁定：已可关闭**（CW330 占位（changelog））— PRD-STULZ-CW320.md v2.0 "
        "Changelog 2026-09-08；参数与归属均到位\n"
        "  - 文件: `KB/3RD-PARTY/_blocks/3rd_Party_List/05_Changelog.md`\n"
        "  - blob: [[KB/3RD-PARTY/_blocks/3rd_Party_List/05_Changelog#^mdc-473ef8fc22]]\n"
    )
    apply_rulings(vault, checklist)
    row = next(ln for ln in target.read_text(encoding="utf-8").splitlines() if "mdc-473ef8fc22" in ln)
    assert "占位条目" not in row
    assert "参数未到" not in row
    assert "2026-08-31" not in row
    assert "不得入 BOM" not in row
    assert "PRD v2.0" in row or "2026-09-08" in row


def test_dedupe_changelog_compass_keeps_first() -> None:
    from mdc_kb_reorg.apply_rulings import dedupe_changelog_compass

    text = (
        "## Changelog\n\n| 日期 | 变更 |\n|---|---|\n"
        "| 2026-09-20 | 🧭 unconfirmed-014 已可关闭 |\n"
        "| 2026-09-20 | 🧭 unconfirmed-014 已可关闭，已回写来源值 |\n"
        "| 2026-09-20 | 🧭 unconfirmed-053 已可关闭 |\n"
    )
    out = dedupe_changelog_compass(text)
    assert out.count("unconfirmed-014") == 1
    assert out.count("unconfirmed-053") == 1


def test_close_does_not_rewrite_historical_10_16() -> None:
    from mdc_kb_reorg.apply_rulings import apply_source_value
    from mdc_kb_reorg.review_state import Ruling

    line = "站点 `CLAIMS.md` C33 已由 10/16 改 **10/15**，六个产品页已重出。 ^mdc-hist\n"
    ruling = Ruling(
        item_id="unconfirmed-219",
        kind="unconfirmed",
        question="",
        ruling="已可关闭",
        ruling_full="🧭 **建议裁定：已可关闭**（CW320）— 净 29.1 kW / 风机 4.5 kW",
        files=[],
        blobs=[],
    )
    out = apply_source_value(line, ruling)
    assert "10/16" in out
    assert "已由 10/16 改 **10/15**" in out


def test_close_178_terminal_composition_from_baseline(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "KB/_COMMON/PRODUCT_SPEC_BASELINE.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        "| 末端构成 | 冷板 + 9× RDHX | 冷板 + CyberRow | "
        "✅ —— 等 L450C20 DESIGN，预期 TBD | ✅ / ✅ / ⏳ | ^mdc-311342bcd7\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-178** term\n"
        "  - 🧭 **建议裁定：已可关闭**（L450C20 末端构成）— "
        "KB/_COMMON/PRODUCT_SPEC_BASELINE.md L98（1× SCR 14103 W + 4× CRS 320 CW）\n"
        "  - 文件: `KB/_COMMON/PRODUCT_SPEC_BASELINE.md`\n"
        "  - blob: [[KB/_COMMON/PRODUCT_SPEC_BASELINE#^mdc-311342bcd7]]\n"
    )
    apply_rulings(vault, checklist)
    row = next(ln for ln in target.read_text(encoding="utf-8").splitlines() if "mdc-311342bcd7" in ln)
    assert "等 L450C20 DESIGN" not in row
    assert "预期 TBD" not in row
    assert "4× CRS 320" in row
    assert "⏳" not in row


def test_enrich_keep_matches_slash_spacing(tmp_path: Path) -> None:
    from mdc_kb_reorg.review_state import Ruling, enrich_keep_targets

    vault = tmp_path / "vault"
    spec = vault / "PUBLIC/Tech_Spec/I200C20_Tech_Spec_CN.md"
    spec.parent.mkdir(parents=True)
    spec.write_text(
        "| 布局图纸 / SVG | ⏳ **#unconfirmed** | 等出图 | ^mdc-layout |\n"
        "| 功率因数（UPS 输出侧） | ⏳ **#unconfirmed** | 等计算书 | ^mdc-pf |\n",
        encoding="utf-8",
    )
    rulings = [
        Ruling(
            item_id="unconfirmed-004",
            kind="unconfirmed",
            question="",
            ruling="仍待确认",
            ruling_full="🧭 **建议裁定：仍待确认**（布局图纸/SVG）— 等出图",
            files=[],
            blobs=[],
        ),
        Ruling(
            item_id="unconfirmed-006",
            kind="unconfirmed",
            question="",
            ruling="仍待确认",
            ruling_full="🧭 **建议裁定：仍待确认**（功率因数 UPS 出）— 等计算书",
            files=[],
            blobs=[],
        ),
    ]
    enrich_keep_targets(vault, rulings)
    assert "mdc-layout" in "".join(rulings[0].blobs)
    assert "I200C20_Tech_Spec_CN.md" in rulings[0].files[0]
    assert "mdc-pf" in "".join(rulings[1].blobs)


def test_attach_ruling_matches_blob_not_sibling_file() -> None:
    text = """
- [ ] **unconfirmed-005** gpu
  - 🧭 **建议裁定：改为 conflict**（GPU 数上限）— 两套值
  - 文件: `PUBLIC/I200.md`
  - blob: [[PUBLIC/I200#^mdc-gpu]]
- [ ] **unconfirmed-002** layout
  - 🧭 **建议裁定：仍待确认**（浸没槽排布方式）— 等 DESIGN
  - 文件: `PUBLIC/I200.md`
  - blob: [[PUBLIC/I200#^mdc-838f17b721]]
"""
    rulings = parse_checklist(text)
    hit = attach_ruling(
        "I200C20 浸没槽排布",
        ["PUBLIC/I200.md"],
        ["PUBLIC/I200#^mdc-838f17b721"],
        rulings,
    )
    assert hit is not None
    assert hit.action == "keep"
    assert "浸没槽排布" in hit.ruling_full
    gpu = attach_ruling("gpu", ["PUBLIC/I200.md"], ["PUBLIC/I200#^mdc-gpu"], rulings)
    assert gpu is not None and gpu.action == "conflict"
    none = attach_ruling("other ⏳", ["PUBLIC/I200.md"], ["PUBLIC/I200#^mdc-other"], rulings)
    assert none is None


def test_close_127_copies_cw320_prd_not_waiting(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "KB/3RD-PARTY/_blocks/STD_Supplier/02_Supplier_Table_Cooling_Power.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        "| 14 | **CyberRow CW 列间空调 10/15 °C（L1800C45 × 6 + L450C20 × 2）** | "
        "[[PRD-STULZ-CW320]] | STULZ | "
        "✅ **归属与台数已定** (2026-08-30) · ✅ 单台规格待厂家选型书，预期 2026-08-31，**到位前不得入 BOM** | "
        "^mdc-71067ab178\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-127** cw320\n"
        "  - 🧭 **建议裁定：已可关闭**（CW320 单台规格）— PRD-STULZ-CW320.md v2.0 §2"
        "（2026-09-08 选型书）；已入 BOM；L450C20 台数改 4\n"
        "  - 文件: `KB/3RD-PARTY/_blocks/STD_Supplier/02_Supplier_Table_Cooling_Power.md`\n"
        "  - blob: [[KB/3RD-PARTY/_blocks/STD_Supplier/02_Supplier_Table_Cooling_Power#^mdc-71067ab178]]\n"
    )
    apply_rulings(vault, checklist)
    row = next(ln for ln in target.read_text(encoding="utf-8").splitlines() if "mdc-71067ab178" in ln)
    assert "L450C20 × 4" in row
    assert "L450C20 × 2" not in row
    assert "2026-08-31" not in row
    assert "不得入 BOM" not in row
    assert "29.1" in row and "4.5" in row
    assert "已入 BOM" in row


def test_close_121_rewrites_cw320_placeholder_version_line(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "KB/3RD-PARTY/3rd Party List.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        "版本：V2.1（2026-08-30 新增 L1800C45 两项 ATS approved 机型；"
        "新增 STULZ CW320 占位条目，✅ 参数未到、归属 SKU 待定，厂家预期 2026-08-31 提供；"
        "同批修复链接。） ^mdc-7352fb76ea\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-121** ver\n"
        "  - 🧭 **建议裁定：已可关闭**（CW320 参数/归属）— PRD-STULZ-CW320.md v2.0 "
        "Changelog（2026-09-08 StulzSelect 选型书）；版本行需更新\n"
        "  - 文件: `KB/3RD-PARTY/3rd Party List.md`\n"
        "  - blob: [[KB/3RD-PARTY/3rd Party List#^mdc-7352fb76ea]]\n"
    )
    apply_rulings(vault, checklist)
    line = next(ln for ln in target.read_text(encoding="utf-8").splitlines() if "mdc-7352fb76ea" in ln)
    assert "参数未到" not in line
    assert "2026-08-31" not in line
    assert "待定" not in line
    assert "PRD v2.0" in line or "2026-09-08" in line
    spec, _, log = target.read_text(encoding="utf-8").partition("## Changelog")
    assert "🧭 unconfirmed-121" not in spec
    assert "🧭 unconfirmed-121" in log


def test_close_016_ul_is_not_provided_only(tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    target = vault / "KB/_COMMON/PRODUCTS_MDC.md"
    target.parent.mkdir(parents=True)
    target.write_text(
        "| **I400C40** | `I400C40ST50` | AC40 | 40ft | 400kW | 浸没式 | 外置 | 10min | ❌ ⛔ | ^mdc-53377e92cf\n"
        "> ⛔ I400C40 的 UL 状态未定义（站点该格为空白），见基准表。 ^mdc-a4c1845fae\n"
        "\n## Changelog\n\n| 日期 | 变更 |\n|---|---|\n",
        encoding="utf-8",
    )
    checklist = (
        "- [ ] **unconfirmed-016** ul\n"
        "  - 🧭 **建议裁定：已可关闭**（I400C40 UL）— KB/_COMMON/PRODUCT_SPEC_BASELINE.md L268"
        "「UL 合规 ❌不提供（站点 ac40.json ulCompliant:false）✅站点 Designer」；行应由⏳改❌\n"
        "  - 文件: `KB/_COMMON/PRODUCTS_MDC.md`\n"
        "  - blob: [[KB/_COMMON/PRODUCTS_MDC#^mdc-53377e92cf]]\n"
        "  - blob: [[KB/_COMMON/PRODUCTS_MDC#^mdc-a4c1845fae]]\n"
    )
    apply_rulings(vault, checklist)
    text = target.read_text(encoding="utf-8")
    cell = next(ln for ln in text.splitlines() if "mdc-53377e92cf" in ln)
    note = next(ln for ln in text.splitlines() if "mdc-a4c1845fae" in ln)
    assert "❌" in cell
    assert "⛔" not in cell
    assert "未定义" not in note
    assert "⛔" not in note
    assert "ulCompliant:false" in note or "不提供" in note


def test_it_pair_still_links_after_filter(fixture_vault: Path) -> None:
    from mdc_kb_reorg.claims import apply_block_ids
    from mdc_kb_reorg.match import match_claims

    aliases = {"X100TEST": "X100TEST"}
    spec = (fixture_vault / "KB/X100TEST_spec.md").read_text(encoding="utf-8")
    ra = (fixture_vault / "Reference Architecture/X100TEST_ra.md").read_text(encoding="utf-8")
    a = extract_claims(spec, "KB/X100TEST_spec.md", "product", aliases)
    b = extract_claims(ra, "Reference Architecture/X100TEST_ra.md", "solution", aliases)
    _, a, _ = apply_block_ids(spec, a)
    _, b, _ = apply_block_ids(ra, b)
    report = match_claims(a + b, client=None, max_typesafe=0)
    keys = {f.key for f in report.linked}
    assert ("sku_presence", "X100TEST") in keys
    it = [f for f in report.linked if f.key == ("sku_it_kw", "X100TEST")]
    assert it
    assert any("#^" in link or "^mdc-" in link for link in it[0].blob_links)
