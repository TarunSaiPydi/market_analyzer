from app.repositories.watchlist_repository import WatchlistRepository
from app.services.dashboard_service import DashboardService
from app.providers.market_data_provider import MarketDataProvider
from app.providers.news_provider import NewsProvider


def get_market_data() -> MarketDataProvider:
    return MarketDataProvider()


def get_news_provider() -> NewsProvider:
    return NewsProvider()


def get_dashboard_service() -> DashboardService:

    repository = WatchlistRepository()

    market_provider = MarketDataProvider()

    news_provider = NewsProvider()

    return DashboardService(
        watchlist_repository=repository,
        market_data_provider=market_provider,
        news_provider=news_provider,
    )