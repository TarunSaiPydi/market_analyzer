import streamlit as st
from utils.helpers import current_user, go_to
from utils.constants import *


def render_topbar(show_auth_buttons: bool = True):

    user = current_user()

    left, middle, right = st.columns([6, 2, 2])

    with left:

        st.markdown(
            """
            <h2 style="margin-bottom:0">
                📈 Market Analyzer
            </h2>
            """,
            unsafe_allow_html=True,
        )

        st.caption("Professional Stock Analytics")

    if show_auth_buttons:

        with middle:

            if st.button(
                "Login",
                width="stretch",
                key="login_button",
            ):
                go_to(LOGIN)

        with right:

            if st.button(
                "Sign Up",
                width="stretch",
                type="primary",
                key="signup_button",
            ):
                go_to(SIGNUP)

    else:

        with middle:

            st.markdown("### 👋 Welcome")

            if user:
                st.caption(
                    user.get(
                        "user_name",
                        "Guest",
                    )
                )

        with right:

            if st.button(
                "🚪 Logout",
                width="stretch",
                type="secondary",
            ):
                from utils.session import logout_user

                logout_user()
                st.rerun()

    st.divider()