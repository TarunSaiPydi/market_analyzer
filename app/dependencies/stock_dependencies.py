"""
Stock Dependencies
"""

from app.providers.market_data_provider import MarketDataProvider
from app.repositories.stock_repository import StockRepository
from app.services.stock_service import StockService


def get_stock_service() -> StockService:
    """
    Dependency for StockService.
    """

    return StockService(
        stock_repository=StockRepository(),
        market_data_provider=MarketDataProvider(),
    )