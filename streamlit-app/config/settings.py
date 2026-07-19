import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "http://127.0.0.1:8000",
)

API_TIMEOUT = 30

PAGE_TITLE = "Market Analyzer"

PAGE_ICON = "📈"

LAYOUT = "wide"