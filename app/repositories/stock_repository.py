"""
Stock Repository

Responsible for stock database operations.
"""

from psycopg2.extras import RealDictCursor

from app.database.connection import get_connection, release_connection
from app.exceptions.database_exceptions import DatabaseConnectionError, DatabaseOperationError
from app.logger import logger


class StockRepository:

    def get_stock_by_symbol(self, symbol: str) -> dict | None:

        conn = get_connection()

        if conn is None:
            raise DatabaseConnectionError(
                "Unable to connect to database."
            )

        try:

            with conn.cursor(cursor_factory=RealDictCursor) as cursor:

                cursor.execute(
                    """
                    SELECT
                        symbol,
                        company_name,
                        exchange,
                        series,
                        isin,
                        sector,
                        industry,
                        currency,
                        country
                    FROM stocks
                    WHERE symbol = %s
                    AND is_active = TRUE;
                    """,
                    (symbol.upper(),),
                )

                return cursor.fetchone()

        except Exception as ex:

            logger.exception(
                "Database error while retrieving stock | Symbol=%s",
                symbol,
            )

            raise DatabaseOperationError(str(ex))

        finally:

            release_connection(conn)