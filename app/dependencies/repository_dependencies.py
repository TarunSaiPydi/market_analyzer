from app.repositories.auth_repository import AuthRepository


def get_auth_repository() -> AuthRepository:
    return AuthRepository()