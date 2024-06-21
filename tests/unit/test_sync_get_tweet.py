from unittest.mock import patch

import pytest

from pytweet._tweet import Tweet
from pytweet.sync import get_tweet
from pytweet.tweet import TWEET_URL
from pytweet.utils import get_params


def test_sync_get_tweet_returns_dict(expected_json: dict):
    tweet_id = "1803774806980022720"

    with patch("requests.get") as mock:
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = expected_json
        data = get_tweet(tweet_id, as_dict=True)

        assert data == expected_json
        assert isinstance(data, dict)

        mock.assert_called_with(
            TWEET_URL,
            params=get_params(tweet_id),
        )


def test_sync_get_tweet_returns_class(expected_json: dict, expected_tweet: Tweet):
    tweet_id = "1803774806980022720"

    with patch("requests.get") as mock:
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = expected_json
        data = get_tweet(tweet_id)

        assert data == expected_tweet
        assert isinstance(data, Tweet)

        mock.assert_called_with(
            TWEET_URL,
            params=get_params(tweet_id),
        )


def test_sync_get_tweet_fail():
    tweet_id = "1803774806980022720"

    with patch("requests.get") as mock:
        mock.return_value.status_code = 400
        mock.return_value.text = "Error"
        with pytest.raises(Exception) as e:
            get_tweet(tweet_id)

        assert str(e.value) == "Error"


def test_sync_get_tweet_with_invalid_tweet_id():
    tweet_id = "180377480698002####"

    with pytest.raises(ValueError) as e:
        get_tweet(tweet_id)

    assert str(e.value) == f"Invalid tweet id: {tweet_id}"
