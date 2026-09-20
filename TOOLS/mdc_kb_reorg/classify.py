"""Classify vault files into four domains + other. Path first; TypeSafe for leftovers."""

from __future__ import annotations

import re
from pathlib import Path

from typesafe_sdk import Choice

from .typesafe_client import TypedAnswers, ask_system_one

DOMAIN_PRODUCT = "product"
DOMAIN_SOLUTION = "solution"
DOMAIN_PROJECT = "project"
DOMAIN_PROCUREMENT = "procurement"
DOMAIN_OTHER = "other"
DOMAIN_UNCLASSIFIABLE = "unclassifiable"
DOMAIN_AMBIGUOUS = "ambiguous"

FOUR_DOMAINS = (
    DOMAIN_PRODUCT,
    DOMAIN_SOLUTION,
    DOMAIN_PROJECT,
    DOMAIN_PROCUREMENT,
)

DOMAIN_LABELS = {
    DOMAIN_PRODUCT: "产品设计",
    DOMAIN_SOLUTION: "解决方案",
    DOMAIN_PROJECT: "项目",
    DOMAIN_PROCUREMENT: "采购询价",
    DOMAIN_OTHER: "其他",
    DOMAIN_UNCLASSIFIABLE: "未分类",
    DOMAIN_AMBIGUOUS: "待判定",
}

PROCUREMENT_NAME = re.compile(
    r"(?:^|/)(?:PROCUREMENT|供应商询价|询价)(?:/|$)|(?:^|/)(?:RFI|RFQ)[^/]*\.(?:md|docx|pdf)$",
    re.I,
)
PROCUREMENT_BASENAME = re.compile(r"^(?:RFI|RFQ)[-_].+|^RFI\.md$|^RFQ\.md$|询价", re.I)

KNOWN_OTHER_PREFIXES = (
    "AGENTS/",
    "PROCESS/",
    "TOOLS/",
    "Business_Documents/",
    "HRBP/",
    "Market/",
    "ResoucePool/",
    "Canvas/",
    "memory/",
    "graphify-out/",
    "Factory/",
    "EXT-001-T2T3-deliverables/",
    "Claude outputs/",
    "_to_delete/",
    "_Archived/",
    ".claude/",
    ".agents/",
    ".openclaw/",
    ".tools/",
    ".permtest/",
    "_holding_unconfirmed/",
    "_domains/",
)

WORKSPACE_ROOT_FILES = {
    "CLAUDE.md",
    "AGENTS.md",
    "PRINCIPLES.md",
    "SOUL.md",
    "IDENTITY.md",
    "USER.md",
    "HEARTBEAT.md",
    "VERSION.md",
    "README.md",
    "index.md",
    "_navigation.md",
    "_graph_index.md",
    "Document Tree.md",
    "OPEN_ITEMS.md",
    "hot.md",
    "FOG_Workspace_Summary.md",
    "MIGRATION_2026-08-17_KB_Naming.md",
}


def _posix(rel: str) -> str:
    return Path(rel).as_posix()


def is_procurement_path(rel: str) -> bool:
    rel = _posix(rel)
    name = Path(rel).name
    if PROCUREMENT_NAME.search(rel):
        return True
    if PROCUREMENT_BASENAME.search(name):
        return True
    parts = Path(rel).parts
    if "RFI" in parts or "RFQ" in parts:
        return True
    return False


def classify_path(rel: str) -> str:
    """Return a domain key, or DOMAIN_AMBIGUOUS when TypeSafe should decide."""
    rel = _posix(rel)
    if rel.startswith(".") and not rel.startswith(".claude/") and "/." in f"/{rel}":
        return DOMAIN_OTHER
    for prefix in KNOWN_OTHER_PREFIXES:
        if rel.startswith(prefix):
            return DOMAIN_OTHER
    if is_procurement_path(rel):
        return DOMAIN_PROCUREMENT
    if rel.startswith("KB/"):
        return DOMAIN_PRODUCT
    if rel.startswith("Reference Architecture/") or rel.startswith("PUBLIC/"):
        return DOMAIN_SOLUTION
    if rel.startswith("Projects/"):
        return DOMAIN_PROJECT
    name = Path(rel).name
    if rel == name and name in WORKSPACE_ROOT_FILES:
        return DOMAIN_OTHER
    if rel == name and name.endswith(
        (".py", ".xlsx", ".docx", ".png", ".jpg", ".json", ".html", ".csv", ".svg", ".lock")
    ):
        return DOMAIN_OTHER
    if name in {"Icon\r", "Icon"} or name.startswith("."):
        return DOMAIN_OTHER
    # Only markdown is worth a TypeSafe domain Choice; binaries stay inventoried as other.
    if not rel.endswith(".md"):
        return DOMAIN_OTHER
    return DOMAIN_AMBIGUOUS


DOMAIN_CRITERIA = {
    "product": "Product design, SKU specs, cooling/power design guidelines, third-party component specs (not a customer project file).",
    "solution": "A reference architecture, public tech spec, or packaged solution offering.",
    "project": "A customer/site project record, proposal, or site-specific note.",
    "procurement": "An RFI, RFQ, supplier inquiry, or procurement pack.",
    "other": "Workspace rules, HR, legal, tools, market intel, or admin — not one of the four domains.",
    "unclassifiable": "Not enough evidence to assign any of the above.",
}


def typesafe_classify_file(
    client,
    *,
    relpath: str,
    excerpt: str,
) -> tuple[str, TypedAnswers]:
    answers = ask_system_one(
        client,
        state={"path": relpath, "excerpt": excerpt[:4000]},
        questions={
            "domain": Choice(
                instructions=(
                    "Which library domain does this file belong to? "
                    "Use `path` as a hint and `excerpt` as evidence. "
                    "Pick unclassifiable when the excerpt is empty, binary-like, or unrelated."
                ),
                criteria=DOMAIN_CRITERIA,
            )
        },
    )
    choice = answers.used_choice("domain")
    conf = answers.choice_confidence.get("domain", 0.0)
    if conf < 0.8 or choice not in DOMAIN_CRITERIA:
        return DOMAIN_UNCLASSIFIABLE, answers
    return choice, answers
