import streamlit as st


def go_to(page):
    print(f"Navigating to: {page}")  # Debug

    st.session_state["page"] = page

    st.rerun()


def is_authenticated():

    return st.session_state.get(
        "authenticated",
        False,
    )


def current_user():

    return st.session_state.get(
        "user",
        {},
    )
