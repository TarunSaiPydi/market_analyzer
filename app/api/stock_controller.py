"""
Stock Controller

Responsible for stock detail APIs.
"""

from fastapi import APIRouter, Depends, Query
from app.dependencies.stock_dependencies import get_stock_service
from app.services.stock_service import StockService
from app.utils.response_builders import success

router = APIRouter(
    prefix="/sma/v1",
    tags=["Stocks"],
)


@router.get("/stocks/{symbol}")
def get_stock_details(
    symbol: str,
    stock_service: StockService = Depends(
        get_stock_service
    ),
):
    """
    Get complete stock details.
    """

    result = stock_service.get_stock_details(symbol)

    return success(
        message="Stock details retrieved successfully.",
        data=result.model_dump(),
    )

@router.get("/{symbol}/history")
def get_stock_history(
    symbol: str,
    period: str = Query(
        default="1y",
        description="1d,5d,1mo,3mo,6mo,1y,2y,5y,max",
    ),
    interval: str = Query(
        default="1d",
        description="1m,5m,15m,30m,1h,1d,1wk,1mo",
    ),
    stock_service: StockService = Depends(
        get_stock_service,
    ),
):

    result = stock_service.get_stock_history(
        symbol=symbol,
        period=period,
        interval=interval,
    )

    return success(
        message="Stock history retrieved successfully.",
        data=result.model_dump(),
    )

@router.get("/{symbol}/indicators")
def get_technical_indicators(
    symbol: str,
    period: str = Query(default="1y"),
    interval: str = Query(default="1d"),
    stock_service: StockService = Depends(get_stock_service),
):

    result = stock_service.get_technical_indicators(
        symbol=symbol,
        period=period,
        interval=interval,
    )

    return success(
        message="Technical indicators retrieved successfully.",
        data=result.model_dump(),
    )