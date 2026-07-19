"""
Global Exception Handlers
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.auth_exceptions import AuthenticationError, UserAlreadyExistsError
from app.exceptions.database_exceptions import DatabaseConnectionError, DatabaseOperationError
from app.logger import logger
from app.utils.constants import STATUS_ERROR, INTERNAL_SERVER_ERROR
from app.utils.response_builders import error


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(AuthenticationError)
    async def authentication_exception_handler(
        request: Request,
        exc: AuthenticationError
    ):

        logger.warning(
            "Authentication failed | %s",
            str(exc)
        )

        return JSONResponse(
            status_code=401,
            content=error(message=str(exc))
        )

    @app.exception_handler(UserAlreadyExistsError)
    async def user_exists_exception_handler(
        request: Request,
        exc: UserAlreadyExistsError
    ):

        logger.warning(str(exc))

        return JSONResponse(
            status_code=409,
            content=error(message=str(exc))
        )

    @app.exception_handler(DatabaseConnectionError)
    async def database_connection_handler(
        request: Request,
        exc: DatabaseConnectionError
    ):

        logger.error(str(exc))

        return JSONResponse(
            status_code=503,
            content=error(message=str(exc))
        )

    @app.exception_handler(DatabaseOperationError)
    async def database_operation_handler(
        request: Request,
        exc: DatabaseOperationError
    ):

        logger.exception(str(exc))

        return JSONResponse(
            status_code=500,
            content=error(message=str(exc))
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request,
        exc: Exception
    ):

        logger.exception(
            "Unhandled exception"
        )

        return JSONResponse(
            status_code=500,
            content=error(message=str(exc))
        )