from unittest.mock import MagicMock, patch

import pytest

from pytweet import get_tweet
from pytweet._tweet import Tweet
from pytweet.tweet import TWEET_URL
from pytweet.utils import get_params

pytestmark = pytest.mark.asyncio


@pytest.mark.asyncio
async def test_get_tweet_returns_dict(expected_json: dict):
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
        result = await get_tweet(tweet_id, as_dict=True)

        assert result == expected_json
        assert isinstance(result, dict)

        mock_session.get.assert_called_with(
            TWEET_URL,
            params=get_params(tweet_id),
        )


@pytest.mark.asyncio
async def test_get_tweet_returns_class(expected_json: dict, expected_tweet: Tweet):
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

        assert result == expected_tweet
        assert isinstance(result, Tweet)

        mock_session.get.assert_called_with(
            TWEET_URL,
            params=get_params(tweet_id),
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
