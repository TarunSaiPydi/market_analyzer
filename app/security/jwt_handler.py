"""
JWT Utility

Provides helper methods for
JWT token generation and validation.
"""

from datetime import datetime, timedelta, timezone
from typing import Any
from jose import JWTError, jwt

from app.config import settings
from app.logger import logger
from app.exceptions.auth_exceptions import AuthenticationError

class JWTService:

    @staticmethod
    def create_access_token(data: dict[str, Any]) -> str:
        """
        Create a signed JWT access token.
        """

        payload = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        payload.update(
            {
                "exp": expire
            }
        )

        token = jwt.encode(
            payload,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM
        )

        logger.info(
            "JWT access token generated successfully."
        )

        return token
    
    @staticmethod
    def verify_access_token(token: str) -> dict[str, Any]:
        """
        Verify and decode a JWT access token.

        Args:
            token: JWT token.

        Returns:
            Decoded JWT payload.

        Raises:
            AuthenticationError: If the token is invalid or expired.
        """

        try:

            payload = jwt.decode(
                token,
                settings.JWT_SECRET_KEY,
                algorithms=[settings.JWT_ALGORITHM]
            )

            logger.info(
                "JWT token verified successfully."
            )

            return payload

        except JWTError as ex:

            logger.warning(
                "JWT verification failed."
            )

            raise AuthenticationError(
                "Invalid or expired access token."
            ) from ex
    