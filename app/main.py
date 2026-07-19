from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter

from app.api.auth_controller import router as auth_router
from app.api.watchlist_controller import router as watchlist_router
from app.api.dashboard_controller import router as dashboard_router
from app.api.search_controller import router as search_router
from app.api.stock_controller import router as stock_router
from app.exceptions.exceptions_handlers import register_exception_handlers
from app.database.connection import close_connection_pool, create_connection_pool
from app.middleware.request_logger import RequestLoggingMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_connection_pool()

    yield

    close_connection_pool()

app = FastAPI(
    title="Market Analyzer API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(RequestLoggingMiddleware)

register_exception_handlers(app)

app.include_router(auth_router)
app.include_router(watchlist_router)
app.include_router(dashboard_router)
app.include_router(search_router)
app.include_router(stock_router)

router = APIRouter()


