"""
Stock Models
"""

from pydantic import BaseModel


class StockDetails(BaseModel):
    symbol: str
    company_name: str
    exchange: str
    currency: str

    sector: str | None = None
    industry: str | None = None
    website: str | None = None
    summary: str | None = None

    current_price: float | None = None
    previous_close: float | None = None

    day_high: float | None = None
    day_low: float | None = None

    fifty_two_week_high: float | None = None
    fifty_two_week_low: float |None = None

    volume: int | None = None
    market_cap: int | None = None

    change: float | None = None
    change_percent: float | None = None

    pe_ratio: float | None = None
    eps: float | None = None
    book_value: float | None = None
    dividend_yield: float | None = None
    beta: float | None = None

    employee_count: int | None = None
    ceo: str | None = None
    country: str | None = None