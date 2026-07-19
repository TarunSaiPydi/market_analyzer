from api.client import api_client
from utils.constants import (
    DEFAULT_PERIOD,
    DEFAULT_INTERVAL,
)


STOCK_DETAILS_ENDPOINT = "/sma/v1/stocks/{symbol}"
STOCK_HISTORY_ENDPOINT = "/sma/v1/{symbol}/history"
STOCK_INDICATORS_ENDPOINT = "/sma/v1/{symbol}/indicators"


def stock_details(symbol: str) -> dict:
    """
    Fetch stock details.
    """

    return api_client.get(
        STOCK_DETAILS_ENDPOINT.format(symbol=symbol),
    )


def history(
    symbol: str,
    period: str = DEFAULT_PERIOD,
    interval: str = DEFAULT_INTERVAL,
) -> dict:
    """
    Fetch historical stock price data.
    """

    return api_client.get(
        STOCK_HISTORY_ENDPOINT.format(symbol=symbol),
        params={
            "period": period,
            "interval": interval,
        },
    )


def indicators(symbol: str) -> dict:
    """
    Fetch technical indicators for a stock.
    """

    return api_client.get(
        STOCK_INDICATORS_ENDPOINT.format(symbol=symbol),
    )