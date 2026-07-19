import streamlit as st


def _format_value(value):
    """Return a display-friendly value."""

    if value is None:
        return "--"

    if isinstance(value, str):
        value = value.strip()
        if not value:
            return "--"

    return value


def _info_card(title: str, value):
    """Render a single information card."""

    value = _format_value(value)

    with st.container(border=True):
        st.caption(title)
        st.markdown(
            f"""
            <div style="
                font-size:16px;
                font-weight:600;
                margin-top:4px;
                margin-bottom:2px;
            ">
                {value}
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_company_information(stock: dict) -> None:
    """
    Render company information section.
    """

    if not stock:
        st.warning("Company information is unavailable.")
        return

    st.subheader("🏢 Company Information")

    left, right = st.columns(2, gap="large")

    # ---------------- Left Column ---------------- #

    with left:

        _info_card(
            "Company",
            stock.get("company_name"),
        )

        _info_card(
            "Symbol",
            stock.get("symbol"),
        )

        _info_card(
            "Exchange",
            stock.get("exchange"),
        )

        _info_card(
            "Sector",
            stock.get("sector"),
        )

        _info_card(
            "Industry",
            stock.get("industry"),
        )

    # ---------------- Right Column ---------------- #

    with right:

        _info_card(
            "Country",
            stock.get("country"),
        )

        _info_card(
            "Currency",
            stock.get("currency"),
        )

        website = _format_value(
            stock.get("website")
        )

        with st.container(border=True):
            st.caption("Website")

            if website != "--":
                st.link_button(
                    "🌐 Visit Website",
                    website,
                    use_container_width=True,
                )
            else:
                st.markdown("**--**")

        _info_card(
            "Market State",
            stock.get("market_state"),
        )

        _info_card(
            "Timezone",
            stock.get("timezone"),
        )