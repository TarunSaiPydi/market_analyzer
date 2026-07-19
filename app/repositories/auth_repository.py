"""
Authentication Repository

Responsible only for database operations.
"""

from psycopg2.extras import RealDictCursor

from app.database.connection import get_connection, release_connection
from app.exceptions.database_exceptions import DatabaseOperationError, DatabaseConnectionError
from app.logger import logger

class AuthRepository:

    def create_user(self, username: str, email: str, password_hash: str) -> dict:

        conn = get_connection()

        if conn is None:
            raise DatabaseConnectionError("Unable to connect to database.")

        try:

            with conn.cursor(cursor_factory=RealDictCursor) as cursor:

                cursor.execute(
                    """
                    INSERT INTO user_credentials (username, email, hash_password)
                    VALUES (%s,%s,%s)
                    RETURNING id, username, email, created_at;
                    """,
                    (username, email, password_hash)
                )

                user = cursor.fetchone()

                conn.commit()

                return user

        except Exception as ex:

            logger.exception(
                "Database error while creating user | Username=%s",
                username
            )

            conn.rollback()

            raise DatabaseOperationError(str(ex))

        finally:

            release_connection(conn)

    def get_user_by_username(self, username: str) -> dict:

        conn = get_connection()

        if conn is None:
            raise DatabaseConnectionError("Unable to connect to database.")

        try:

            with conn.cursor(
                cursor_factory=RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT id, username, hash_password
                    FROM user_credentials
                    WHERE username=%s
                    """,
                    (username,)
                )

                return cursor.fetchone()
            
        except Exception as ex:

            logger.exception(
                "Database error while retrieving user | Username=%s",
                username
            )

            raise DatabaseOperationError(str(ex))

        finally:

            release_connection(conn)

    def save_login_audit(self, user_id: int, client_ip: str) -> dict:

        conn = get_connection()

        if conn is None:
            raise DatabaseConnectionError("Unable to connect to database.")

        try:

            with conn.cursor(
                cursor_factory=RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    INSERT INTO users_login_info(user_id, ip_address, status)
                    VALUES(%s, %s, 'success')
                    RETURNING last_login;
                    """,
                    (user_id, client_ip)
                )

                login_info = cursor.fetchone()

                conn.commit()

                return login_info

        except Exception as ex:

            logger.exception(
                "Database error while saving login audit | UserId=%s",
                user_id
            )
            
            conn.rollback()

            raise DatabaseOperationError(str(ex))

        finally:

           release_connection(conn)

    def get_user_by_id(self, user_id: int) -> dict | None:
        """
        Returns user by primary key.
        """
        conn = get_connection()

        if conn is None:
            raise DatabaseConnectionError("Unable to connect to database.")

        try:

            with conn.cursor(
                cursor_factory=RealDictCursor
            ) as cursor:

                cursor.execute(
                    """
                    SELECT id, username, hash_password
                    FROM user_credentials
                    WHERE id=%s
                    """,
                    (user_id,)
                )

                return cursor.fetchone()
            
        except Exception as ex:

            logger.exception(
                "Database error while retrieving user | id=%s",
                user_id
            )

            raise DatabaseOperationError(str(ex))

        finally:

            release_connection(conn)
