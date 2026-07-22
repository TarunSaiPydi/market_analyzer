import streamlit as st

from api.stocks import history, stock_details

from api.watchlist import add_watchlist
from components.company_information import (
    render_company_information,
)
from components.financial_metrics import (
    render_financial_metrics,
)
from components.footer import render_footer
from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.stock_chart import render_stock_chart
from components.stock_header import render_stock_header
from components.stock_metrics import render_stock_metrics
from components.summary import render_summary

from utils.constants import LOGIN, STOCK_SEARCH
from utils.helpers import go_to, is_authenticated


def render() -> None:
    """
    Render the Stock Details screen.
    """

    # --------------------------------------------------
    # Authentication
    # --------------------------------------------------

    if not is_authenticated():
        st.warning("Please login first.")
        go_to(LOGIN)
        return

    render_sidebar()
    render_navbar()

    symbol = st.session_state.get("selected_stock")

    if not symbol:
        st.warning("No stock selected.")
        go_to(STOCK_SEARCH)
        return

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------
    # Top Navigation Buttons
    # --------------------------------------------------

    left, right = st.columns([1, 5])

    with left:
        if st.button(
            "← Back",
            width="stretch",
        ):
            go_to(STOCK_SEARCH)
            return

    with right:
        # Fixed button layout logic & tied it to your add_watchlist function
        if st.button(
            "⭐ Watchlist",
            key=f"add_watchlist_{symbol}", # Unique key prevents widget runtime conflicts
            use_container_width=True,       # Fixed the width parameter bug
        ):
            with st.spinner("Adding stock to watchlist..."):
                response = add_watchlist(symbol)
            
            # Check if your API responds with a success status string
            if response.get("status") == "success":
                st.success(f"Added {symbol} to your watchlist!")
            else:
                st.error(response.get("message", f"Could not add {symbol}."))
            
            st.rerun()

    st.divider()

    # --------------------------------------------------
    # Chart Configuration
    # --------------------------------------------------

    period = st.session_state.get(
        "chart_period",
        "5d",
    )

    interval = "1d"

    # --------------------------------------------------
    # Fetch Data
    # --------------------------------------------------

    with st.spinner("Loading stock details..."):

        stock_response = stock_details(symbol)

        if stock_response["status"] != "success":
            st.error(
                stock_response.get(
                    "message",
                    "Unable to fetch stock details.",
                )
            )
            render_footer()
            return

        history_response = history(
            symbol=symbol,
            period=period,
            interval=interval,
        )

        if history_response["status"] != "success":
            st.error(
                history_response.get(
                    "message",
                    "Unable to fetch chart data.",
                )
            )
            render_footer()
            return

    stock = stock_response.get("data", {})
    history_data = history_response.get("data", {})

    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    top_left, top_right = st.columns(
        [2.3, 1],
        gap="large",
    )

    with top_left:
        render_stock_header(stock)

    with top_right:
        render_stock_metrics(stock)

    # --------------------------------------------------
    # Chart
    # --------------------------------------------------

    period = st.segmented_control(
        "Chart Period",
        options=[
            "5d",
            "1mo",
            "3mo",
            "6mo",
            "1y",
            "5y",
            "max",
        ],
        default=period,
    )

    st.session_state["chart_period"] = period

    render_stock_chart(history_data)

    st.divider()

    # --------------------------------------------------
    # Key Metrics
    # --------------------------------------------------

    render_financial_metrics(stock)

    st.divider()

    # --------------------------------------------------
    # Company Information
    # --------------------------------------------------

    render_company_information(stock)

    st.divider()

    # --------------------------------------------------
    # Business Summary
    # --------------------------------------------------

    render_summary(stock)

    render_footer()