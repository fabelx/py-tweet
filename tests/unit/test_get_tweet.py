from unittest.mock import MagicMock, patch

import pytest

from pytweet import get_tweet
from pytweet.tweet import TWEET_URL
from pytweet.utils import get_id_token

pytestmark = pytest.mark.asyncio


@pytest.mark.asyncio
async def test_get_tweet():
    expected_json = {"key": "value"}
    tweet_id = "1803774806980022720"

    async def __json():
        return expected_json

    mock_response = MagicMock()
    mock_response.status = 200
    mock_response.json = __json

    mock_session = MagicMock()
    mock_session.get.return_value.__aenter__.return_value = mock_response

    with patch("aiohttp.ClientSession") as MockClientSession:
        MockClientSession.return_value.__aenter__.return_value = mock_session
        result = await get_tweet(tweet_id)

        assert result == expected_json
        assert isinstance(result, dict)

        mock_session.get.assert_called_with(
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


@pytest.mark.asyncio
async def test_get_tweet_fail():
    tweet_id = "1803774806980022720"

    async def text():
        return "Error"

    mock_response = MagicMock()
    mock_response.status = 400
    mock_response.text = text

    mock_session = MagicMock()
    mock_session.get.return_value.__aenter__.return_value = mock_response

    with patch("aiohttp.ClientSession") as MockClientSession:
        MockClientSession.return_value.__aenter__.return_value = mock_session

        with pytest.raises(Exception) as e:
            await get_tweet(tweet_id)

        assert str(e.value) == await text()


@pytest.mark.asyncio
async def test_get_tweet_with_invalid_tweet_id():
    tweet_id = "18037748069800#####"

    with pytest.raises(ValueError) as e:
        await get_tweet(tweet_id)

    assert str(e.value) == f"Invalid tweet id: {tweet_id}"
