"""
Database Connection Manager

Responsible for:
- Creating PostgreSQL connection pool
- Providing database connections
- Returning connections back to the pool
"""

from psycopg2 import pool
from psycopg2 import OperationalError

from app.config import settings
from app.logger import logger


connection_pool = None

def create_connection_pool():
    """
    Initialize PostgreSQL connection pool.
    """

    global connection_pool

    try:

        connection_pool = pool.ThreadedConnectionPool(
            minconn=2,
            maxconn=10,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
        )

        logger.info(
            "PostgreSQL connection pool initialized successfully."
        )

    except OperationalError:

        logger.exception(
            "Failed to initialize PostgreSQL connection pool."
        )

        raise


def get_connection():
    """
    Get a database connection from the pool.
    """

    try:

        return connection_pool.getconn()

    except Exception:

        logger.exception(
            "Failed to obtain database connection."
        )

        return None
    
def release_connection(connection):
    """
    Return a database connection to the pool.
    """

    if connection is not None:

        connection_pool.putconn(connection)

def close_connection_pool():
    """
    Close all pooled database connections.
    """

    if connection_pool:

        connection_pool.closeall()

        logger.info(
            "Database connection pool closed."
        )
    