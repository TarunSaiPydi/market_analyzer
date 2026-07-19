"""
Watchlist Service

Responsible for business logic.
"""

from app.repositories.watchlist_repository import WatchlistRepository
from app.logger import logger
from app.utils.response_builders import error, success
from app.utils.constants import STATUS_ERROR
from app.exceptions.watchlist_exceptions import WatchlistNotFoundError


class WatchlistService:

    def __init__(self, repository: WatchlistRepository):
        self.repository = repository

    def add_watchlist(self, user_id: int, symbol: str) -> dict:

        symbol = symbol.upper().strip()

        watchlist = self.repository.add_watchlist(
            user_id=user_id,
            symbol=symbol,
        )

        logger.info(
            "Watchlist item added | UserId=%s Symbol=%s",
            user_id,
            symbol,
        )

        return success(
                message="Watchlist added successfully.",
                data=watchlist
        )

    def get_watchlist(self, user_id: int) -> dict:

        watchlist = self.repository.get_watchlist(user_id)

        return success(
            message="Watchlist retrieved successfully.",
            data={
                "count": len(watchlist),
                "items": watchlist
            }
        )

    def remove_watchlist(self, user_id: int,symbol: str) -> dict:

        symbol = symbol.upper().strip()

        deleted = self.repository.remove_watchlist(
            user_id=user_id,
            symbol=symbol,
        )

        if not deleted:

            raise WatchlistNotFoundError(
                "Ticker not found in watchlist.",
            )

        logger.info(
            "Watchlist item removed | UserId=%s Symbol=%s",
            user_id,
            symbol,
        )

        return success(
            message=f"{symbol} removed successfully."
        )