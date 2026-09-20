"""Citation check: string-match quotes first, then TypeSafe Choice. Code owns control flow."""

from __future__ import annotations

import re
from dataclasses import dataclass

from typesafe_sdk import Choice, Noul, Score

from .typesafe_client import TypedAnswers, ask_system_one

AUTO_ACCEPT = 0.8

RELATION_TO_VERDICT = {
    "supports": "verified",
    "contradicts": "contradicted",
    "says_nothing": "unsupported",
}

CITATION_QUESTIONS = {
    "relation": Choice(
        instructions="How does the section relate to the claim?",
        criteria={
            "supports": "The section states the claim or directly implies that it is true",
            "contradicts": "The section states the opposite of the claim or implies it is false",
            "says_nothing": "The section does not address what the claim asserts, either way",
        },
    ),
    "same_fact": Noul(
        instructions="Does the section discuss the same SKU, load, cooling choice, or RFI item as the claim?",
        criteria={
            "true": "Same engineering object (SKU/load/cooling/RFI)",
            "false": "Different object or the section never names it",
        },
    ),
    "mismatch_severity": Score(
        instructions="If the section and claim both talk about the same fact, how far apart are they?",
        criteria=[
            "identical meaning and numbers",
            "wording differs but values agree",
            "values or selections conflict",
            "cannot tell or not the same fact",
        ],
    ),
}


def normalize(text: str) -> str:
    table = str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'"})
    return re.sub(r"\s+", " ", (text or "").translate(table)).strip()


def quote_in_source(source: str, quote: str | None) -> bool:
    if not quote:
        return False
    return normalize(quote) in normalize(source)


@dataclass
class CitationVerdict:
    status: str  # found | missing | section-only
    verdict: str  # verified | contradicted | unsupported | fabricated | review
    choice: str | None
    noul: float | None
    score: float | None
    confidence: float | None
    auto: bool
    answers: TypedAnswers | None = None


def check_citation(
    client,
    *,
    source: str,
    claim: str,
    quote: str | None,
) -> CitationVerdict:
    """Shipped citation check used by the matcher. Makes a real TypeSafe call when the quote exists or source is given."""
    if quote and not quote_in_source(source, quote):
        return CitationVerdict(
            status="missing",
            verdict="fabricated",
            choice=None,
            noul=None,
            score=None,
            confidence=None,
            auto=True,
            answers=None,
        )
    answers = ask_system_one(
        client,
        state={"claim": claim, "section": source[:6000]},
        questions=CITATION_QUESTIONS,
    )
    relation = answers.used_choice("relation")
    conf = answers.choice_confidence.get("relation", 0.0)
    verdict = RELATION_TO_VERDICT.get(relation, "unsupported")
    auto = conf >= AUTO_ACCEPT
    if not auto:
        verdict = "review"
    return CitationVerdict(
        status="found" if quote else "section-only",
        verdict=verdict,
        choice=relation,
        noul=answers.used_noul("same_fact"),
        score=answers.used_score("mismatch_severity"),
        confidence=conf,
        auto=auto,
        answers=answers,
    )
