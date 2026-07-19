import streamlit as st

from utils.helpers import current_user, go_to
from utils.session import logout_user
from utils.constants import *


MENU_ITEMS = [
    ("📊", "Dashboard", DASHBOARD),
    ("🔍", "Stock Search", STOCK_SEARCH),
    ("⭐", "Watchlist", WATCHLIST),
    ("⚙", "Settings", SETTINGS),
]


def _navigate(page: str):
    if st.session_state["page"] != page:
        go_to(page)


def render_sidebar():

    user = current_user()

    with st.sidebar:

        st.markdown(
            """
            <h2 style='margin-bottom:0'>
                📈 Market Analyzer
            </h2>
            """,
            unsafe_allow_html=True,
        )

        st.caption("Professional Stock Analytics")

        st.divider()

        if user:

            username = (
                user.get("username")
                or user.get("user_name")
                or "Guest"
            )

            st.write(username)

        current_page = st.session_state.get("page")

        for icon, label, page in MENU_ITEMS:

            button_type = (
                "primary"
                if current_page == page
                else "secondary"
            )

            if st.button(
                f"{icon}  {label}",
                width="stretch",
                type=button_type,
            ):
                _navigate(page)

        st.divider()

        if st.button(
            "🚪 Logout",
            width="stretch",
            type="secondary",
        ):
            logout_user()
            go_to(LANDING)