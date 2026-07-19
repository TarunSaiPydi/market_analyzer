"""
History Models
"""

from datetime import date
from pydantic import BaseModel


class PriceCandle(BaseModel):
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int


class StockHistory(BaseModel):
    symbol: str
    period: str
    interval: str
    prices: list[PriceCandle]