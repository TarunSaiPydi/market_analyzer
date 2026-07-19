from fastapi import APIRouter, Depends
from app.dependencies.watchlist_dependencies import get_watchlist_service
from app.dependencies.security_dependencies import get_current_user
from app.models.watchlist_models import AddWatchlistRequest
from app.services.watchlist_service import WatchlistService

router = APIRouter(
    prefix="/watchlist",
    tags=["Watchlist"],
)

@router.post("")
def add_watchlist(
    request: AddWatchlistRequest,
    current_user=Depends(get_current_user),
    service: WatchlistService = Depends(get_watchlist_service),
):
    return service.add_watchlist(
        current_user["id"],
        request.symbol,
    )

@router.get("")
def get_watchlist(
    current_user=Depends(get_current_user),
    service: WatchlistService = Depends(get_watchlist_service),
):
    return service.get_watchlist(
        current_user["id"],
    )


@router.delete("/{symbol}")
def remove_watchlist(
    symbol: str,
    current_user=Depends(get_current_user),
    service: WatchlistService = Depends(get_watchlist_service),
):
    return service.remove_watchlist(
        current_user["id"],
        symbol,
    )

