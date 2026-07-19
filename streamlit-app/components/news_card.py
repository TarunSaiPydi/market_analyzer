import streamlit as st


def render_news_card(article: dict, index: int) -> bool:
    """
    Render a single news article.

    Parameters
    ----------
    article : dict
        News article information.

    Returns
    -------
    bool
        True if the Read More button is clicked.
    """

    title = article.get("title", "Untitled")
    summary = article.get("summary", "No summary available.")
    source = article.get("source", "Unknown Source")
    published = article.get("published_date", "")
    url = article.get("url", "")

    with st.container(border=True):

        st.subheader(f"📰 {title}")

        st.write(summary)

        info = []

        if source:
            info.append(source)

        if published:
            info.append(published)

        if info:
            st.caption(" • ".join(info))

        read_more = st.button(
            "Read More",
            key=f"news_{index}_{title}",
            type="primary",
            width="stretch",
        )

    return read_more