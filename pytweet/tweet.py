import aiohttp

from .utils import get_params, validate_tweet_id

SYNDICATION_URL = "https://cdn.syndication.twimg.com"
TWEET_URL = f"{SYNDICATION_URL}/tweet-result"


async def fetch_tweet(tweet_id) -> dict:
    params = get_params(tweet_id)

    async with aiohttp.ClientSession() as session:
        async with session.get(TWEET_URL, params=params) as resp:
            if resp.status != 200:
                raise Exception(await resp.text())

            return await resp.json()


async def get_tweet(tweet_id: str) -> dict | None:
    if not validate_tweet_id(tweet_id):
        raise ValueError(f"Invalid tweet id: {tweet_id}")

    return await fetch_tweet(tweet_id)
