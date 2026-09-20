from __future__ import annotations

from pathlib import Path

from mdc_kb_reorg.claims import Claim, apply_block_ids, extract_claims
from mdc_kb_reorg.citations import check_citation
from mdc_kb_reorg.match import match_claims


def test_matching_pair_gets_block_citation(fixture_vault: Path) -> None:
    aliases = {"X100TEST": "X100TEST"}
    spec = (fixture_vault / "KB/X100TEST_spec.md").read_text(encoding="utf-8")
    ra = (fixture_vault / "Reference Architecture/X100TEST_ra.md").read_text(encoding="utf-8")
    spec_claims = extract_claims(spec, "KB/X100TEST_spec.md", "product", aliases)
    ra_claims = extract_claims(ra, "Reference Architecture/X100TEST_ra.md", "solution", aliases)
    spec2, spec_claims, _ = apply_block_ids(spec, spec_claims)
    ra2, ra_claims, _ = apply_block_ids(ra, ra_claims)
    assert "^mdc-" in spec2
    assert "^mdc-" in ra2
    report = match_claims(spec_claims + ra_claims, client=None, max_typesafe=0)
    keys = {fact.key for fact in report.linked}
    assert ("sku_presence", "X100TEST") in keys
    presence = next(f for f in report.linked if f.key == ("sku_presence", "X100TEST"))
    assert any("#^" in link or "^mdc-" in link for link in presence.blob_links)


def test_conflict_and_unsourced_seed_checklist(fixture_vault: Path) -> None:
    aliases = {"X100TEST": "X100TEST"}
    claims = []
    mapping = {
        "KB/X100TEST_spec.md": "product",
        "KB/X100TEST_conflict.md": "product",
        "KB/unsourced.md": "product",
        "Projects/alpha/Project_Record.md": "project",
        "Projects/alpha/RFI.md": "procurement",
        "Reference Architecture/X100TEST_ra.md": "solution",
    }
    for rel, domain in mapping.items():
        text = (fixture_vault / rel).read_text(encoding="utf-8")
        file_claims = extract_claims(text, rel, domain, aliases)
        _, file_claims, _ = apply_block_ids(text, file_claims)
        claims.extend(file_claims)
    report = match_claims(claims, client=None, max_typesafe=0)
    kinds = {s.kind for s in report.seeds}
    assert "mismatch" in kinds
    assert "unconfirmed" in kinds
    mismatch = next(s for s in report.seeds if s.kind == "mismatch")
    assert mismatch.files
    assert mismatch.blobs
    assert "选项" in mismatch.question
    unconf = next(s for s in report.seeds if s.kind == "unconfirmed")
    assert any(path.endswith("unsourced.md") for path in unconf.files)
    assert any(c.kind == "rfi" and c.relpath.endswith("RFI.md") for c in claims)
    assert any(f.key == ("sku_presence", "X100TEST") and "procurement" in f.domains for f in report.linked)


def _claim(**kwargs) -> Claim:
    defaults = dict(
        kind="sku_presence",
        sku="X100TEST",
        value="X100TEST",
        raw="X100TEST",
        relpath="KB/x.md",
        domain="product",
        line_no=1,
        block_id="mdc-aa",
        blob="KB/x#^mdc-aa",
        extra={},
    )
    defaults.update(kwargs)
    return Claim(**defaults)


def test_representative_prefers_canonical_product_card() -> None:
    bess = _claim(
        relpath="KB/3RD-PARTY/BESS/Suppliers/Gotion.md",
        blob="KB/3RD-PARTY/BESS/Suppliers/Gotion#^mdc-bess",
        block_id="mdc-bess",
        line_no=1,
    )
    baseline = _claim(
        relpath="KB/_COMMON/PRODUCT_SPEC_BASELINE.md",
        blob="KB/_COMMON/PRODUCT_SPEC_BASELINE#^mdc-base",
        block_id="mdc-base",
        line_no=2,
    )
    solution = _claim(
        domain="solution",
        relpath="PUBLIC/Tech_Spec/X100TEST_Tech_Spec.md",
        blob="PUBLIC/Tech_Spec/X100TEST_Tech_Spec#^mdc-sol",
        block_id="mdc-sol",
        line_no=1,
    )
    report = match_claims([bess, baseline, solution], client=None, max_typesafe=0)
    fact = next(f for f in report.linked if f.key == ("sku_presence", "X100TEST"))
    product_blob = next(b for b in fact.blob_links if "KB/" in b)
    assert "PRODUCT_SPEC_BASELINE" in product_blob
    assert "Gotion" not in product_blob


def test_rfi_blob_prefers_file_whose_path_contains_the_id() -> None:
    wrong = _claim(
        kind="rfi",
        sku=None,
        value="RFI-PIP-001",
        raw="see RFI-PIP-001",
        relpath="KB/LIQUID/X/PROCUREMENT/RFI-BUS-001_母线/RFI-BUS-001.md",
        domain="procurement",
        blob="KB/LIQUID/X/PROCUREMENT/RFI-BUS-001_母线/RFI-BUS-001#^a",
        block_id="a",
    )
    right = _claim(
        kind="rfi",
        sku=None,
        value="RFI-PIP-001",
        raw="RFI-PIP-001 管路",
        relpath="KB/LIQUID/X/PROCUREMENT/RFI-PIP-001_管路/RFI-PIP-001.md",
        domain="procurement",
        blob="KB/LIQUID/X/PROCUREMENT/RFI-PIP-001_管路/RFI-PIP-001#^b",
        block_id="b",
    )
    product_index = _claim(
        kind="rfi",
        sku=None,
        value="RFI-PIP-001",
        raw="RFI-PIP-001 listed",
        relpath="KB/LIQUID/X/3D/README.md",
        domain="product",
        blob="KB/LIQUID/X/3D/README#^c",
        block_id="c",
    )
    report = match_claims([wrong, right, product_index], client=None, max_typesafe=0)
    fact = next(f for f in report.linked if f.key == ("rfi", "RFI-PIP-001"))
    proc_blob = next(b for b in fact.blob_links if "PROCUREMENT" in b)
    assert "RFI-PIP-001_管路" in proc_blob
    assert "RFI-BUS-001" not in proc_blob


def test_typesafe_non_verified_is_not_linked_as_match() -> None:
    """Surface-equal kW must not stay in 跨域已匹配 when citation check fails closed."""

    class Boom:
        def system_one(self, *args, **kwargs):
            raise AssertionError("fabricated quote must not call TypeSafe")

    product = _claim(
        kind="sku_it_kw",
        value="220",
        raw="X100TEST IT 220 kW",
        relpath="KB/spec.md",
        extra={"kw": 220.0},
        blob="KB/spec#^p",
        block_id="p",
    )
    solution = _claim(
        kind="sku_it_kw",
        value="220",
        raw="X100TEST IT 220 kW",
        relpath="PUBLIC/ra.md",
        domain="solution",
        extra={"kw": 220.0},
        blob="PUBLIC/ra#^s",
        block_id="s",
    )
    report = match_claims(
        [product, solution],
        client=Boom(),
        max_typesafe=4,
        source_texts={"KB/spec.md": "unrelated section, no quote here", "PUBLIC/ra.md": "also unrelated"},
    )
    assert ("sku_it_kw", "X100TEST") not in {f.key for f in report.linked}
    assert any(s.kind in {"mismatch", "typesafe"} and "X100TEST" in s.question for s in report.seeds)
    # Shipped citation check is what the matcher uses.
    verdict = check_citation(
        Boom(),
        source="unrelated section, no quote here",
        claim=solution.raw,
        quote=product.raw,
    )
    assert verdict.verdict == "fabricated"
