import streamlit as st

from api.dashboard import get_dashboard

from components.footer import render_footer
from components.metrics import (
    currency_metric,
    number_metric,
)
from components.navbar import render_navbar
from components.news_section import render_news_section
from components.sidebar import render_sidebar
from components.watchlist_table import render_watchlist_table

from utils.constants import LOGIN
from utils.helpers import go_to, is_authenticated


def render() -> None:
    """
    Render the dashboard screen.
    """

    if not is_authenticated():
        st.warning("Please login first.")
        go_to(LOGIN)
        return

    render_sidebar()
    render_navbar()

    st.title("📊 Dashboard")
    st.caption("Your AI-powered investment dashboard")

    with st.spinner("Loading dashboard..."):
        response = get_dashboard()

    if response["status"] != "success":
        st.error(
            response.get(
                "message",
                "Unable to load dashboard.",
            )
        )
        return

    dashboard = response["data"]

    # ----------------------------
    # Portfolio Summary
    # ----------------------------

    st.subheader("Overview")

    col1, col2 = st.columns(2)

    with col1:
        number_metric(
            "Watchlist",
            len(dashboard.get("watchlist", [])),
        )

    with col2:
        number_metric(
            "News",
            len(dashboard.get("news", [])),
        )

    st.divider()

    # ----------------------------
    # Market Indices
    # ----------------------------

    st.subheader("Market Indices")

    indices = dashboard.get("indices", [])

    if indices:

        columns = st.columns(len(indices))

        for column, index in zip(columns, indices):

            with column:

                currency_metric(
                    index.get("index_name", "--"),
                    index.get("current_price"),
                    index.get("change_percent"),
                )

    else:
        st.info("No market indices available.")

    st.divider()

    # ----------------------------
    # Watchlist
    # ----------------------------

    st.subheader("Your Watchlist")

    render_watchlist_table(
        dashboard.get("watchlist", []),
    )

    st.divider()

    # ----------------------------
    # News
    # ----------------------------

    render_news_section(
        dashboard.get("news", []),
    )

    render_footer()