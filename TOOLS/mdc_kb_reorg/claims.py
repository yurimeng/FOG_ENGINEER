"""Extract matchable claims and attach Obsidian block ids. Never rewrite numbers."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path

from .classify import DOMAIN_LABELS, FOUR_DOMAINS
from .typesafe_client import looks_like_price

DEFAULT_ALIASES = {
    "DC45": "L1240C45",
    "AC45": "I400C45",
    "AC40": "I400C40",
    "AC20": "I200C20",
    "A32": "I50TS",
    "L1240C45SUR150": "L1240C45",
    "L1800C45DR220": "L1800C45",
    "L450C20DR150": "L450C20",
    "I400C45SUT50": "I400C45",
    "I400C40ST50": "I400C40",
    "I200C20ST50": "I200C20",
}

SKU_CORE = [
    "L1240C45",
    "L1800C45",
    "L450C20",
    "I400C45",
    "I400C40",
    "I200C20",
    "I50TS",
    "DC45",
    "AC45",
    "AC40",
    "AC20",
    "A32",
]

BLOCK_ID_RE = re.compile(r"\s+\^([A-Za-z0-9_-]+)\s*$")
BLOCK_ID_IN_TABLE_RE = re.compile(r"\s+\^([A-Za-z0-9_-]+)\s*\|\s*$")
LOAD_RE = re.compile(
    r"(?P<num>\d+(?:\.\d+)?)\s*(?P<unit>kW|MW|千瓦)",
    re.I,
)
RFI_RE = re.compile(r"\b((?:RFI|RFQ)[-_][A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*)\b")
COOLING_RE = re.compile(
    r"(CRAH|CyberRow|列间空调|CDU|STULZ\s+\S+|OHS-084|CRS\s*\d+|浸没|液冷|DLC|immersion)",
    re.I,
)
COOLING_FAMILIES = (
    (re.compile(r"immersion|浸没", re.I), "immersion"),
    (re.compile(r"cyberrow|列间", re.I), "cyberrow"),
    (re.compile(r"crah|吊顶", re.I), "crah"),
    (re.compile(r"\bcdu\b", re.I), "cdu"),
    (re.compile(r"stulz|ohs-084|crs\s*\d+", re.I), "stulz"),
    (re.compile(r"液冷|dlc|liquid", re.I), "liquid"),
)


def normalize_cooling(token: str) -> str:
    raw = (token or "").strip()
    for pattern, family in COOLING_FAMILIES:
        if pattern.search(raw):
            return family
    return raw.lower()
UNCONFIRMED_RE = re.compile(r"#unconfirmed|⏳")
IT_CAPACITY_CUE = re.compile(
    r"单箱\s*IT|整箱\s*IT|IT\s*(?:容量|负荷|Load)|IT\s*load|整箱\s*(?:\d+\s*(?:kW|MW))",
    re.I,
)
NON_IT_LOAD_CUE = re.compile(
    r"UPS|单槽|单柜|柜密度|kW/rack|/rack|CDU|列间|净冷量|冷量|风机|"
    r"排热|冷站|多箱|合计|风冷柜|模块额定|site\s*total|项目总量|站端|额定功率",
    re.I,
)


def _span_distance(a0: int, a1: int, b0: int, b1: int) -> int:
    if a1 <= b0:
        return b0 - a1
    if b1 <= a0:
        return a0 - b1
    return 0


def _clause_slice(text: str, pos: int) -> tuple[int, int]:
    seps = "；。;"
    left = 0
    for i, ch in enumerate(text):
        if i >= pos:
            break
        if ch in seps:
            left = i + 1
    right = len(text)
    for i in range(pos, len(text)):
        if text[i] in seps:
            right = i
            break
    return left, right


def _is_it_capacity_load(line: str, start: int, end: int) -> bool:
    """Only SKU IT 容量. Reject UPS / 单槽 / 单柜 / CDU / 列间冷量 / 项目合计."""
    local = line[max(0, start - 36) : min(len(line), end + 20)]
    clause = line[_clause_slice(line, start)[0] : _clause_slice(line, start)[1]]
    it_local = IT_CAPACITY_CUE.search(local)
    non_local = NON_IT_LOAD_CUE.search(local)
    if non_local and not it_local:
        return False
    if it_local and not non_local:
        return True
    if it_local and non_local:
        it_pos = it_local.start() + max(0, start - 36)
        non_pos = non_local.start() + max(0, start - 36)
        return abs(it_pos - start) <= abs(non_pos - start)
    if IT_CAPACITY_CUE.search(clause) and not NON_IT_LOAD_CUE.search(clause):
        return True
    return False


def _nearest_sku(
    start: int,
    end: int,
    sku_hits: list[tuple[int, int, str]],
    text: str,
    *,
    max_dist: int = 80,
) -> str | None:
    """Bind a number to the SKU it modifies: same clause, then SKU before the number."""
    c0, c1 = _clause_slice(text, start)
    in_clause = [(ss, se, sku) for ss, se, sku in sku_hits if ss >= c0 and se <= c1]
    pool = in_clause or list(sku_hits)
    before = [(ss, se, sku) for ss, se, sku in pool if se <= start]
    use = before or pool
    best: str | None = None
    best_d: int | None = None
    for ss, se, sku in use:
        dist = _span_distance(start, end, ss, se)
        if best_d is None or dist < best_d:
            best, best_d = sku, dist
    if best is None or best_d is None or best_d > max_dist:
        return None
    return best


@dataclass
class Claim:
    kind: str  # sku_presence | sku_it_kw | cooling | rfi | unconfirmed
    sku: str | None
    value: str
    raw: str
    relpath: str
    domain: str
    line_no: int
    block_id: str | None = None
    blob: str = "no blob"
    extra: dict = field(default_factory=dict)

    @property
    def match_key(self) -> tuple[str, str]:
        sku = self.sku or "_"
        if self.kind == "rfi":
            return ("rfi", self.value)
        if self.kind == "cooling":
            return ("cooling", sku)
        if self.kind == "sku_it_kw":
            return ("sku_it_kw", sku)
        if self.kind == "sku_presence":
            return ("sku_presence", sku)
        return (self.kind, sku)


def normalize_sku(token: str, aliases: dict[str, str], relpath: str = "") -> str:
    token = token.strip()
    path = relpath.replace("\\", "/")
    # Legacy "DC45 L1800" inside the L1800C45 tree is L1800C45, not L1240C45.
    if token == "DC45" and "L1800C45" in path:
        return "L1800C45"
    return aliases.get(token, token)


def sku_pattern(aliases: dict[str, str]) -> re.Pattern[str]:
    tokens = sorted(set(list(aliases.keys()) + list(aliases.values()) + SKU_CORE), key=len, reverse=True)
    escaped = "|".join(re.escape(t) for t in tokens if t)
    # Fixture / test SKUs (never used as live-vault oracles).
    extra = r"|X[0-9]+TEST" if escaped else r"X[0-9]+TEST"
    return re.compile(rf"\b(?:{escaped}{extra})\b")


def load_alias_map(root: Path) -> dict[str, str]:
    aliases = dict(DEFAULT_ALIASES)
    naming = root / "KB" / "NAMING_MAP.md"
    if not naming.is_file():
        return aliases
    text = naming.read_text(encoding="utf-8", errors="replace")
    row = re.compile(
        r"\|\s*([A-Za-z0-9_-]+)\s*\|\s*\*\*([A-Za-z0-9]+)\*\*\s*\|\s*`([A-Za-z0-9]+)`"
    )
    for match in row.finditer(text):
        old, short, full = match.group(1), match.group(2), match.group(3)
        aliases[old] = short
        aliases[full] = short
        aliases[short] = short
    return aliases


def _to_kw(num: float, unit: str) -> float:
    if unit.lower() in {"mw"}:
        return num * 1000.0
    return num


def _skip_changelog(lines: list[str]) -> list[tuple[int, str]]:
    return list(_iter_body_lines(lines))


def _iter_body_lines(lines: list[str]) -> list[tuple[int, str]]:
    """Skip YAML frontmatter and stop at Changelog."""
    start = 0
    if lines and lines[0].strip() == "---":
        start = 1
        while start < len(lines) and lines[start].strip() != "---":
            start += 1
        start += 1
    out: list[tuple[int, str]] = []
    for i, line in enumerate(lines[start:], start=start + 1):
        if re.match(r"^##\s+Changelog\b", line, re.I):
            break
        out.append((i, line))
    return out


def nearest_heading(text: str, line_no: int) -> str | None:
    heading = None
    for i, line in enumerate(text.splitlines(), start=1):
        if i > line_no:
            break
        m = re.match(r"^(#{1,6})\s+(.+)$", line.strip())
        if m:
            heading = re.sub(r"\s+\^[A-Za-z0-9_-]+\s*$", "", m.group(2)).strip()
    return heading or None


def _anchor_kind(line: str, line_no: int, fm_end: int) -> str:
    if fm_end and line_no <= fm_end:
        return "yaml"
    stripped = line.strip()
    if stripped.startswith("|"):
        return "table"
    if re.match(r"^#{1,6}\s", stripped):
        return "heading"
    return "para"


def bind_citation_anchors(text: str, claims: list[Claim]) -> list[Claim]:
    """Table/YAML/heading claims cite the nearest section heading, not an unindexable ^id."""
    fm_end = _frontmatter_line_count(text)
    lines = text.splitlines()
    for claim in claims:
        if claim.line_no < 1 or claim.line_no > len(lines):
            continue
        line = lines[claim.line_no - 1]
        kind = _anchor_kind(line, claim.line_no, fm_end)
        heading = nearest_heading(text, claim.line_no)
        if heading:
            claim.extra["heading"] = heading
        if kind != "para":
            claim.extra["cite_heading"] = True
            claim.block_id = None
            claim.blob = (
                f"{_note_target(claim.relpath)}#{heading}" if heading else "no blob"
            )
    return claims


def extract_claims(
    text: str,
    relpath: str,
    domain: str,
    aliases: dict[str, str] | None = None,
    *,
    max_per_file: int = 80,
) -> list[Claim]:
    if domain not in FOUR_DOMAINS:
        return []
    aliases = aliases or dict(DEFAULT_ALIASES)
    sku_re = sku_pattern(aliases)
    claims: list[Claim] = []
    lines = text.splitlines()
    for line_no, line in _skip_changelog(lines):
        if looks_like_price(line):
            continue
        stripped = line.strip()
        if not stripped or stripped.startswith("```"):
            continue
        if re.match(r"^#{1,6}\s", stripped):
            continue
        sku_hits = [
            (m.start(), m.end(), normalize_sku(m.group(0), aliases, relpath))
            for m in sku_re.finditer(stripped)
        ]
        skus = list(dict.fromkeys(sku for _, _, sku in sku_hits))
        block = line_block_id(line)
        blob = f"{_note_target(relpath)}#^{block}" if block else "no blob"

        changelog_hist = bool(re.search(r"变更记录|^\|\s*V?\d+\.\d+", stripped))
        if (
            UNCONFIRMED_RE.search(stripped)
            and (skus or LOAD_RE.search(stripped))
            and not changelog_hist
        ):
            claims.append(
                Claim(
                    kind="unconfirmed",
                    sku=skus[0] if skus else None,
                    value=stripped[:200],
                    raw=stripped,
                    relpath=relpath,
                    domain=domain,
                    line_no=line_no,
                    block_id=block,
                    blob=blob,
                )
            )

        for sku in skus:
            claims.append(
                Claim(
                    kind="sku_presence",
                    sku=sku,
                    value=sku,
                    raw=stripped,
                    relpath=relpath,
                    domain=domain,
                    line_no=line_no,
                    block_id=block,
                    blob=blob,
                )
            )

        sku_loads: dict[str, tuple[int, float, str]] = {}
        for load in LOAD_RE.finditer(stripped):
            if not _is_it_capacity_load(stripped, load.start(), load.end()):
                continue
            kw = _to_kw(float(load.group("num")), load.group("unit"))
            sku = _nearest_sku(load.start(), load.end(), sku_hits, stripped)
            if sku is None:
                continue
            dist = min(
                _span_distance(load.start(), load.end(), ss, se)
                for ss, se, name in sku_hits
                if name == sku
            )
            prev = sku_loads.get(sku)
            if prev is None or dist < prev[0]:
                sku_loads[sku] = (dist, kw, load.group("unit"))
        for sku, (_dist, kw, unit) in sku_loads.items():
            claims.append(
                Claim(
                    kind="sku_it_kw",
                    sku=sku,
                    value=f"{kw:.4g}",
                    raw=stripped,
                    relpath=relpath,
                    domain=domain,
                    line_no=line_no,
                    block_id=block,
                    blob=blob,
                    extra={"kw": kw, "unit": unit},
                )
            )

        sku_cool: dict[str, tuple[int, str]] = {}
        for cool in COOLING_RE.finditer(stripped):
            token = cool.group(0).strip()
            sku = _nearest_sku(cool.start(), cool.end(), sku_hits, stripped)
            if sku is None:
                continue
            dist = min(
                _span_distance(cool.start(), cool.end(), ss, se)
                for ss, se, name in sku_hits
                if name == sku
            )
            prev = sku_cool.get(sku)
            if prev is None or dist < prev[0]:
                sku_cool[sku] = (dist, token)
        for sku, (_dist, token) in sku_cool.items():
            claims.append(
                Claim(
                    kind="cooling",
                    sku=sku,
                    value=normalize_cooling(token),
                    raw=stripped,
                    relpath=relpath,
                    domain=domain,
                    line_no=line_no,
                    block_id=block,
                    blob=blob,
                    extra={"cooling_raw": token},
                )
            )

        for rfi in RFI_RE.finditer(stripped):
            claims.append(
                Claim(
                    kind="rfi",
                    sku=skus[0] if skus else None,
                    value=rfi.group(1),
                    raw=stripped,
                    relpath=relpath,
                    domain=domain,
                    line_no=line_no,
                    block_id=block,
                    blob=blob,
                )
            )

        if len(claims) >= max_per_file:
            break
    return bind_citation_anchors(text, _dedupe(claims))


def _dedupe(claims: list[Claim]) -> list[Claim]:
    seen: set[tuple] = set()
    out: list[Claim] = []
    for claim in claims:
        key = (claim.kind, claim.sku, claim.value, claim.relpath, claim.line_no)
        if key in seen:
            continue
        seen.add(key)
        out.append(claim)
    return out


def _note_target(relpath: str) -> str:
    rel = Path(relpath).as_posix()
    if rel.endswith(".md"):
        rel = rel[:-3]
    return rel


def claim_block_id(claim: Claim) -> str:
    if claim.block_id:
        return claim.block_id
    material = f"{claim.relpath}|{claim.kind}|{claim.sku}|{claim.value}|{claim.line_no}"
    digest = hashlib.sha1(material.encode("utf-8")).hexdigest()[:10]
    return f"mdc-{digest}"


def line_block_id(core: str) -> str | None:
    m = BLOCK_ID_IN_TABLE_RE.search(core) if core.lstrip().startswith("|") else None
    if m:
        return m.group(1)
    m = BLOCK_ID_RE.search(core)
    return m.group(1) if m else None


def _frontmatter_line_count(text: str) -> int:
    if not text.startswith("---"):
        return 0
    lines = text.splitlines()
    for i, ln in enumerate(lines[1:], start=2):
        if ln.strip() == "---":
            return i
    return 0


def _attach_block_token(core: str, block: str) -> str:
    """Legal placement: inside last table cell, or end of a paragraph. Never YAML/after-pipe."""
    stripped = core.rstrip()
    if re.match(r"^#{1,6}\s", stripped):
        return core
    if stripped.lstrip().startswith("|"):
        # Table rows are not Obsidian blocks; do not inject ^id (cite heading instead).
        return core
    if BLOCK_ID_RE.search(core):
        return core
    return f"{core} ^{block}"


def ensure_block_id(text: str, claim: Claim) -> tuple[str, str, bool]:
    """Append ^block-id to the claim line if missing. Does not change other bytes."""
    lines = text.splitlines(keepends=True)
    idx = claim.line_no - 1
    if idx < 0 or idx >= len(lines):
        return text, claim.block_id or "no blob", False
    fm_end = _frontmatter_line_count(text)
    if fm_end and claim.line_no <= fm_end:
        return text, claim.block_id or "no blob", False
    line = lines[idx]
    newline = ""
    if line.endswith("\r\n"):
        core, newline = line[:-2], "\r\n"
    elif line.endswith("\n"):
        core, newline = line[:-1], "\n"
    else:
        core = line
    after_pipe = bool(re.search(r"\|\s+\^[A-Za-z0-9_-]+\s*$", core))
    existing_id = line_block_id(core)
    if existing_id and not after_pipe:
        return text, existing_id, False
    block = existing_id or claim_block_id(claim)
    new_core = _attach_block_token(core, block)
    if new_core == core:
        return text, block, False
    lines[idx] = new_core + newline
    return "".join(lines), block, True


def repair_block_id_placement(text: str) -> tuple[str, int]:
    """Move after-pipe table ids into the last cell; strip ids from YAML frontmatter."""
    lines = text.splitlines(keepends=True)
    n = 0
    in_fm = False
    out: list[str] = []
    after_pipe = re.compile(r"^(.*?)\|\s+(\^mdc-[0-9a-f]+)\s*$")
    yaml_id = re.compile(r"\s+\^mdc-[0-9a-f]+\s*")
    for i, line in enumerate(lines):
        if line.endswith("\r\n"):
            core, newline = line[:-2], "\r\n"
        elif line.endswith("\n"):
            core, newline = line[:-1], "\n"
        else:
            core, newline = line, ""
        if i == 0 and core.strip() == "---":
            in_fm = True
            out.append(line)
            continue
        if in_fm and core.strip() == "---":
            in_fm = False
            out.append(line)
            continue
        if in_fm:
            new = yaml_id.sub("", core).rstrip()
            if new != core.rstrip():
                n += 1
            out.append(new + newline)
            continue
        m = after_pipe.match(core)
        if m and core.lstrip().startswith("|"):
            left, bid = m.group(1).rstrip(), m.group(2)
            core = f"{left} {bid} |"
            n += 1
        out.append(core + newline)
    return "".join(out), n


def apply_block_ids(text: str, claims: list[Claim]) -> tuple[str, list[Claim], bool]:
    changed = False
    # Apply from bottom so line numbers stay valid.
    ordered = sorted(claims, key=lambda c: c.line_no, reverse=True)
    updated_by_line: dict[int, str] = {}
    for claim in ordered:
        if claim.extra.get("cite_heading"):
            continue
        text, block, did = ensure_block_id(text, claim)
        if did:
            changed = True
        updated_by_line[claim.line_no] = block
        claim.block_id = block
        claim.blob = f"{_note_target(claim.relpath)}#^{block}"
    return text, claims, changed


def wiki_blob(claim: Claim, label: str | None = None) -> str:
    shown = label or claim.value
    note = _note_target(claim.relpath)
    heading = (claim.extra or {}).get("heading")
    if claim.extra.get("cite_heading") and heading:
        return f"[[{note}#{heading}|{shown}]]"
    if claim.block_id:
        return f"[[{note}#^{claim.block_id}|{shown}]]"
    if heading:
        return f"[[{note}#{heading}|{shown}]]"
    return f"[[{note}|{shown}]]"
