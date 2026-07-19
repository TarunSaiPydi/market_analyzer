from app.repositories.watchlist_repository import WatchlistRepository
from app.services.watchlist_service import WatchlistService


def get_watchlist_service() -> WatchlistService:

    repository = WatchlistRepository()

    return WatchlistService(repository)