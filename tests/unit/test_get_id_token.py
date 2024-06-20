import pytest

from pytweet.utils import get_id_token


@pytest.mark.parametrize(
    "tweet_id,expected",
    (
        (
            "1445130599547772936",
            "3i4f4pjmzkfo81xwm6lxr",
        ),
        (
            "1803774806980022720",
            "4deq4hfom7b52ey8p5vcxr",
        ),
    ),
)
def test_get_id_token(tweet_id: str, expected: str):
    assert get_id_token(tweet_id) == expected


def test_get_id_token_fail():
    with pytest.raises(ValueError):
        get_id_token("1803774806980022###")
