"""TypeSafe client. Credentials only from the environment. Fail closed if missing."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from typing import Any, Mapping

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

API_KEY_ENV = "TYPESAFE_API_KEY"
BASE_URL_ENV = "TYPESAFE_BASE_URL"
DEFAULT_MODEL_ENV = "TYPESAFE_DEFAULT_MODEL"


class MissingApiKeyError(RuntimeError):
    """Raised when TYPESAFE_API_KEY is absent. Fail closed."""


def env_api_key() -> str:
    return os.environ.get(API_KEY_ENV, "").strip()


def build_client() -> TypeSafeClient:
    key = env_api_key()
    if not key:
        raise MissingApiKeyError(
            f"{API_KEY_ENV} is missing or empty; refusing to construct a TypeSafe client"
        )
    kwargs: dict[str, str] = {"api_key": key}
    base = os.environ.get(BASE_URL_ENV, "").strip()
    model = os.environ.get(DEFAULT_MODEL_ENV, "").strip()
    if base:
        kwargs["base_url"] = base
    if model:
        kwargs["model"] = model
    return TypeSafeClient(**kwargs)


def redact(text: str, key: str | None = None) -> str:
    secret = key if key is not None else env_api_key()
    if not secret:
        return text
    return text.replace(secret, "***REDACTED***")


@dataclass
class TypedAnswers:
    """Shipped view of a System One response used by the matcher."""

    choices: dict[str, str]
    choice_confidence: dict[str, float]
    nouls: dict[str, float]
    scores: dict[str, float]
    score_confidence: dict[str, float]
    raw_keys: tuple[str, ...]

    def used_choice(self, qid: str) -> str:
        return self.choices[qid]

    def used_noul(self, qid: str) -> float:
        return self.nouls[qid]

    def used_score(self, qid: str) -> float:
        return self.scores[qid]


def ask_system_one(
    client: TypeSafeClient,
    state: Any,
    questions: Mapping[str, Choice | Noul | Score],
    *,
    model: str | None = None,
) -> TypedAnswers:
    kwargs: dict[str, Any] = {"state": state, "questions": questions}
    if model:
        kwargs["model"] = model
    response = client.system_one(**kwargs)
    choices: dict[str, str] = {}
    choice_conf: dict[str, float] = {}
    for qid, ans in getattr(response, "choices", {}).items():
        choices[qid] = str(ans.choice)
        choice_conf[qid] = float(ans.confidence)
    nouls: dict[str, float] = {}
    for qid, ans in getattr(response, "nouls", {}).items():
        nouls[qid] = float(ans.noul)
    scores: dict[str, float] = {}
    score_conf: dict[str, float] = {}
    for qid, ans in getattr(response, "scores", {}).items():
        scores[qid] = float(ans.score)
        score_conf[qid] = float(ans.confidence)
    return TypedAnswers(
        choices=choices,
        choice_confidence=choice_conf,
        nouls=nouls,
        scores=scores,
        score_confidence=score_conf,
        raw_keys=tuple(questions.keys()),
    )


PRICE_RE = re.compile(
    r"(?:USD|CNY|RMB|\$|€|￥|¥)\s*\d|\d[\d,]*\s*(?:万元|美元|人民币)|报价\s*[:：]?\s*\d",
    re.I,
)


def looks_like_price(text: str) -> bool:
    return bool(PRICE_RE.search(text or ""))
