from api.client import api_client


DASHBOARD_ENDPOINT = "/sma/v1/dashboard"


def get_dashboard() -> dict:
    """
    Fetch dashboard data.
    """

    return api_client.get(
        DASHBOARD_ENDPOINT,
    )