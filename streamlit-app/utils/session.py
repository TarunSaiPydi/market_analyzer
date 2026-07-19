import streamlit as st

from utils.constants import *


DEFAULT_SESSION_STATE = {
    # Navigation
    "page": LANDING,

    # Authentication
    "authenticated": False,
    "token": None,
    "user": {},

    # Stocks
    "selected_stock": None,
    "chart_period": DEFAULT_PERIOD,

    # Dashboard
    "watchlist": [],
    "recent_searches": [],

    # Theme
    "theme": DEFAULT_THEME,
}


def initialize_session() -> None:
    """
    Initialize Streamlit session state.
    """

    for key, value in DEFAULT_SESSION_STATE.items():
        st.session_state.setdefault(key, value)


def login_user(token: str, user: dict) -> None:
    """
    Store authenticated user session.
    """

    st.session_state.update({
        "authenticated": True,
        "token": token,
        "user": user,
        "page": DASHBOARD,
    })


def logout_user():
    st.session_state.update({
        "authenticated": False,
        "token": None,
        "user": {},
        "page": LANDING,
        "selected_stock": None,
    })