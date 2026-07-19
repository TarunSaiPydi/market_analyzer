"""
Authentication dependencies.

Provides dependency injection for
authentication services.
"""

from app.services.auth_service import AuthService


def get_auth_service() -> AuthService:
    """
    Returns an AuthService instance.
    """

    return AuthService()