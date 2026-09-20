"""Path inventory, origin map, relocate. Never delete."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

SKIP_DIR_NAMES = {".git"}


@dataclass(frozen=True)
class FileRecord:
    relpath: str
    sha256: str
    size: int


class OriginMap:
    """original relpath -> current relpath. Identity omitted."""

    def __init__(self, mapping: dict[str, str] | None = None) -> None:
        self._map: dict[str, str] = dict(mapping or {})

    def record(self, original: str, current: str) -> None:
        original = _posix(original)
        current = _posix(current)
        # Keep the earliest original for chained moves.
        root_original = original
        for prev_orig, prev_cur in list(self._map.items()):
            if prev_cur == original:
                root_original = prev_orig
                break
        self._map[root_original] = current
        if original != root_original and original in self._map:
            self._map[root_original] = current

    def current_of(self, original: str) -> str:
        original = _posix(original)
        return self._map.get(original, original)

    def original_of(self, current: str) -> str | None:
        current = _posix(current)
        for orig, cur in self._map.items():
            if cur == current:
                return orig
        return None

    def items(self) -> list[tuple[str, str]]:
        return sorted(self._map.items())

    def to_json(self) -> dict[str, str]:
        return dict(sorted(self._map.items()))

    @classmethod
    def from_json(cls, data: dict[str, str]) -> "OriginMap":
        return cls(data)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(self.to_json(), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    @classmethod
    def load(cls, path: Path) -> "OriginMap":
        if not path.is_file():
            return cls()
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError(f"origin map is not an object: {path}")
        return cls({str(k): str(v) for k, v in data.items()})


def _posix(rel: str | Path) -> str:
    return Path(rel).as_posix()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def snapshot(root: Path, skip_dirs: Iterable[str] = SKIP_DIR_NAMES) -> list[FileRecord]:
    root = root.resolve()
    skip = set(skip_dirs)
    records: list[FileRecord] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in skip for part in rel.parts):
            continue
        # macOS Finder "Icon\r" files: strip CR so inventories stay one-line and match.
        relpath = rel.as_posix().replace("\r", "")
        records.append(
            FileRecord(relpath=relpath, sha256=sha256_file(path), size=path.stat().st_size)
        )
    records.sort(key=lambda rec: rec.relpath)
    return records


def write_inventory(records: Iterable[FileRecord], dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"{rec.sha256}  {rec.relpath}" for rec in records]
    dest.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def load_inventory(path: Path) -> list[FileRecord]:
    records: list[FileRecord] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        records.append(FileRecord(relpath=rel, sha256=digest, size=-1))
    return records


def unique_dest(root: Path, dest_rel: str) -> str:
    dest = root / dest_rel
    if not dest.exists():
        return _posix(dest_rel)
    stem = Path(dest_rel).name
    parent = Path(dest_rel).parent
    n = 1
    while True:
        candidate = parent / f"{Path(stem).stem}__kept_{n}{Path(stem).suffix}"
        if not (root / candidate).exists():
            return candidate.as_posix()
        n += 1


def relocate_file(root: Path, src_rel: str, dest_rel: str, origin: OriginMap) -> str:
    """Move a file. Never overwrite. Never delete source without dest existing."""
    src_rel = _posix(src_rel)
    dest_rel = unique_dest(root, _posix(dest_rel))
    src = root / src_rel
    dest = root / dest_rel
    if not src.is_file():
        raise FileNotFoundError(src)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dest))
    if not dest.is_file():
        raise RuntimeError(f"move failed: {src_rel} -> {dest_rel}")
    origin.record(src_rel, dest_rel)
    return dest_rel


def assert_preserved(
    before: Iterable[FileRecord],
    after: Iterable[FileRecord],
    origin: OriginMap,
) -> list[str]:
    """Return missing original paths (defect). Relocations via origin map count as present."""
    after_paths = {rec.relpath.replace("\r", "") for rec in after}
    missing: list[str] = []
    for rec in before:
        original = rec.relpath.replace("\r", "")
        current = origin.current_of(original).replace("\r", "")
        if original in after_paths or current in after_paths:
            continue
        missing.append(original)
    return missing


_WIKI_TARGET = re.compile(
    r"\[\[([^\]|#]+)(#[^\]|]+)?(\|[^\]]+)?\]\]"
)


def rewrite_wikilinks(text: str, old_rel: str, new_rel: str) -> str:
    """Rewrite path-qualified wikilinks and markdown links after a move."""
    old = _posix(old_rel)
    new = _posix(new_rel)
    old_no = old[:-3] if old.endswith(".md") else old
    new_no = new[:-3] if new.endswith(".md") else new
    old_stem = Path(old_no).name
    new_stem = Path(new_no).name

    def repl(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        rest = (match.group(2) or "") + (match.group(3) or "")
        variants = {target, target.replace("\\", "/")}
        if target in {old, old_no, old_stem} or target.replace("\\", "/") in {old, old_no}:
            return f"[[{new_no}{rest}]]"
        return match.group(0)

    out = _WIKI_TARGET.sub(repl, text)
    out = out.replace(f"]({old})", f"]({new})")
    out = out.replace(f"]({old_no})", f"]({new_no})")
    return out


def rewrite_vault_links(root: Path, old_rel: str, new_rel: str) -> int:
    changed = 0
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        original = path.read_text(encoding="utf-8", errors="replace")
        updated = rewrite_wikilinks(original, old_rel, new_rel)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def records_to_json(records: Iterable[FileRecord]) -> list[dict]:
    return [asdict(rec) for rec in records]
