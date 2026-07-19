import streamlit as st

from components.news_card import render_news_card


def render_news_section(news: list[dict]) -> None:
    """
    Render the market news section.
    """

    st.subheader("📰 Latest Market News")

    if not news:

        st.info(
            "No news articles available."
        )

        return

    for index, article in enumerate(news):
        read_more = render_news_card(article, index)

        if read_more:

            url = article.get("url")

            if url:
                st.link_button(
                    "Open Article",
                    url,
                    width="stretch",
                )

        st.write("")