import streamlit as st


FEATURE_CARD_STYLE = """
background-color:#1E1E2F;
border:1px solid #30363D;
border-radius:16px;
padding:24px;
min-height:220px;
transition:all 0.2s ease;
"""


def metric_card(title: str, value: str, delta: str | None = None) -> None:
    """
    Display a metric card.
    """
    with st.container(border=True):
        st.metric(
            label=title,
            value=value,
            delta=delta,
        )


def feature_card(icon: str, title: str, description: str):

    st.markdown(
        f"""
### {icon} {title}

{description}
"""
    )