import streamlit as st

from utils.formatters import format_currency, format_market_cap, format_percentage


def render_stock_search_card(stock: dict) -> bool:
    """
    Render a stock search result card.

    Parameters
    ----------
    stock : dict
        Stock information returned from the backend.

    Returns
    -------
    bool
        True if the user clicks the View Details button,
        otherwise False.
    """

    symbol = stock.get("symbol", "--")
    company = stock.get("company_name", "--")
    exchange = stock.get("exchange", "--")
    series = stock.get("series", "--")
    sector = stock.get("sector", "--")
    current_price = stock.get("current_price")
    change_percent = stock.get("change_percent")
    market_cap = stock.get("market_cap")

    with st.container(border=True):

        header_col, price_col = st.columns([5, 2])

        with header_col:

            st.subheader(symbol)

            st.write(company)

            st.caption(f"{exchange} • {series}")

        with price_col:

            if current_price is not None:

                delta = None

                if change_percent is not None:
                    delta = format_percentage(change_percent)

                st.metric(
                    label="Current Price",
                    value=format_currency(current_price),
                    delta=delta,
                )

        st.divider()


        return st.button(
            "View Details",
            key=f"view_{symbol}",
            width="stretch",
            type="primary",
        )