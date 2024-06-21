from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Base(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)


class Hashtag(Base):
    indices: list[int] = None
    text: str = None


class EntityUrl(BaseModel):
    display_url: str = None
    expanded_url: str = None
    indices: list[int] = None
    url: str = None


class Media(Base):
    display_url: str = None
    expanded_url: str = None
    indices: list[int] = None
    url: str = None


class Entities(Base):
    hashtags: list[Hashtag] = None
    urls: list[EntityUrl] = None
    user_mentions: list[Any] = None
    symbols: list[Any] = None
    media: list[Media] = None


class EditControl(Base):
    edit_tweet_ids: list[str] = None
    editable_until_msecs: str = None
    is_edit_eligible: bool = None
    edits_remaining: str = None


class ExtMediaAvailability(Base):
    status: str = None


class FocusRect(Base):
    x: int = None
    y: int = None
    w: int = None
    h: int = None


class OriginalInfo(Base):
    height: int = None
    width: int = None
    focus_rects: list[FocusRect] = None


class Size(Base):
    h: int = None
    resize: str = None
    w: int = None


class Sizes(Base):
    large: Size = None
    medium: Size = None
    small: Size = None
    thumb: Size = None


class MediaDetails(Base):
    display_url: str = None
    expanded_url: str = None
    ext_media_availability: ExtMediaAvailability = None
    indices: list[int] = None
    media_url_https: str = None
    original_info: OriginalInfo = None
    sizes: Sizes = None
    type: str = None
    url: str = None


class BackgroundColor(Base):
    red: int = None
    green: int = None
    blue: int = None


class CropCandidate(Base):
    x: int = None
    y: int = None
    w: int = None
    h: int = None


class Photo(Base):
    background_color: BackgroundColor = Field(alias="backgroundColor", default=None)
    crop_candidates: list[CropCandidate] = Field(alias="cropCandidates", default=None)
    expanded_url: str = Field(alias="expandedUrl", default=None)
    url: str = None
    width: int = None
    height: int = None


class Badge(Base):
    url: str = None


class Url(Base):
    url: str = None
    url_type: str = None


class HighlightedLabel(Base):
    description: str = None
    badge: Badge = None
    url: Url = None
    user_label_type: str = None
    user_label_display_type: str = None


class User(Base):
    id_str: str = None
    name: str = None
    profile_image_url_https: str = None
    screen_name: str = None
    verified: bool = None
    verified_type: str = None
    highlighted_label: HighlightedLabel = None
    is_blue_verified: bool = None
    profile_image_shape: str = None


class Tweet(Base):
    lang: str = None
    favorite_count: int = None
    possibly_sensitive: bool = None
    created_at: datetime = None
    display_text_range: list[int] = None
    entities: Entities = None
    id_str: str = None
    text: str = None
    user: User = None
    edit_control: EditControl = None
    media_details: list[MediaDetails] = Field(alias="mediaDetails", default=None)
    photos: list[Photo] = None
    conversation_count: int = None
    news_action_type: str = None
    is_edited: bool = Field(alias="isEdited", default=None)
    is_stale_edit: bool = Field(alias="isStaleEdit", default=None)
