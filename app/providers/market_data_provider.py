"""
Market Data Provider

Responsible for fetching market data from Yahoo Finance.
"""

import yfinance as yf
import pandas as pd

from app.models.history_models import PriceCandle, StockHistory
from app.logger import logger
from app.models.dashboard_models import IndexData, WatchlistItem
from app.models.stock_models import StockDetails
from app.utils.dashboard_constants import INDEX_NAMES


class MarketDataProvider:

    def _normalize_symbol(self, symbol: str) -> str:
        symbol = symbol.upper().strip()

        if symbol.startswith("^"):
            return symbol

        if symbol.endswith(".NS") or symbol.endswith(".BO"):
            return symbol

        return f"{symbol}.NS"

    def _get_ticker(self, symbol: str,) -> yf.Ticker:
        """
        Returns a Yahoo Finance ticker object.
        """
        symbol = self._normalize_symbol(symbol)
        
        return yf.Ticker(symbol)
    
    def _get_value(self, *values):
        for value in values:
            if value is not None:
                return value

        return None

    def _calculate_change(
        self,
        current_price: float | None,
        previous_close: float | None,
    ) -> tuple[float | None, float | None]:
        """
        Calculate price change and percentage change.
        """

        if (
            current_price is None
            or previous_close in (None, 0)
        ):
            return None, None

        change = round(
            current_price - previous_close,
            2,
        )

        change_percent = round(
            (change / previous_close) * 100,
            2,
        )

        return change, change_percent
    
    def _extract_ceo(self, info: dict) -> str | None:
        """
        Extract CEO name from Yahoo Finance company officers.
        """

        officers = info.get("companyOfficers")

        if not officers:
            return None

        for officer in officers:

            title = (officer.get("title") or "").lower()

            if (
                "chief executive" in title
                or title == "ceo"
            ):
                return officer.get("name")

        return None

    def get_stock_data(self, symbol: str) -> WatchlistItem | None:
        """
        Fetch live market data for a stock.
        """

        try:
            ticker = self._get_ticker(symbol)

            logger.debug("Fetching Yahoo Finance data for %s", symbol)

            info = ticker.info

            logger.debug("Yahoo Finance response received for %s", symbol)

            try:
                fast_info = ticker.fast_info
            except Exception:
                logger.warning("Unable to load fast_info for %s", symbol)
                fast_info = {}

            if not info:
                return None

            current_price = self._get_value(
                fast_info.get("lastPrice")
                or info.get("currentPrice")
                or info.get("regularMarketPrice")
            )

            previous_close = (
                fast_info.get("previousClose")
                or info.get("previousClose")
            )
            
            day_high = (
                fast_info.get("dayHigh")
                or info.get("dayHigh")
            )
            
            day_low = (
                fast_info.get("dayLow")
                or info.get("dayLow")
            )
            
            volume = (
                fast_info.get("lastVolume")
                or info.get("volume")
            )

            change, change_percent = self._calculate_change(
                current_price,
                previous_close,
            )

            return WatchlistItem(
                symbol=symbol,

                company_name=info.get("shortName"),

                exchange=info.get("fullExchangeName"),

                currency=info.get("currency"),

                sector=info.get("sector"),

                industry=info.get("industry"),

                website=info.get("website"),

                current_price=current_price,

                previous_close=previous_close,

                day_high=day_high,

                day_low=day_low,

                fifty_two_week_high=info.get("fiftyTwoWeekHigh"),

                fifty_two_week_low=info.get("fiftyTwoWeekLow"),

                volume=volume,

                market_cap=info.get("marketCap"),

                change=change,

                change_percent=change_percent,
            )

        except Exception:
            logger.exception(
                "Failed to fetch market data | Symbol=%s",
                symbol,
            )
            return None
        

    def get_stock_details(self, symbol: str) -> StockDetails | None:
        """
        Fetch complete stock details from Yahoo Finance.
        """

        try:

            ticker = self._get_ticker(symbol)

            logger.debug(
                "Fetching stock details | Symbol=%s",
                symbol,
            )

            info = ticker.info

            try:
                fast_info = ticker.fast_info
            except Exception:
                fast_info = {}

            if not info:
                return None

            current_price = self._get_value(
                fast_info.get("lastPrice"),
                info.get("currentPrice"),
                info.get("regularMarketPrice"),
            )

            previous_close = self._get_value(
                fast_info.get("previousClose"),
                info.get("previousClose"),
            )

            day_high = self._get_value(
                fast_info.get("dayHigh"),
                info.get("dayHigh"),
            )

            day_low = self._get_value(
                fast_info.get("dayLow"),
                info.get("dayLow"),
            )

            volume = self._get_value(
                fast_info.get("lastVolume"),
                info.get("volume"),
            )

            change, change_percent = self._calculate_change(
                current_price,
                previous_close,
            )

            return StockDetails(

                symbol=symbol,

                company_name=self._get_value(
                    info.get("longName"),
                    info.get("shortName"),
                ),

                exchange=self._get_value(
                    info.get("fullExchangeName"),
                    info.get("exchange"),
                ),

                currency=info.get("currency"),

                sector=info.get("sector"),

                industry=info.get("industry"),

                website=info.get("website"),

                summary=info.get("longBusinessSummary"),

                current_price=current_price,

                previous_close=previous_close,

                day_high=day_high,

                day_low=day_low,

                fifty_two_week_high=info.get("fiftyTwoWeekHigh"),

                fifty_two_week_low=info.get("fiftyTwoWeekLow"),

                volume=volume,

                market_cap=info.get("marketCap"),

                change=change,

                change_percent=change_percent,

                pe_ratio=info.get("trailingPE"),

                eps=info.get("trailingEps"),

                book_value=info.get("bookValue"),

                dividend_yield=info.get("dividendYield"),

                beta=info.get("beta"),

                employee_count=info.get("fullTimeEmployees"),

                country=info.get("country"),

                ceo=self._extract_ceo(info),
            )
        

        except Exception:

            logger.exception(
                "Failed to fetch stock details | Symbol=%s",
                symbol,
            )

            return None

    def get_multiple_stocks(self, symbols: list[str]) -> list[WatchlistItem]:
        """
        Fetch market data for multiple stocks.
        """

        stocks: list[WatchlistItem] = []

        for symbol in symbols:

            stock = self.get_stock_data(symbol)

            if stock:
                stocks.append(stock)

        return stocks

    def get_indices(self, symbols: list[str]) -> list[IndexData]:
        """
        Fetch market index data.
        """

        indices: list[IndexData] = []

        for symbol in symbols:

            stock = self.get_stock_data(symbol)

            if stock:

                indices.append(
                    IndexData(
                        symbol=symbol,
                        index_name=stock.company_name or INDEX_NAMES.get(symbol),
                        exchange=stock.exchange,
                        current_price=stock.current_price,
                        previous_close=stock.previous_close,
                        change=stock.change,
                        change_percent=stock.change_percent,
                    )
                )

        return indices
    
    def get_stock_history(
        self,
        symbol: str,
        period: str = "1y",
        interval: str = "1d",
        ) -> StockHistory | None:
        """
        Fetch historical OHLC data.
        """

        try:

            ticker = self._get_ticker(symbol)

            history = ticker.history(
                period=period,
                interval=interval,
                auto_adjust=False,
            )

            if history.empty:
                return None

            prices: list[PriceCandle] = []

            for index, row in history.iterrows():

                prices.append(
                    PriceCandle(
                        date=index.date(),
                        open=round(float(row["Open"]), 2),
                        high=round(float(row["High"]), 2),
                        low=round(float(row["Low"]), 2),
                        close=round(float(row["Close"]), 2),
                        volume=int(row["Volume"]),
                    )
                )

            return StockHistory(
                symbol=symbol.upper(),
                period=period,
                interval=interval,
                prices=prices,
            )

        except Exception:

            logger.exception(
                "Failed to fetch history | Symbol=%s",
                symbol,
            )

            return None
        
    def get_history_dataframe(
    self,
    symbol: str,
    period: str,
    interval: str,
    ) -> pd.DataFrame | None:
        """
        Fetch historical stock data as a DataFrame.
        """
    
        try:
        
            ticker = self._get_ticker(symbol)
    
            history = ticker.history(
                period=period,
                interval=interval,
                auto_adjust=False,
            )
    
            if history.empty:
                return None
    
            return history
    
        except Exception:
        
            logger.exception(
                "Failed to fetch history dataframe | Symbol=%s",
                symbol,
            )
    
            return None