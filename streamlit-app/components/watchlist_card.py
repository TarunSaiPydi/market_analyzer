import streamlit as st

from utils.formatters import (
    format_currency,
    format_percentage,
)


def render_watchlist_card(
    stock: dict,
) -> tuple[bool, bool]:
    """
    Render a watchlist stock card.

    Returns
    -------
    (view_clicked, remove_clicked)
    """

    symbol = stock.get("symbol", "--")

    company = stock.get(
        "company_name",
        "Unknown Company",
    )

    exchange = stock.get(
        "exchange",
        "--",
    )

    sector = stock.get(
        "sector",
        "--",
    )

    price = stock.get("current_price")

    change = stock.get("change_percent")

    with st.container(border=True):

        left, right = st.columns(
            [4, 1.5],
            gap="large",
        )

        with left:

            st.subheader(symbol)

            st.write(company)

            info = []

            if exchange:
                info.append(exchange)

            if sector:
                info.append(sector)

            if info:
                st.caption(" • ".join(info))

        with right:

            if price is not None:

                delta = None

                if change is not None:
                    delta = format_percentage(change)

                st.metric(
                    "Price",
                    format_currency(price),
                    delta=delta,
                )

        col1, col2 = st.columns(2)

        with col1:

            view_clicked = st.button(
                "📈 View Details",
                key=f"view_{symbol}",
                use_container_width=True,
                type="primary",
            )

        with col2:

            remove_clicked = st.button(
                "🗑 Remove",
                key=f"remove_{symbol}",
                use_container_width=True,
            )

    return (
        view_clicked,
        remove_clicked,
    )