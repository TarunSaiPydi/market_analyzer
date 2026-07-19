import streamlit as st


def primary_button(
    label: str,
    key: str | None = None,
    *,
    width: str = "stretch",
    disabled: bool = False,
    help: str | None = None,
) -> bool:
    """
    Render a primary action button.
    """

    return st.button(
        label,
        key=key,
        type="primary",
        width=width,
        disabled=disabled,
        help=help,
    )


def secondary_button(
    label: str,
    key: str | None = None,
    *,
    width: str = "stretch",
    disabled: bool = False,
    help: str | None = None,
) -> bool:
    """
    Render a secondary action button.
    """

    return st.button(
        label,
        key=key,
        width=width,
        disabled=disabled,
        help=help,
    )


def icon_button(
    icon: str,
    label: str,
    key: str | None = None,
    *,
    width: str = "stretch",
    type: str = "secondary",
    disabled: bool = False,
) -> bool:
    """
    Render a button with an icon.
    """

    return st.button(
        f"{icon} {label}",
        key=key,
        width=width,
        type=type,
        disabled=disabled,
    )