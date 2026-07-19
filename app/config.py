from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    # ---------------- Application ---------------- #

    APP_NAME: str = "Market Analyzer"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # ---------------- Server ---------------- #

    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # ---------------- Database ---------------- #

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # ---------------- JWT ---------------- #

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()


if __name__ == "__main__":
    print(settings.model_dump())
    print(settings.JWT_SECRET_KEY)
    print(settings.JWT_ALGORITHM)
    print(settings.ACCESS_TOKEN_EXPIRE_MINUTES)