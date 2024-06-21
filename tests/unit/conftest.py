import json
from pathlib import Path

import pytest

from pytweet._tweet import Tweet

TEST_DIR = Path(__file__).resolve().parent.parent


def get_file_path(filename: str) -> Path:
    return TEST_DIR / "examples" / filename


@pytest.fixture(scope="session")
def expected_json(filename: str = "1803774806980022720.json") -> list[str]:
    filepath = get_file_path(filename=filename)
    with open(filepath, "r") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def expected_tweet(filename: str = "1803774806980022720.json") -> Tweet:
    filepath = get_file_path(filename=filename)
    with open(filepath, "r") as f:
        return Tweet(**json.load(f))
