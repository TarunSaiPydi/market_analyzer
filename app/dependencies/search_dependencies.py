"""
Search Dependencies
"""

from app.repositories.search_repository import SearchRepository
from app.services.search_service import SearchService


def get_search_service() -> SearchService:
    return SearchService(
        search_repository=SearchRepository(),
    )