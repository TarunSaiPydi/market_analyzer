class DatabaseConnectionError(Exception):
    """Raised when database connection cannot be established."""


class DatabaseOperationError(Exception):
    """Raised when a database operation fails."""