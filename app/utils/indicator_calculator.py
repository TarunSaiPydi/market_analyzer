"""
Indicator Calculator
"""

import pandas as pd


class IndicatorCalculator:
    """
    Utility class for calculating technical indicators.
    """

    @staticmethod
    def calculate_sma(
        data: pd.DataFrame,
        period: int,
    ) -> float | None:
        """
        Calculate Simple Moving Average.
        """

        if len(data) < period:
            return None

        sma = (
            data["Close"]
            .rolling(window=period)
            .mean()
            .iloc[-1]
        )

        return round(float(sma), 2)

    @staticmethod
    def calculate_ema(
        data: pd.DataFrame,
        period: int,
    ) -> float | None:
        """
        Calculate Exponential Moving Average.
        """

        if len(data) < period:
            return None

        ema = (
            data["Close"]
            .ewm(span=period, adjust=False)
            .mean()
            .iloc[-1]
        )

        return round(float(ema), 2)
    
    @staticmethod
    def calculate_rsi(
        data: pd.DataFrame,
        period: int = 14,
    ) -> float | None:
        """
        Calculate Relative Strength Index (RSI).
        """

        if len(data) < period + 1:
            return None

        close = data["Close"]

        delta = close.diff()

        gain = delta.where(delta > 0, 0.0)
        loss = -delta.where(delta < 0, 0.0)

        average_gain = gain.rolling(window=period).mean()
        average_loss = loss.rolling(window=period).mean()

        rs = average_gain / average_loss

        rsi = 100 - (100 / (1 + rs))

        return round(float(rsi.iloc[-1]), 2)
    
    @staticmethod
    def calculate_macd(
    data: pd.DataFrame,
    ) -> tuple[float | None, float | None, float | None]:
        """
        Calculate MACD, Signal Line and Histogram.
        """

        if len(data) < 35:
            return None, None, None

        close = data["Close"]

        ema12 = close.ewm(span=12, adjust=False).mean()
        ema26 = close.ewm(span=26, adjust=False).mean()

        macd_line = ema12 - ema26
        signal_line = macd_line.ewm(span=9, adjust=False).mean()

        histogram = macd_line - signal_line

        return (
            round(float(macd_line.iloc[-1]), 2),
            round(float(signal_line.iloc[-1]), 2),
            round(float(histogram.iloc[-1]), 2),
        )
    
    @staticmethod
    def calculate_bollinger_bands(
        data: pd.DataFrame,
        period: int = 20,
    ) -> tuple[float | None, float | None, float | None]:
        """
        Calculate Bollinger Bands.
        """
    
        if len(data) < period:
            return None, None, None
    
        close = data["Close"]
    
        sma = close.rolling(window=period).mean()
    
        std = close.rolling(window=period).std()
    
        upper = sma + (2 * std)
        lower = sma - (2 * std)
    
        return (
            round(float(upper.iloc[-1]), 2),
            round(float(sma.iloc[-1]), 2),
            round(float(lower.iloc[-1]), 2),
        )