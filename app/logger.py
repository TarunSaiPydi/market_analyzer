"""
Centralized logging configuration for the application.

This module configures:
1. Console logging
2. Rotating file logging
3. Common log format
"""

import logging
import os
from logging.handlers import RotatingFileHandler

# ------------------------------------------------------------------
# Log Directory
# ------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIRECTORY = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIRECTORY, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIRECTORY, "application.log")


# ------------------------------------------------------------------
# Log Formatter
# ------------------------------------------------------------------

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)

formatter = logging.Formatter(LOG_FORMAT)


# ------------------------------------------------------------------
# Root Logger
# ------------------------------------------------------------------

logger = logging.getLogger("MarketAnalyzer")

logger.setLevel(logging.INFO)

logger.propagate = False


# Prevent duplicate handlers
if not logger.handlers:

    # --------------------------------------------------------------
    # Console Handler
    # --------------------------------------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)

    console_handler.setFormatter(formatter)


    # --------------------------------------------------------------
    # Rotating File Handler
    # --------------------------------------------------------------

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,   # 5 MB
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setLevel(logging.INFO)

    file_handler.setFormatter(formatter)


    logger.addHandler(console_handler)

    logger.addHandler(file_handler)