import pytest

from pytweet.utils import validate_tweet_id


@pytest.mark.parametrize(
    "tweet_id,expected",
    (
        (
            "1445130599547772936",
            True,
        ),
        (
            "1803774806980022720",
            True,
        ),
        (
            "1803774806980022###",
            False,
        ),
        (
            "a180377480698002272",
            False,
        ),
        (
            "1111111111118037748069800227211111111111",
            False,
        ),
        (
            "111111111111803774806980022721111111111",
            True,
        ),
    ),
)
def test_validate_tweet_id(tweet_id: str, expected: bool):
    assert validate_tweet_id(tweet_id) == expected
