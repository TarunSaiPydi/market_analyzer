"""
Custom authentication exceptions.
"""


class AuthenticationError(Exception):
    """Raised when user authentication fails."""


class UserAlreadyExistsError(Exception):
    """Raised when attempting to register an existing user."""