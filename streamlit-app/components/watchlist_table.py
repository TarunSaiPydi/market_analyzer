import streamlit as st

from api.watchlist import delete_watchlist

from components.watchlist_card import render_watchlist_card

from utils.constants import STOCK_DETAILS
from utils.helpers import go_to


def render_watchlist_table(
    watchlist: list[dict],
) -> None:
    """
    Render the user's watchlist.
    """

    if not watchlist:
        st.info("Your watchlist is empty.")
        return

    st.caption(
        f"{len(watchlist)} stock(s) in your watchlist"
    )

    for stock in watchlist:

        view_clicked, remove_clicked = render_watchlist_card(
            stock
        )

        if view_clicked:

            st.session_state["selected_stock"] = stock.get(
                "symbol"
            )

            go_to(STOCK_DETAILS)
            return

        if remove_clicked:

            symbol = stock.get("symbol")

            with st.spinner("Removing stock..."):

                response = delete_watchlist(symbol)

            if response.get("status") == "success":

                st.success(
                    f"{symbol} removed from watchlist."
                )

                st.rerun()

            else:

                st.error(
                    response.get(
                        "message",
                        "Unable to remove stock.",
                    )
                )