import streamlit as st

from components.footer import render_footer
from components.navbar import render_navbar
from components.sidebar import render_sidebar
from utils.constants import APP_NAME, LOGIN
from utils.helpers import current_user, go_to, is_authenticated
from utils.session import logout_user


def render() -> None:
    """
    Render the settings screen.
    """

    if not is_authenticated():
        st.warning("Please login first.")
        go_to(LOGIN)

    render_sidebar()
    render_navbar()

    st.title("⚙ Settings")
    st.caption("Manage your account and application preferences.")

    user = current_user()

    # ---------------------------------
    # Profile
    # ---------------------------------

    st.subheader("👤 Profile")

    col1, col2 = st.columns(2)

    with col1:
        st.text_input(
            "Username",
            value=user.get("user_name", ""),
            disabled=True,
        )

    with col2:
        st.text_input(
            "Email",
            value=user.get("email_id", ""),
            disabled=True,
        )

    st.divider()

    # ---------------------------------
    # Chart Preferences
    # ---------------------------------

    st.subheader("📈 Chart Preferences")

    periods = [
        "5d",
        "1mo",
        "3mo",
        "6mo",
        "1y",
        "5y",
        "max",
    ]

    selected_period = st.selectbox(
        "Default Chart Period",
        periods,
        index=periods.index(
            st.session_state.get(
                "chart_period",
                "5d",
            )
        ),
    )

    st.session_state["chart_period"] = selected_period

    st.divider()

    # ---------------------------------
    # Theme
    # ---------------------------------

    st.subheader("🎨 Appearance")

    theme = st.radio(
        "Theme",
        [
            "Dark",
            "Light",
        ],
        horizontal=True,
        index=0,
    )

    st.caption(
        f"Current theme: {theme}"
    )

    st.divider()

    # ---------------------------------
    # About
    # ---------------------------------

    st.subheader("ℹ About")

    st.write(f"**Application:** {APP_NAME}")

    st.write("**Version:** 1.0.0")

    st.write("**Backend:** FastAPI")

    st.write("**Frontend:** Streamlit")

    st.write("**Data Source:** Yahoo Finance")

    st.divider()

    # ---------------------------------
    # Logout
    # ---------------------------------

    st.subheader("🔒 Session")

    if st.button(
        "Logout",
        type="primary",
        width="stretch",
    ):

        logout_user()

    render_footer()