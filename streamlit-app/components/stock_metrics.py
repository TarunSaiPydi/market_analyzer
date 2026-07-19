import streamlit as st

from utils.formatters import format_currency


def render_stock_metrics(stock: dict) -> None:
    """
    Render the stock price summary card.
    """

    if not stock:
        st.warning("Stock data unavailable.")
        return

    current_price = stock.get("current_price")
    change = stock.get("change", 0)
    change_percent = stock.get("change_percent", 0)
    exchange = stock.get("exchange", "--")

    price = (
        format_currency(current_price)
        if current_price is not None
        else "--"
    )

    positive = change >= 0
    delta = f"{change:.2f} ({change_percent:.2f}%)"

    if not positive:
        delta = f"-{abs(change):.2f} ({abs(change_percent):.2f}%)"

    with st.container(border=True):

        st.metric(
            label="Current Price",
            value=price,
            delta=delta,
        )

        st.caption(exchange)