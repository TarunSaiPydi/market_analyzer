"""
HTTP Request Logging Middleware
"""

import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.logger import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        request_id = str(uuid.uuid4())

        request.state.request_id = request_id

        start_time = time.perf_counter()

        client_ip = (
            request.client.host
            if request.client
            else "Unknown"
        )

        logger.info(
            "[%s] Incoming Request | Method=%s | Path=%s | ClientIP=%s",
            request_id,
            request.method,
            request.url.path,
            client_ip,
        )

        response = await call_next(request)

        execution_time = (
            time.perf_counter() - start_time
        ) * 1000

        logger.info(
            "[%s] Request Completed | Method=%s | Path=%s | Status=%s | Duration=%.2f ms",
            request_id,
            request.method,
            request.url.path,
            response.status_code,
            execution_time,
        )

        response.headers["X-Request-ID"] = request_id

        return response