from __future__ import annotations

from mdc_kb_reorg.claims import extract_claims


ALIASES = {"X100TEST": "X100TEST", "X200TEST": "X200TEST"}


def _kw(claims, sku: str) -> list[str]:
    return [c.value for c in claims if c.kind == "sku_it_kw" and c.sku == sku]


def test_kw_binds_to_nearest_sku_not_every_sku() -> None:
    text = (
        "X100TEST 单箱 IT 容量 100 kW；X200TEST 单箱 IT 容量 450 kW。\n"
    )
    claims = extract_claims(text, "KB/multi.md", "product", ALIASES)
    assert _kw(claims, "X100TEST") == ["100"]
    assert _kw(claims, "X200TEST") == ["450"]
    assert "100" not in _kw(claims, "X200TEST")


def test_excluded_sku_does_not_inherit_other_load() -> None:
    text = "X100TEST 单箱 IT 100 kW。X200TEST 不在本文范围。\n"
    claims = extract_claims(text, "KB/scope.md", "product", ALIASES)
    assert _kw(claims, "X100TEST") == ["100"]
    assert _kw(claims, "X200TEST") == []


def test_non_it_kw_is_not_sku_it_capacity() -> None:
    text = (
        "X100TEST UPS 额定 600 kW。\n"
        "X100TEST 单柜 150 kW。\n"
        "X100TEST 单槽 50 kW。\n"
        "X100TEST CDU 容量 1500 kW。\n"
        "X100TEST 列间空调冷量 137 kW。\n"
        "项目合计 1600 kW（4×X100TEST）。\n"
        "X100TEST 单箱 IT 容量 100 kW。\n"
    )
    claims = extract_claims(text, "KB/spec.md", "product", ALIASES)
    assert _kw(claims, "X100TEST") == ["100"]


def test_dc45_in_l1800_procurement_is_not_l1240_it() -> None:
    text = "DC45 L1800 整箱 1800 kW，legacy 写法。\n"
    path = "KB/LIQUID/L1800C45/PROCUREMENT/RFI-BUS-001.md"
    claims = extract_claims(text, path, "procurement")
    it_skus = [c.sku for c in claims if c.kind == "sku_it_kw"]
    assert "L1240C45" not in it_skus
    presence = [c.sku for c in claims if c.kind == "sku_presence"]
    assert "L1800C45" in presence
    assert "L1240C45" not in presence
