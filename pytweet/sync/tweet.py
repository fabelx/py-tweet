import requests

from ..tweet import TWEET_URL
from ..utils import get_id_token, validate_tweet_id


def fetch_tweet(tweet_id) -> dict:
    # todo: move params
    params = {
        "id": tweet_id,
        "lang": "en",  # todo: maybe optional
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
    }

    resp = requests.get(TWEET_URL, params=params)
    if resp.status_code != 200:
        raise Exception(resp.text)

    return resp.json()


def get_tweet(tweet_id: str) -> dict | None:
    if not validate_tweet_id(tweet_id):
        raise ValueError(f"Invalid tweet id: {tweet_id}")

    return fetch_tweet(tweet_id)
