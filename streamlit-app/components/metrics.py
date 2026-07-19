import streamlit as st

from utils.formatters import format_currency, format_percentage, format_volume


def metric_card(
    label: str,
    value,
    delta=None,
    *,
    help: str | None = None,
) -> None:
    """
    Render a standard metric card.
    """

    display_value = "--"

    if value is not None:
        display_value = str(value)

    display_delta = None

    if delta is not None:
        display_delta = str(delta)

    st.metric(
        label=label,
        value=display_value,
        delta=display_delta,
        help=help,
        width="stretch",
    )


def currency_metric(
    label: str,
    value: float | None,
    delta: float | None = None,
) -> None:
    """
    Render a currency metric.
    """

    if value is None:
        metric_card(label, "--")
        return

    delta_text = None

    if delta is not None:
        delta_text = format_percentage(delta)

    st.metric(
        label,
        f"₹{value:,.2f}",
        delta=delta_text,
        width="stretch",
    )


def percentage_metric(
    label: str,
    value: float | None,
) -> None:
    """
    Render a percentage metric.
    """

    if value is None:
        metric_card(label, "--")
        return

    st.metric(
        label,
        format_percentage(value),
        width="stretch",
    )


def number_metric(
    label: str,
    value: int | float | None,
) -> None:
    """
    Render a formatted numeric metric.
    """

    if value is None:
        metric_card(label, "--")
        return

    st.metric(
        label,
        format_volume(value),
        width="stretch",
    )