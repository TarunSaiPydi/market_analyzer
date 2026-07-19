"""
Watchlist Repository

Responsible only for database operations.
"""

from psycopg2.extras import RealDictCursor

from app.database.connection import get_connection, release_connection
from app.exceptions.database_exceptions import DatabaseConnectionError, DatabaseOperationError
from app.logger import logger


class WatchlistRepository:

    def add_watchlist(self, user_id: int, symbol: str) -> dict:

        conn = get_connection()

        if conn is None:
            raise DatabaseConnectionError("Unable to connect to database.")

        try:

            with conn.cursor(
                cursor_factory=RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    INSERT INTO watchlist(user_id, symbol)
                    VALUES (%s, %s)
                    RETURNING
                        id,
                        user_id,
                        symbol,
                        created_at;
                    """,
                    (user_id, symbol)
                )

                watchlist = cursor.fetchone()

                conn.commit()

                return watchlist

        except Exception as ex:

            logger.exception(
                "Database error while adding watchlist | UserId=%s Symbol=%s",
                user_id,
                symbol,
            )

            conn.rollback()

            raise DatabaseOperationError(str(ex))

        finally:

            release_connection(conn)

    def get_watchlist(self, user_id: int) -> list[dict]:

        conn = get_connection()

        if conn is None:
            raise DatabaseConnectionError(
                "Unable to connect to database."
            )

        try:

            with conn.cursor(
                cursor_factory=RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT
                        id,
                        symbol,
                        created_at
                    FROM watchlist
                    WHERE user_id=%s
                    ORDER BY created_at DESC;
                    """,
                    (user_id,)
                )

                return cursor.fetchall()

        except Exception as ex:

            logger.exception(
                "Database error while retrieving watchlist | UserId=%s",
                user_id,
            )

            raise DatabaseOperationError(str(ex))

        finally:

            release_connection(conn)

    def remove_watchlist(self, user_id: int, symbol: str) -> bool:

        conn = get_connection()

        if conn is None:
            raise DatabaseConnectionError(
                "Unable to connect to database."
            )

        try:

            with conn.cursor() as cursor:

                cursor.execute(
                    """
                    DELETE FROM watchlist
                    WHERE user_id=%s
                    AND symbol=%s;
                    """,
                    (
                        user_id,
                        symbol,
                    )
                )

                deleted = cursor.rowcount > 0

                conn.commit()

                return deleted

        except Exception as ex:

            logger.exception(
                "Database error while deleting watchlist | UserId=%s Symbol=%s",
                user_id,
                symbol,
            )

            conn.rollback()

            raise DatabaseOperationError(str(ex))

        finally:

            release_connection(conn)