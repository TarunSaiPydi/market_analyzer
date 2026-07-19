"""
Technical Indicator Models
"""

from pydantic import BaseModel


class MovingAverage(BaseModel):
    sma20: float | None = None
    sma50: float | None = None
    ema20: float | None = None
    ema50: float | None = None


class RSI(BaseModel):
    value: float | None = None


class MACD(BaseModel):
    macd: float | None = None
    signal: float | None = None
    histogram: float | None = None


class BollingerBands(BaseModel):
    upper: float | None = None
    middle: float | None = None
    lower: float | None = None


class TechnicalIndicators(BaseModel):
    symbol: str
    moving_average: MovingAverage
    rsi: RSI
    macd: MACD
    bollinger_bands: BollingerBands