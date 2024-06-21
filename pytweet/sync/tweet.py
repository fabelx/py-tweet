import requests

from ..utils import TWEET_URL, get_params, validate_tweet_id

try:
    from .._tweet import Tweet
except ImportError:
    Tweet = None


def fetch_tweet(tweet_id) -> dict:
    """Fetches a tweet's data.

    This function sends a synchronous GET request to the X API to fetch the tweet data
    based on the provided tweet ID.

    Args:
        tweet_id: The tweet ID for which the data is to be fetched.

    Returns:
        dict: The tweet data in JSON format.

    Raises:
        Exception: If the response status is not 200, an exception with the response text is raised.
    """
    params = get_params(tweet_id)

    resp = requests.get(TWEET_URL, params=params)
    if resp.status_code != 200:
        raise Exception(resp.text)

    return resp.json()


def get_tweet(tweet_id: str, as_dict: bool = False) -> dict | Tweet | None:
    """Retrieves tweet data based on the tweet ID.

    This function validates the tweet ID first. If valid, it fetches the tweet data
    synchronously. Depending on the `as_dict` parameter:
        - If `as_dict` is True, returns the tweet data as a dictionary.
        - If `as_dict` is False and Pydantic is installed (Tweet is not None), returns the tweet
          data as a Tweet object.
        - Otherwise, returns the tweet data as-is.

    Args:
        tweet_id: The tweet ID to retrieve.
        as_dict: Flag indicating whether to return data as a dictionary. Defaults to False.

    Returns:
        dict | Tweet | None: Tweet data in the desired format, or None if tweet ID is invalid.

    Raises:
        ValueError: If the tweet ID is invalid.
        Exception: If an error occurs during fetching the tweet data.
    """
    # The returned JSON is undocumented, so errors or data loss may eventually occur during conversion to a class.
    # It's probably better to use raw JSON instead.
    if not validate_tweet_id(tweet_id):
        raise ValueError(f"Invalid tweet id: {tweet_id}")

    data = fetch_tweet(tweet_id)
    if as_dict:
        return data

    if Tweet:
        return Tweet(**data)

    return data
