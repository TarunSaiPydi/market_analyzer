"""
Search Controller

Responsible for stock search APIs.
"""

from fastapi import APIRouter, Depends, Query
from app.dependencies.search_dependencies import get_search_service
from app.services.search_service import SearchService
from app.utils.response_builders import success

router = APIRouter(
    prefix="/sma/v1",
    tags=["Search"],
)


@router.get("/search")
def search_stocks(
    query: str = Query(
        ...,
        min_length=1,
        description="Stock symbol or company name",
    ),
    limit: int = Query(
        default=10,
        ge=1,
        le=50,
    ),
    offset: int = Query(
        default=0,
        ge=0,
    ),
    search_service: SearchService = Depends(
        get_search_service
    ),
):
    """
    Search stocks by symbol or company name.
    """

    result = search_service.search_stocks(
        query=query,
        limit=limit,
        offset=offset,
    )

    return success(
        message="Stocks retrieved successfully.",
        data=result.model_dump(),
    )