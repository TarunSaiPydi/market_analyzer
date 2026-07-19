"""
Search Repository

Responsible only for stock search database operations.
"""

from psycopg2.extras import RealDictCursor

from app.database.connection import get_connection, release_connection
from app.exceptions.database_exceptions import DatabaseConnectionError, DatabaseOperationError
from app.logger import logger


class SearchRepository:

    def search_stocks(
        self,
        query: str,
        limit: int = 10,
        offset: int = 0,
    ) -> list[dict]:
        """
        Search stocks by symbol or company name.
        """

        conn = get_connection()

        if conn is None:
            raise DatabaseConnectionError(
                "Unable to connect to database."
            )

        try:

            with conn.cursor(
                cursor_factory=RealDictCursor
            ) as cursor:

                search_term = f"%{query.strip()}%"
                starts_with = f"{query.strip()}%"

                cursor.execute(
                    """
                    SELECT
                        symbol,
                        company_name,
                        exchange,
                        series
                    FROM stocks
                    WHERE
                        is_active = TRUE
                        AND (
                            symbol ILIKE %s
                            OR company_name ILIKE %s
                        )
                    ORDER BY
                        CASE
                            WHEN symbol ILIKE %s THEN 1
                            WHEN company_name ILIKE %s THEN 2
                            ELSE 3
                        END,
                        company_name
                    LIMIT %s
                    OFFSET %s;
                    """,
                    (
                        search_term,
                        search_term,
                        starts_with,
                        starts_with,
                        limit,
                        offset,
                    ),
                )

                return cursor.fetchall()

        except Exception as ex:

            logger.exception(
                "Database error while searching stocks | Query=%s",
                query,
            )

            raise DatabaseOperationError(str(ex))

        finally:

            release_connection(conn)