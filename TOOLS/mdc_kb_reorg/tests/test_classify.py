from __future__ import annotations

from mdc_kb_reorg.classify import classify_path


def test_tools_fixtures_and_domain_indexes_are_not_procurement() -> None:
    assert (
        classify_path("TOOLS/mdc_kb_reorg/tests/fixtures/vault/Projects/alpha/RFI.md")
        == "other"
    )
    assert classify_path("_domains/采购询价.md") == "other"
    assert classify_path("_domains/产品设计.md") == "other"
    assert classify_path("_holding_unconfirmed/问题确认清单.md") == "other"


def test_real_rfi_and_procurement_still_classify() -> None:
    assert (
        classify_path("KB/LIQUID/L1800C45/PROCUREMENT/RFI-BUS-001_母线系统/RFI-BUS-001.md")
        == "procurement"
    )
    assert classify_path("Projects/alpha/RFI.md") == "procurement"
    assert classify_path("KB/LIQUID/L1800C45/PRODUCTS/spec.md") == "product"
