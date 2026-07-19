import streamlit as st

from config.settings import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
)

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

from utils.constants import LANDING
from utils.session import initialize_session

initialize_session()

from styles.theme import load_theme

load_theme()

from config.routes import ROUTES

page = st.session_state.get(
    "page",
    LANDING,
)

ROUTES[page]()