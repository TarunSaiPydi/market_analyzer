import streamlit as st

from api.auth import signup
from components.topbar import render_topbar
from utils.constants import DASHBOARD, LANDING, LOGIN
from utils.helpers import go_to, is_authenticated


def render() -> None:
    """
    Render the signup screen.
    """

    # Redirect authenticated users
    if is_authenticated():
        go_to(DASHBOARD)
        return

    render_topbar()

    _, center, _ = st.columns([1.5, 2, 1.5])

    with center:

        st.title("📝 Create Account")
        st.caption(
            "Create your Market Analyzer account."
        )

        with st.form("signup_form"):

            username = st.text_input(
                "Username",
                placeholder="Choose a username",
            )

            email = st.text_input(
                "Email",
                placeholder="Enter your email",
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Create a password",
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                placeholder="Confirm your password",
            )

            submitted = st.form_submit_button(
                "Create Account",
                type="primary",
                width="stretch",
            )

            if submitted:

                if not username.strip():
                    st.error("Username is required.")
                    return

                if not email.strip():
                    st.error("Email is required.")
                    return

                if not password:
                    st.error("Password is required.")
                    return

                if password != confirm_password:
                    st.error("Passwords do not match.")
                    return

                with st.spinner("Creating your account..."):

                    response = signup(
                        username=username.strip(),
                        email=email.strip(),
                        password=password,
                    )

                if response["status"] == "success":

                    st.success(
                        "Account created successfully!"
                    )

                    st.info(
                        "Please sign in with your new account."
                    )

                    go_to(LOGIN)

                st.error(
                    response.get(
                        "message",
                        "Unable to create account.",
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
                "Go to Login",
                width="stretch",
            ):
                
                go_to(LOGIN)