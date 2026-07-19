from datetime import datetime


def format_currency(value):

    if value is None:
        return "--"

    return f"₹{value:,.2f}"


def format_percentage(value):

    if value is None:
        return "--"

    return f"{value:.2f}%"


def format_volume(value):

    if value is None:
        return "--"

    return f"{value:,}"


def format_market_cap(value):

    if value is None:
        return "--"

    if value >= 1_00_00_00_00_000:
        return f"₹{value/1_00_00_00_00_000:.2f} L Cr"

    if value >= 1_00_00_00_000:
        return f"₹{value/1_00_00_00_000:.2f} Cr"

    return format_currency(value)


def format_date(value):

    if not value:
        return "--"

    if isinstance(value, datetime):
        return value.strftime("%d %b %Y")

    return str(value)