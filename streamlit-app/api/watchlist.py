from api.client import api_client


WATCHLIST_ENDPOINT = "/watchlist"


def get_watchlist() -> dict:
    """
    Fetch the user's watchlist.
    """

    return api_client.get(
        WATCHLIST_ENDPOINT,
    )


def add_watchlist(symbol: str) -> dict:
    """
    Add a stock to the watchlist.
    """

    return api_client.post(
        WATCHLIST_ENDPOINT,
        {
            "symbol": symbol,
        },
    )


def delete_watchlist(symbol: str) -> dict:
    """
    Remove a stock from the watchlist.
    """

    return api_client.delete(
        f"{WATCHLIST_ENDPOINT}/{symbol}",
    )