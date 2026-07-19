from pathlib import Path

import streamlit as st


def load_theme() -> None:
    """
    Load the application's global stylesheet.
    """

    css_file = Path(__file__).parent / "style.css"

    with css_file.open(encoding="utf-8") as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True,
        )