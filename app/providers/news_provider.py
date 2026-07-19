"""
News Provider

Responsible for fetching stock related news.
"""

import yfinance as yf

from app.logger import logger
from app.models.dashboard_models import NewsItem


class NewsProvider:

    def get_news(self, symbol: str) -> NewsItem | None:

        try:
            news = yf.Ticker(symbol).news

            if not news:
                return None

            article = news[0]["content"]

            thumbnail = None

            thumbnail_data = article.get("thumbnail")

            if isinstance(thumbnail_data, dict):
                thumbnail = thumbnail_data.get("originalUrl")

            canonicalUrl = None

            canonicalUrl_data = article.get("canonicalUrl")

            if isinstance(canonicalUrl_data, dict):
                canonicalUrl = canonicalUrl_data.get("originalUrl")

            return NewsItem(
                title=article.get("title"),
                summary=article.get("summary"),
                published_date=article.get("pubDate"),
                display_time=article.get("displayTime"),
                thumbnail=thumbnail,
                url=canonicalUrl,
            )

        except Exception:
            logger.exception(
                "Failed to fetch news | Symbol=%s",
                symbol,
            )

            return None

    def get_news_for_symbols(self, symbols: list[str]) -> list[NewsItem]:

        articles: list[NewsItem] = []

        for symbol in symbols:

            article = self.get_news(symbol)

            if article:
                articles.append(article)

        return articles