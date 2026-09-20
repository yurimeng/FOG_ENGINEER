from __future__ import annotations

import os
from pathlib import Path

import pytest

from mdc_kb_reorg.inventory import OriginMap, assert_preserved, snapshot
from mdc_kb_reorg.reorg import run_reorg


def _checklist(root: Path) -> str:
    return (root / "_holding_unconfirmed" / "问题确认清单.md").read_text(encoding="utf-8")


def test_fixture_reorg_links_match_and_lists_conflict_unsourced(fixture_vault: Path) -> None:
    live = bool(os.environ.get("TYPESAFE_API_KEY", "").strip())
    before = snapshot(fixture_vault)
    before_rels = {r.relpath for r in before}
    report = run_reorg(
        fixture_vault,
        live_typesafe=live,
        max_typesafe=8,
        apply_moves=True,
        log_dir=None,
    )
    after = snapshot(fixture_vault)
    origin = OriginMap.load(fixture_vault / "_holding_unconfirmed" / "origin-map.json")
    missing = assert_preserved(before, after, origin)
    assert missing == []
    assert report.ok()
    # No fixture file deleted (paths may move).
    for rel in before_rels:
        current = origin.current_of(rel)
        assert (fixture_vault / current).is_file() or (fixture_vault / rel).is_file()

    hub = fixture_vault / "_domains" / "index.md"
    product = fixture_vault / "_domains" / "产品设计.md"
    solution = fixture_vault / "_domains" / "解决方案.md"
    project = fixture_vault / "_domains" / "项目.md"
    proc = fixture_vault / "_domains" / "采购询价.md"
    for path in (hub, product, solution, project, proc):
        assert path.is_file(), path
    product_txt = product.read_text(encoding="utf-8")
    assert "X100TEST" in product_txt
    assert "#^" in product_txt or "^mdc-" in product_txt
    # Matching pair cited at block level.
    assert "sku_presence:X100TEST" in product_txt or "X100TEST" in product_txt

    checklist = _checklist(fixture_vault)
    assert "250" in checklist or "不一致" in checklist or "冲突" in checklist
    assert "unsourced" in checklist or "77 kW" in checklist or "#unconfirmed" in checklist
    assert "Solutions Design" in checklist
    assert "SupplyChain" in checklist
    assert "no blob" in checklist
    # Concrete yes/no or choice question
    assert "选项：" in checklist
    idx = (fixture_vault / "index.md").read_text(encoding="utf-8")
    assert "_domains/解决方案" in idx
    assert "_domains/采购询价" in idx
    if live:
        assert report.typed_used is True
        assert report.typesafe_calls >= 1
        assert report.smoke.get("choice_kind")


def test_fixture_files_not_deleted_second_pass(fixture_vault: Path) -> None:
    live = bool(os.environ.get("TYPESAFE_API_KEY", "").strip())
    run_reorg(fixture_vault, live_typesafe=live, max_typesafe=4, apply_moves=True)
    before = snapshot(fixture_vault)
    report = run_reorg(fixture_vault, live_typesafe=False, max_typesafe=0, apply_moves=True)
    after = snapshot(fixture_vault)
    origin = OriginMap.load(fixture_vault / "_holding_unconfirmed" / "origin-map.json")
    assert assert_preserved(before, after, origin) == []
    assert report.ok()


def test_reorg_keep_compass_not_sibling_conflict(tmp_path: Path) -> None:
    from mdc_kb_reorg.review_state import Ruling, save_review

    vault = tmp_path / "vault"
    spec = vault / "KB" / "X100TEST_spec.md"
    spec.parent.mkdir(parents=True)
    spec.write_text(
        "X100TEST 单箱 IT 容量 100 kW。\n\n"
        "| GPU 数上限 | ⏳ #unconfirmed | TBD | ^mdc-gpu |\n"
        "| 浸没槽排布方式 | ⏳ #unconfirmed | 等 DESIGN | ^mdc-838f17b721 |\n",
        encoding="utf-8",
    )
    (vault / "index.md").write_text("# idx\n- KB/\n", encoding="utf-8")
    (vault / "_navigation.md").write_text("| 产品 KB |\n", encoding="utf-8")
    (vault / "README.md").write_text("# Engineer Workspace\n", encoding="utf-8")
    (vault / "Projects" / "a").mkdir(parents=True)
    (vault / "Projects" / "a" / "Project_Record.md").write_text("proj\n", encoding="utf-8")
    holding = vault / "_holding_unconfirmed"
    holding.mkdir()
    save_review(
        holding / "review-state.json",
        [
            Ruling(
                item_id="unconfirmed-005",
                kind="unconfirmed",
                question="GPU",
                ruling="改为 conflict",
                ruling_full="🧭 **建议裁定：改为 conflict**（GPU 数上限）— 两套值",
                files=["KB/X100TEST_spec.md"],
                blobs=["KB/X100TEST_spec#^mdc-gpu"],
            ),
            Ruling(
                item_id="unconfirmed-002",
                kind="unconfirmed",
                question="layout",
                ruling="仍待确认",
                ruling_full="🧭 **建议裁定：仍待确认**（浸没槽排布方式）— 等 DESIGN",
                files=["KB/X100TEST_spec.md"],
                blobs=["KB/X100TEST_spec#^mdc-838f17b721"],
            ),
        ],
    )
    report = run_reorg(vault, live_typesafe=False, max_typesafe=0, apply_moves=True)
    assert report.ok()
    cl = (holding / "问题确认清单.md").read_text(encoding="utf-8")
    open_part, _, appendix = cl.partition("## 已按🧭落地")
    assert "浸没槽排布方式" in open_part
    assert "仍待确认" in open_part
    layout_at = open_part.find("浸没槽排布方式")
    layout_block = open_part[layout_at : layout_at + 400]
    assert "改为 conflict" not in layout_block
    assert "unconfirmed-005" in cl
    assert "conflict" in appendix
