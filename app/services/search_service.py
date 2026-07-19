"""
Search Service

Responsible for business logic related to stock search.
"""

from app.logger import logger
from app.models.search_models import SearchResponse, SearchStock
from app.repositories.search_repository import SearchRepository


class SearchService:

    def __init__(
        self,
        search_repository: SearchRepository,
    ):
        self.search_repository = search_repository

    def search_stocks(
        self,
        query: str,
        limit: int = 10,
        offset: int = 0,
    ) -> SearchResponse:
        """
        Search stocks.
        """

        query = query.strip()

        if not query:
            return SearchResponse(
                stocks=[],
                total=0,
            )

        logger.info(
            "Searching stocks | Query=%s",
            query,
        )

        rows = self.search_repository.search_stocks(
            query=query,
            limit=limit,
            offset=offset,
        )

        stocks = [
            SearchStock(**row)
            for row in rows
        ]

        logger.info(
            "Search completed | Query=%s Results=%d",
            query,
            len(stocks),
        )

        return SearchResponse(
            stocks=stocks,
            total=len(stocks),
        )