import streamlit as st

from api.stocks import stock_details
from api.watchlist import get_watchlist

from components.footer import render_footer
from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.watchlist_table import render_watchlist_table

from utils.constants import LOGIN
from utils.helpers import go_to, is_authenticated


def render() -> None:
    """
    Render the user's watchlist.
    """

    if not is_authenticated():
        st.warning("Please login first.")
        go_to(LOGIN)
        return

    render_sidebar()
    render_navbar()

    st.title("⭐ My Watchlist")
    st.caption("Track your favorite stocks.")

    with st.spinner("Loading watchlist..."):
        response = get_watchlist()

    if response.get("status") != "success":
        st.error(
            response.get(
                "message",
                "Unable to load watchlist.",
            )
        )
        render_footer()
        return

    data = response.get("data", {})

    items = data.get("items", [])

    if not items:
        st.info("Your watchlist is empty.")
        render_footer()
        return

    watchlist = []

    with st.spinner("Loading stock details..."):

        for item in items:

            symbol = item.get("symbol")

            if not symbol:
                continue

            stock_response = stock_details(symbol)

            if stock_response.get("status") == "success":
                watchlist.append(stock_response.get("data", {}))

    render_watchlist_table(watchlist)

    render_footer()