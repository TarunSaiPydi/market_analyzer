from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class IndexData(BaseModel):
    symbol: str
    name: str | None = None
    exchange: str | None = None
    current_price: float | None = None
    previous_close: float | None = None
    change: float | None = None
    change_percent: float | None = None


class WatchlistItem(BaseModel):
    symbol: str
    company_name: str | None = None
    exchange: str | None = None

    current_price: float | None = None
    previous_close: float | None = None

    day_high: float | None = None
    day_low: float | None = None

    fifty_two_week_high: float | None = None
    fifty_two_week_low: float |None = None

    volume: int | None = None

    change: float | None = None
    change_percent: float | None = None


class NewsItem(BaseModel):
    title: str
    summary: str | None = None
    published_date: str | None = None
    display_time: str | None = None
    thumbnail: str | None = None
    url: str | None = None


class DashboardData(BaseModel):

    market_status: str = Field(alias="marketStatus")
    last_updated: datetime = Field(alias="lastUpdated")

    indices: list[IndexData]

    watchlist: list[WatchlistItem]

    news: list[NewsItem]

    model_config = ConfigDict(
        populate_by_name=True
    )