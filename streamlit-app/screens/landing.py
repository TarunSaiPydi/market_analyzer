import streamlit as st

from components.cards import (
    feature_card,
    metric_card,
)

from components.buttons import primary_button
from components.topbar import render_topbar
from utils.constants import *
from utils.helpers import go_to, is_authenticated


def render():
    if is_authenticated():
        render_topbar(False)
    else:
        render_topbar(True)
    if st.session_state.get("authenticated", False):
        go_to(DASHBOARD)
        return

    st.title("📈 Market Analyzer")

    st.subheader(
        "AI-Powered Stock Market Analytics Platform"
    )

    st.write(
        """
Analyze stocks, monitor your portfolio,
discover opportunities,
and make smarter investment decisions.
"""
    )

    col1, col2 = st.columns(2)

    with col1:
        if primary_button("Login", "login"):
            go_to(LOGIN)

    with col2:
        if primary_button("Sign Up", "signup"):
            go_to(SIGNUP)

    st.divider()

    st.header("Features")

    cols = st.columns(4)

    with cols[0]:
        feature_card(
            "📊",
            "Market Dashboard",
            "Monitor the latest market trends.",
        )

    with cols[1]:
        feature_card(
            "📈",
            "Technical Analysis",
            "Professional stock analysis.",
        )

    with cols[2]:
        feature_card(
            "🤖",
            "AI Insights",
            "AI-driven market intelligence.",
        )

    with cols[3]:
        feature_card(
            "⭐",
            "Watchlist",
            "Track your favorite stocks.",
        )

    st.divider()

    st.header("Platform Statistics")

    stats = st.columns(4)

    with stats[0]:
        metric_card("Stocks", "5000+")

    with stats[1]:
        metric_card("Accuracy", "98%")

    with stats[2]:
        metric_card("Live Data", "24/7")

    with stats[3]:
        metric_card("Users", "100K+")