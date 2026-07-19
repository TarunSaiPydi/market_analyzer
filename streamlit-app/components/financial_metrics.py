import streamlit as st

from utils.formatters import (
    format_currency,
    format_volume,
)


def metric_card(title: str, value: str) -> None:
    """
    Render a metric card.
    """

    with st.container(border=True):

        st.caption(title)

        st.markdown(
            f"""
            <h3 style="margin-top:0px;">
                {value}
            </h3>
            """,
            unsafe_allow_html=True,
        )


def render_financial_metrics(stock: dict) -> None:
    """
    Render key stock metrics below the chart.
    """

    if not stock:
        st.warning("Metrics unavailable.")
        return

    st.subheader("📊 Key Metrics")

    row1 = st.columns(4)

    with row1[0]:
        metric_card(
            "Previous Close",
            format_currency(
                stock.get("previous_close")
            ),
        )

    with row1[1]:
        metric_card(
            "Day High",
            format_currency(
                stock.get("day_high")
            ),
        )

    with row1[2]:
        metric_card(
            "Day Low",
            format_currency(
                stock.get("day_low")
            ),
        )

    with row1[3]:
        metric_card(
            "Volume",
            format_volume(
                stock.get("volume")
            ),
        )

    row2 = st.columns(4)

    with row2[0]:
        metric_card(
            "52 Week High",
            format_currency(
                stock.get("fifty_two_week_high")
            ),
        )

    with row2[1]:
        metric_card(
            "52 Week Low",
            format_currency(
                stock.get("fifty_two_week_low")
            ),
        )

    with row2[2]:
        metric_card(
            "Market Cap",
            format_volume(
                stock.get("market_cap")
            ),
        )

    with row2[3]:
        metric_card(
            "P/E Ratio",
            stock.get("pe_ratio", "--"),
        )

    row3 = st.columns(4)

    with row3[0]:
        metric_card(
            "EPS",
            stock.get("eps", "--"),
        )

    with row3[1]:
        metric_card(
            "Book Value",
            stock.get("book_value", "--"),
        )

    with row3[2]:
        metric_card(
            "Dividend Yield",
            f"{stock.get('dividend_yield', '--')}%",
        )

    with row3[3]:
        metric_card(
            "Employees",
            format_volume(
                stock.get("employee_count")
            ),
        )