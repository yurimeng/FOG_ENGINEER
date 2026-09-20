from __future__ import annotations

from pathlib import Path

from mdc_kb_reorg.inventory import (
    OriginMap,
    assert_preserved,
    relocate_file,
    snapshot,
    write_inventory,
)


def test_snapshot_and_relocate_never_drops_file(fixture_vault: Path, tmp_path: Path) -> None:
    before = snapshot(fixture_vault)
    assert before, "fixture vault must contain files"
    origin = OriginMap()
    src = "KB/unsourced.md"
    dest = relocate_file(fixture_vault, src, "_holding_unconfirmed/files/KB/unsourced.md", origin)
    after = snapshot(fixture_vault)
    missing = assert_preserved(before, after, origin)
    assert missing == []
    assert not (fixture_vault / src).exists()
    assert (fixture_vault / dest).is_file()
    assert origin.current_of(src) == dest
    inv = tmp_path / "inv.txt"
    write_inventory(after, inv)
    listing = inv.read_text(encoding="utf-8")
    assert f"  {src}\n" not in listing
    assert f"  {dest}\n" in listing


def test_macos_icon_cr_is_preserved(tmp_path: Path) -> None:
    vault = tmp_path / "v"
    vault.mkdir()
    (vault / "note.md").write_text("ok\n", encoding="utf-8")
    (vault / "Icon\r").write_bytes(b"icns")
    recs = snapshot(vault)
    paths = {rec.relpath for rec in recs}
    assert "Icon" in paths
    assert "note.md" in paths
    assert assert_preserved(recs, recs, OriginMap()) == []
