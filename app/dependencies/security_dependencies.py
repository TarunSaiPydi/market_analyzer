from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.repositories.auth_repository import AuthRepository
from app.exceptions.auth_exceptions import AuthenticationError
from app.security.jwt_handler import JWTService
from app.dependencies.repository_dependencies import get_auth_repository

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    repository: AuthRepository = Depends(get_auth_repository)
) -> dict:
    """
    Returns the authenticated user.
    """

    token = credentials.credentials

    payload = JWTService.verify_access_token(token)

    user_id = payload.get("sub")

    if not user_id:
        raise AuthenticationError("Invalid access token.")

    user = repository.get_user_by_id(int(user_id))

    if user is None:
        raise AuthenticationError("User not found.")

    return user