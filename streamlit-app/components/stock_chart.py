import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def render_stock_chart(history: dict) -> None:
    """
    Render a professional candlestick chart for stock history.
    """

    if not history:
        st.warning("Historical data not found.")
        return

    prices = history.get("prices", [])

    if not prices:
        st.info("No historical price data available.")
        return

    df = pd.DataFrame(prices)

    required_columns = [
        "date",
        "open",
        "high",
        "low",
        "close",
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        st.error(
            f"Missing required columns: {', '.join(missing_columns)}"
        )
        return

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    with st.container(border=True):

        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader("📈 Price History")

        with col2:
            st.caption(
                f"{history.get('period', '')} • {history.get('interval', '')}"
            )

        figure = go.Figure()

        figure.add_trace(
            go.Candlestick(
                x=df["date"],
                open=df["open"],
                high=df["high"],
                low=df["low"],
                close=df["close"],
                name=history.get("symbol", "Stock"),
                increasing_line_color="#22C55E",
                decreasing_line_color="#EF4444",
                increasing_fillcolor="#22C55E",
                decreasing_fillcolor="#EF4444",
                hovertemplate=(
                    "<b>%{x}</b><br>"
                    "Open : ₹%{open:,.2f}<br>"
                    "High : ₹%{high:,.2f}<br>"
                    "Low : ₹%{low:,.2f}<br>"
                    "Close : ₹%{close:,.2f}"
                    "<extra></extra>"
                ),
            )
        )

        figure.update_layout(
            template="plotly_dark",
            height=550,
            margin=dict(
                l=10,
                r=10,
                t=10,
                b=10,
            ),
            paper_bgcolor="#0F172A",
            plot_bgcolor="#0F172A",
            hovermode="x unified",
            showlegend=False,
            dragmode="zoom",
        )

        figure.update_xaxes(
            title=None,
            showgrid=False,
            showline=True,
            linecolor="#334155",
            rangeslider_visible=False,
            tickfont=dict(size=11),
        )

        figure.update_yaxes(
            title=None,
            showgrid=True,
            gridcolor="#1E293B",
            showline=True,
            linecolor="#334155",
            zeroline=False,
            tickprefix="₹",
            tickformat=",.2f",
        )

        st.plotly_chart(
            figure,
            use_container_width=True,
            config={
                "displaylogo": False,
                "responsive": True,
                "scrollZoom": True,
                "displayModeBar": True,
                "modeBarButtonsToRemove": [
                    "lasso2d",
                    "select2d",
                    "autoScale2d",
                    "resetScale2d",
                ],
            },
        )