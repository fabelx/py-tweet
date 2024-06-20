from unittest.mock import patch

import pytest

from pytweet.sync import get_tweet
from pytweet.tweet import TWEET_URL
from pytweet.utils import get_id_token


def test_sync_get_tweet():
    expected_json = {"key": "value"}
    tweet_id = "1803774806980022720"

    with patch("requests.get") as mock:
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = expected_json
        data = get_tweet(tweet_id)

        assert data == expected_json
        assert isinstance(data, dict)

        mock.assert_called_with(
            TWEET_URL,
            params={
                "id": tweet_id,
                "lang": "en",
                "token": get_id_token(tweet_id),
                "features": ";".join(
                    [
                        "tfw_timeline_list:",
                        "tfw_follower_count_sunset:true",
                        "tfw_tweet_edit_backend:on",
                        "tfw_refsrc_session:on",
                        "tfw_fosnr_soft_interventions_enabled:on",
                        "tfw_show_birdwatch_pivots_enabled:on",
                        "tfw_show_business_verified_badge:on",
                        "tfw_duplicate_scribes_to_settings:on",
                        "tfw_use_profile_image_shape_enabled:on",
                        "tfw_show_blue_verified_badge:on",
                        "tfw_legacy_timeline_sunset:true",
                        "tfw_show_gov_verified_badge:on",
                        "tfw_show_business_affiliate_badge:on",
                        "tfw_tweet_edit_frontend:on",
                    ]
                ),
            },
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
