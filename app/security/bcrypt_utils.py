"""
Password hashing utilities.

This module provides helper functions for:
- Password hashing
- Password verification
"""

import bcrypt

from app.logger import logger


BCRYPT_ROUNDS = 12


def generate_password_hash(password: str) -> str:
    """
    Generate a bcrypt hash for the given password.

    Args:
        password: Plain text password.

    Returns:
        Secure bcrypt hashed password.
    """

    try:

        password_bytes = password.encode("utf-8")

        salt = bcrypt.gensalt(rounds=BCRYPT_ROUNDS)

        hashed_password = bcrypt.hashpw(
            password_bytes,
            salt
        )

        return hashed_password.decode("utf-8")

    except Exception:

        logger.exception(
            "Failed to generate password hash."
        )

        raise


def verify_password_hash(plain_password: str, stored_password_hash: str) -> bool:
    """
    Verify a password against its bcrypt hash.

    Args:
        plain_password: Password entered by the user.
        stored_password_hash: Password hash stored in database.

    Returns:
        True if password matches.
        False otherwise.
    """

    try:

        return bcrypt.checkpw(
            plain_password.encode("utf-8"),
            stored_password_hash.encode("utf-8")
        )

    except Exception:

        logger.exception(
            "Password verification failed."
        )

        raise
