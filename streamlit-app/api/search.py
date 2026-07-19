from api.client import api_client


SEARCH_ENDPOINT = "/sma/v1/search"


def search_stocks(
    query: str,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Search stocks by company name or symbol.
    """

    return api_client.get(
        SEARCH_ENDPOINT,
        params={
            "query": query,
            "limit": limit,
            "offset": offset,
        },
    )