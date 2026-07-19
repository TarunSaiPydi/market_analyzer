"""
Response Builder

Provides helper methods to build
consistent API responses.
"""

from typing import Any

from app.utils.constants import STATUS_SUCCESS, STATUS_ERROR


def success(message: str, data: Any = None) -> dict:
    """
    Build a successful API response.

    Args:
        message: Success message.
        data: Response payload.

    Returns:
        Standard success response.
    """

    response = {
        "status": STATUS_SUCCESS,
        "message": message,
        "data": data
    }

    if data is None:
        response.pop("data")

    return response


def error(message: str, data: Any = None) -> dict:
    """
    Build an error API response.

    Args:
        message: Error message.
        data: Additional error information.

    Returns:
        Standard error response.
    """

    response = {
        "status": STATUS_ERROR,
        "message": message,
        "data": data
    }

    if data is None:
        response.pop("data")

    return response