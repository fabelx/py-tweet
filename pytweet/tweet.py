from dataclasses import dataclass, field
from typing import Any, Dict

import aiohttp

from .utils import get_id_token, validate_tweet_id

SYNDICATION_URL = "https://cdn.syndication.twimg.com"
TWEET_URL = f"{SYNDICATION_URL}/tweet-result"


async def fetch_tweet(tweet_id) -> dict:
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

    async with aiohttp.ClientSession() as session:
        async with session.get(TWEET_URL, params=params) as resp:
            if resp.status != 200:
                raise Exception(await resp.text())

            return await resp.json()


async def get_tweet(tweet_id: str) -> dict | None:
    if not validate_tweet_id(tweet_id):
        raise ValueError(f"Invalid tweet id: {tweet_id}")

    return await fetch_tweet(tweet_id)
