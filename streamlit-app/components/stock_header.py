import streamlit as st


def render_stock_header(stock: dict) -> None:
    """
    Render the company header.

    This component only renders the company information.
    Pricing information is rendered by stock_metrics.py.
    """

    company = stock.get(
        "company_name",
        "Unknown Company",
    )

    symbol = stock.get(
        "symbol",
        "--",
    )

    exchange = stock.get(
        "exchange",
        "--",
    )

    sector = stock.get(
        "sector",
    )

    industry = stock.get(
        "industry",
    )

    details = [symbol, exchange]

    if sector:
        details.append(sector)

    if industry:
        details.append(industry)

    with st.container(border=True):

        st.markdown(
            f"""
## {company}
"""
        )

        st.caption(" • ".join(details))