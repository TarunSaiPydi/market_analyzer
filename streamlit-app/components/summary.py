import streamlit as st


def render_summary(stock: dict) -> None:
    """
    Render the company business summary section.
    """

    if not stock:
        return

    summary = (
        stock.get("summary")
        or stock.get("business_summary")
        or stock.get("long_business_summary")
        or "Business summary is not available."
    )

    with st.container(border=True):

        st.subheader("🏢 Business Summary")

        st.markdown(
            """
            <style>
            .summary-text{
                font-size:16px;
                line-height:1.8;
                text-align:justify;
                color:#CBD5E1;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="summary-text">
                {summary}
            </div>
            """,
            unsafe_allow_html=True,
        )