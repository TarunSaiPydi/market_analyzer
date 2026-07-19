import streamlit as st
import plotly.graph_objects as go


def render_line_chart(
    x,
    y,
    *,
    title: str,
    x_title: str = "",
    y_title: str = "",
    color: str = "#2962FF",
) -> None:
    """
    Render a reusable Plotly line chart.
    """

    if not x or not y:
        st.info("No chart data available.")
        return

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            line=dict(width=2, color=color),
            name=title,
        )
    )

    fig.update_layout(
        title=title,
        template="plotly_dark",
        xaxis_title=x_title,
        yaxis_title=y_title,
        height=450,
        margin=dict(l=20, r=20, t=60, b=20),
        hovermode="x unified",
        showlegend=False,
    )

    st.plotly_chart(
        fig,
        width="stretch",
        config={
            "displaylogo": False,
            "responsive": True,
            "modeBarButtonsToRemove": [
                "lasso2d",
                "select2d",
            ],
        },
    )


def render_volume_chart(
    x,
    volume,
) -> None:
    """
    Render a stock volume chart.
    """

    if not x or not volume:
        st.info("No volume data available.")
        return

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=x,
            y=volume,
            name="Volume",
        )
    )

    fig.update_layout(
        title="Trading Volume",
        template="plotly_dark",
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False,
    )

    st.plotly_chart(
        fig,
        width="stretch",
        config={"displaylogo": False},
    )