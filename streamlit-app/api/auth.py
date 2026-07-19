from api.client import api_client


LOGIN_ENDPOINT = "/sma/v1/login"
SIGNUP_ENDPOINT = "/sma/v1/signup"
PROFILE_ENDPOINT = "/sma/v1/me"


def login(username: str, password: str) -> dict:
    """
    Authenticate a user.
    """

    payload = {
        "user_name": username,
        "password": password,
    }

    return api_client.post(
        LOGIN_ENDPOINT,
        payload,
    )


def signup(
    username: str,
    email: str,
    password: str,
) -> dict:
    """
    Register a new user.
    """

    payload = {
        "user_name": username,
        "email_id": email,
        "password": password,
    }

    return api_client.post(
        SIGNUP_ENDPOINT,
        payload,
    )


def get_current_user() -> dict:
    """
    Fetch currently logged-in user.
    """

    return api_client.get(
        PROFILE_ENDPOINT,
    )