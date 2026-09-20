from __future__ import annotations

from mdc_kb_reorg.claims import Claim, apply_block_ids, extract_claims, repair_block_id_placement


ALIASES = {"X100TEST": "X100TEST"}


def _claim(line_no: int, relpath: str = "KB/spec.md") -> Claim:
    return Claim(
        kind="sku_presence",
        sku="X100TEST",
        value="X100TEST",
        raw="X100TEST",
        relpath=relpath,
        domain="product",
        line_no=line_no,
    )


def test_block_id_not_injected_on_table_row() -> None:
    text = "| Item | X100TEST 单箱 IT 容量 100 kW |\n"
    claims = extract_claims(text, "KB/spec.md", "product", ALIASES)
    out, _, changed = apply_block_ids(text, claims)
    line = out.splitlines()[0]
    assert line.count("|") == text.count("|")
    assert "^mdc-" not in line
    assert changed is False or "^mdc-" not in line


def test_block_id_not_injected_into_yaml_frontmatter() -> None:
    text = (
        "---\n"
        "sku_id: X100TEST\n"
        "title: X100TEST 单箱 IT 容量 100 kW\n"
        "---\n"
        "X100TEST 单箱 IT 容量 100 kW。\n"
    )
    claims = extract_claims(text, "KB/spec.md", "product", ALIASES)
    # Force a claim on the yaml title line if extractor skipped it.
    yaml_claim = _claim(2)
    out, _, _ = apply_block_ids(text, [yaml_claim] + claims)
    yaml = out.split("---")[1]
    assert "^mdc-" not in yaml
    body = out.split("---", 2)[-1]
    assert "^mdc-" in body


def test_repair_moves_id_off_pipe_and_strips_yaml() -> None:
    text = (
        "---\n"
        "sku_id: I200C20ST50 ^mdc-74639cf336\n"
        "---\n"
        "| Item | spec |\n"
        "|---|---|\n"
        "| Foo | bar | ^mdc-aaaa1111\n"
        "\nA paragraph. ^mdc-bbbb2222\n"
    )
    out, n = repair_block_id_placement(text)
    assert n >= 2
    yaml = out.split("---")[1]
    assert "^mdc-" not in yaml
    table_line = [ln for ln in out.splitlines() if ln.startswith("| Foo")][0]
    assert table_line.count("|") == 3
    assert "^mdc-aaaa1111" in table_line
    assert not table_line.rstrip().endswith("| ^mdc-aaaa1111")
    assert "A paragraph. ^mdc-bbbb2222" in out


def test_yaml_sku_id_is_cited_via_heading_not_frontmatter() -> None:
    from mdc_kb_reorg.claims import wiki_blob

    text = (
        "---\n"
        "sku_id: X100TEST\n"
        "---\n"
        "# X100TEST spec\n"
        "\nX100TEST 单箱 IT 容量 100 kW。\n"
    )
    claims = extract_claims(text, "KB/X100TEST_spec.md", "product", ALIASES)
    presence = [c for c in claims if c.kind == "sku_presence"]
    assert presence
    links = [wiki_blob(c, "X100TEST") for c in presence]
    assert all("#^mdc-" not in lk or "sku_id" not in lk for lk in links)
    assert any("#X100TEST spec" in lk for lk in links)


def test_table_claim_cites_section_heading() -> None:
    from mdc_kb_reorg.claims import wiki_blob

    text = (
        "# Layout\n"
        "\n| SKU | 冷却 |\n|---|---|\n"
        "| X100TEST | 浸没 |\n"
    )
    claims = extract_claims(text, "KB/t.md", "product", ALIASES)
    cool = [c for c in claims if c.kind == "cooling"]
    assert cool
    link = wiki_blob(cool[0], "X100TEST")
    assert "#Layout" in link
    assert "#^mdc-" not in link


def test_repair_is_idempotent() -> None:
    text = "| Foo | bar ^mdc-aaaa1111 |\n"
    out, n = repair_block_id_placement(text)
    out2, n2 = repair_block_id_placement(out)
    assert n2 == 0
    assert out == out2
