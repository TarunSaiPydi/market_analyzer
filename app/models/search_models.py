"""
Search Models
"""

from pydantic import BaseModel


class SearchStock(BaseModel):
    symbol: str
    company_name: str
    exchange: str
    series: str


class SearchResponse(BaseModel):
    stocks: list[SearchStock]
    total: int