import streamlit as st
from datetime import datetime

from utils.constants import APP_NAME


def render_footer() -> None:
    """
    Render the application footer.
    """

    current_year = datetime.now().year

    st.divider()

    left, center, right = st.columns([3, 2, 3])

    with left:
        st.caption(
            f"© {current_year} {APP_NAME}"
        )

    with center:
        st.caption(
            "Built with ❤️ using Streamlit"
        )

    with right:
        st.caption(
            "Data provided by Yahoo Finance"
        )