import requests

from ..tweet import TWEET_URL
from ..utils import get_params, validate_tweet_id


def fetch_tweet(tweet_id) -> dict:
    params = get_params(tweet_id)

    resp = requests.get(TWEET_URL, params=params)
    if resp.status_code != 200:
        raise Exception(resp.text)

    return resp.json()


def get_tweet(tweet_id: str) -> dict | None:
    if not validate_tweet_id(tweet_id):
        raise ValueError(f"Invalid tweet id: {tweet_id}")

    return fetch_tweet(tweet_id)
