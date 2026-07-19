import streamlit as st

from api.search import search_stocks

from components.footer import render_footer
from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.stock_search_card import (
    render_stock_search_card,
)
from utils.constants import LOGIN, STOCK_DETAILS
from utils.helpers import go_to, is_authenticated


def render() -> None:
    """
    Render the stock search screen.
    """

    if not is_authenticated():
        st.warning("Please login first.")
        go_to(LOGIN)

    render_sidebar()
    render_navbar()

    st.title("🔍 Stock Search")
    st.caption(
        "Search stocks by company name or ticker symbol."
    )

    query = st.text_input(
        "Search Stocks",
        placeholder="Example: TCS, Infosys, Reliance",
        key="stock_search",
    ).strip()

    if not query:
        st.info("Search for any NSE/BSE listed company.")
        render_footer()
        return

    if len(query) < 2:
        st.warning(
            "Please enter at least 2 characters."
        )
        render_footer()
        return

    with st.spinner("Searching stocks..."):
        response = search_stocks(query)

    if response["status"] != "success":
        st.error(
            response.get(
                "message",
                "Unable to search stocks.",
            )
        )
        render_footer()
        return

    stocks = response.get(
        "data",
        {},
    ).get(
        "stocks",
        [],
    )

    if not stocks:
        st.info("No matching stocks found.")
        render_footer()
        return

    st.success(
        f"Found {len(stocks)} matching stock(s)."
    )

    for stock in stocks:

        view_clicked = render_stock_search_card(
            stock
        )

        if view_clicked:

            st.session_state["selected_stock"] = (
                stock["symbol"]
            )

            go_to(STOCK_DETAILS)

    render_footer()