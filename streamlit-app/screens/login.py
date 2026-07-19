import streamlit as st

from api.auth import login
from components.topbar import render_topbar
from utils.constants import DASHBOARD, LANDING, SIGNUP
from utils.helpers import go_to, is_authenticated
from utils.session import login_user


def render() -> None:
    """
    Render the login screen.
    """

    if is_authenticated():
        go_to(DASHBOARD)
        return

    render_topbar()

    _, center, _ = st.columns([1.5, 2, 1.5])

    with center:

        st.title("🔐 Welcome Back")
        st.caption(
            "Sign in to continue to Market Analyzer."
        )

        with st.form("login_form", clear_on_submit=False):

            username = st.text_input(
                "Username",
                placeholder="Enter your username",
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password",
            )

            submitted = st.form_submit_button(
                "Sign In",
                type="primary",
                width="stretch",
            )

            if submitted:

                if not username.strip():
                    st.error("Please enter your username.")
                    return

                if not password:
                    st.error("Please enter your password.")
                    return

                with st.spinner("Signing you in..."):

                    response = login(
                        username=username.strip(),
                        password=password,
                    )

                if response["status"] == "success":

                    data = response["data"]

                    login_user(
                        token=data["access_token"],
                        user=data["user"],
                    )

                    st.success("Login successful.")
                    st.rerun()

                st.error(
                    response.get(
                        "message",
                        "Invalid username or password.",
                    )
                )

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "← Back",
                width="stretch",
            ):
                go_to(LANDING)

        with col2:

            if st.button(
                "Create Account",
                width="stretch",
            ):
                go_to(SIGNUP)