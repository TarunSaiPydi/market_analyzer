import streamlit as st

from utils.helpers import current_user


def render_navbar() -> None:
    """
    Render the top navigation bar.
    """

    user = current_user()

    username = (
        user.get("username")
        or user.get("user_name")
        or "Guest"
    )

    left, middle, right = st.columns([6, 1, 2])

    with left:

        st.markdown(
            """
            ## 📈 Market Analyzer
            """
        )

        st.caption(
            f"Welcome back, **{username}** 👋"
        )

    with middle:

        st.button(
            "🔔",
            disabled=True,
            help="Notifications coming soon.",
            width="stretch",
        )

    with right:

        st.info(f"👤 {username}")

    st.divider()