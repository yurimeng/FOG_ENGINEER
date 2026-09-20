from __future__ import annotations

import os

import pytest

from mdc_kb_reorg.citations import check_citation
from mdc_kb_reorg.typesafe_client import MissingApiKeyError, build_client


def test_missing_api_key_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("TYPESAFE_API_KEY", raising=False)
    monkeypatch.delenv("TYPESAFE_BASE_URL", raising=False)
    with pytest.raises(MissingApiKeyError):
        build_client()


def test_live_choice_noul_score_used_by_citation_check() -> None:
    if not os.environ.get("TYPESAFE_API_KEY", "").strip():
        pytest.fail("TYPESAFE_API_KEY must be set for the live TypeSafe gating test")
    client = build_client()
    source = "The unit X100TEST has IT load 100 kW and uses CyberRow in-row CW."
    claim = "X100TEST IT load is 100 kW."
    quote = "The unit X100TEST has IT load 100 kW"
    verdict = check_citation(client, source=source, claim=claim, quote=quote)
    assert verdict.answers is not None
    assert verdict.choice in {"supports", "contradicts", "says_nothing"}
    assert verdict.noul is not None and 0.0 <= verdict.noul <= 1.0
    assert verdict.score is not None
    assert "relation" in verdict.answers.choices
    assert "same_fact" in verdict.answers.nouls
    assert "mismatch_severity" in verdict.answers.scores
    # The matcher consumes these typed fields rather than raw text.
    used = verdict.answers.used_choice("relation")
    assert used == verdict.choice


def test_fabricated_quote_does_not_need_model() -> None:
    class Boom:
        def system_one(self, *args, **kwargs):
            raise AssertionError("string-match miss must not call TypeSafe")

    verdict = check_citation(
        Boom(),
        source="hello",
        claim="X100TEST is 100 kW",
        quote="this quote is not in the source at all",
    )
    assert verdict.verdict == "fabricated"
    assert verdict.auto is True
    assert verdict.answers is None
