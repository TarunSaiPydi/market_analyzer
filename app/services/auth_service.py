"""
Authentication Service

Contains all business logic related to
user registration and authentication.
"""

from app.security.jwt_handler import JWTService
from app.config import settings
from app.exceptions.auth_exceptions import AuthenticationError
from app.models.request_models import SignupRequest, LoginRequest
from app.repositories.auth_repository import AuthRepository
from app.security.bcrypt_utils import generate_password_hash, verify_password_hash
from app.utils.constants import INVALID_CREDENTIALS, LOGIN_SUCCESS, SIGNUP_SUCCESS
from app.utils.response_builders import success
from app.logger import logger


class AuthService:

    def __init__(self):
        self.repository = AuthRepository()

    def signup(self, credentials: SignupRequest) -> dict:

        username = credentials.user_name.strip()

        logger.info(
            "User registration started | Username=%s",
            username
        )

        if not username:
            raise AuthenticationError("Username cannot be empty.")

        email = credentials.email_id.strip().lower()

        password_hash = generate_password_hash(
            credentials.password
        )

        user = self.repository.create_user(
            username=username,
            email=email,
            password_hash=password_hash
        )

        logger.info(
            "User registered successfully | UserId=%s | Username=%s",
            user["id"],
            username
        )

        return success(
            message=SIGNUP_SUCCESS,
            data={
                "id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "created_at": str(user["created_at"])
            }
        )

    def login(self, credentials: LoginRequest, client_ip: str) -> dict:

        username = credentials.user_name.strip()

        logger.info(
            "Authentication started | Username=%s",
            username
        )

        user = self.repository.get_user_by_username(
            username
        )

        if user is None:

            logger.warning(
                "Authentication failed | Username=%s | Reason=User not found",
                username
            )

            raise AuthenticationError(INVALID_CREDENTIALS)

        password_verified = verify_password_hash(
            credentials.password,
            user["hash_password"]
        )

        if not password_verified:

            logger.warning(
                "Authentication failed | Username=%s | Reason=Invalid password",
                username
            )

            raise AuthenticationError(INVALID_CREDENTIALS)

        login_record = self.repository.save_login_audit(
            user_id=user["id"],
            client_ip=client_ip
        )

        access_token = JWTService.create_access_token(
            {
                "sub": str(user["id"]),
                "username": user["username"]
            }
        )

        logger.info(
            "Authentication successful | UserId=%s | Username=%s",
            user["id"],
            username
        )

        return success(
            message=LOGIN_SUCCESS,
            data={
                "access_token": access_token,
                "token_type": "Bearer",
                "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
                "user": {
                    "id": user["id"],
                    "username": user["username"]
                },
                "login_timestamp": str(login_record["last_login"])
            }
        )
    