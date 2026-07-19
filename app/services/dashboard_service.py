"""
Dashboard Service

Responsible for aggregating dashboard data required
for the user's dashboard.
"""

from datetime import datetime, timezone

from app.logger import logger

from app.providers.market_data_provider import MarketDataProvider
from app.providers.news_provider import NewsProvider
from app.repositories.watchlist_repository import WatchlistRepository
from app.models.dashboard_models import DashboardData, IndexData, NewsItem

from app.utils.dashboard_constants import INDEX_NAMES


class DashboardService:
    """
    Service responsible for preparing dashboard data.
    """

    def __init__(
        self,
        watchlist_repository: WatchlistRepository,
        market_data_provider: MarketDataProvider,
        news_provider: NewsProvider,
    ):
        self.watchlist_repository = watchlist_repository
        self.market_data_provider = market_data_provider
        self.news_provider = news_provider

    def _get_indices(self) -> list[IndexData]:
        """
        Fetch live market indices.
        """
        logger.info("Fetching market indices.")

        return self.market_data_provider.get_indices(
            INDEX_NAMES
        )

    def _get_watchlist_symbols(self, user_id: int) -> list[str]:
        """
        Fetch user's watchlist symbols.
        """

        logger.info(
            "Fetching watchlist symbols for user_id=%s",
            user_id,
        )

        watchlist = self.watchlist_repository.get_watchlist(
            user_id
        )

        return [
            stock["symbol"]
            for stock in watchlist
        ]

    def _get_news(self, symbols: list[str]) -> list[NewsItem]:
        """
        Fetch news related to watchlist symbols.
        """

        logger.info(
            "Fetching dashboard news."
        )

        return self.news_provider.get_news_for_symbols(
            symbols
        )

    def get_dashboard(self, user_id: int) -> DashboardData:

        logger.info(
            "Preparing dashboard for user_id=%s",
            user_id,
        )

        symbols = self._get_watchlist_symbols(user_id)
        logger.info("Watchlist symbols: %s", symbols)

        indices = self._get_indices()

        watchlist = []
        news = []

        if symbols:
            watchlist = self.market_data_provider.get_multiple_stocks(
                symbols
            )
            news = self._get_news(symbols)

        logger.info(
            "Dashboard prepared successfully for user_id=%s",
            user_id,
        )

        return DashboardData(
            market_status="OPEN",
            last_updated=datetime.now(timezone.utc),
            indices=indices,
            watchlist=watchlist,
            news=news,
        )