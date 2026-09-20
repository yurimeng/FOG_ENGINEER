from __future__ import annotations

import shutil
from pathlib import Path

import pytest

FIXTURE_VAULT = Path(__file__).resolve().parent / "fixtures" / "vault"


@pytest.fixture
def fixture_vault(tmp_path: Path) -> Path:
    dest = tmp_path / "vault"
    shutil.copytree(FIXTURE_VAULT, dest)
    return dest
