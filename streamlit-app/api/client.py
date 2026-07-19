import requests
import streamlit as st
from utils.logger import logger

from config.settings import API_BASE_URL, API_TIMEOUT


class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL.rstrip("/")

    def _headers(self):
        headers = {
            "Content-Type": "application/json",
        }

        token = st.session_state.get("token")

        if token:
            headers["Authorization"] = f"Bearer {token}"

        return headers

    def _handle_response(self, response: requests.Response):
        """
        Parse the HTTP response and return a dictionary.
        """

        try:
            response.raise_for_status()
            return response.json()

        except requests.HTTPError:
            try:
                error = response.json()
            except ValueError:
                error = {
                    "message": response.text
                }

            return {
                "status": "error",
                "message": error.get(
                    "message",
                    f"HTTP {response.status_code}"
                ),
                "status_code": response.status_code,
            }

        except ValueError:
            return {
                "status": "error",
                "message": "Invalid JSON response from server.",
            }

    def get(self, endpoint: str, params=None):

        try:
            logger.info("GET %s", endpoint)
            response = requests.get(
                f"{self.base_url}{endpoint}",
                headers=self._headers(),
                params=params,
                timeout=API_TIMEOUT,
            )

            return self._handle_response(response)

        except requests.RequestException as e:
            logger.exception("API request failed")
            return {
                "status": "error",
                "message": str(e),
            }

    def post(self, endpoint: str, data=None):

        try:
            logger.info("POST %s", endpoint)
            response = requests.post(
                f"{self.base_url}{endpoint}",
                headers=self._headers(),
                json=data,
                timeout=30,
            )

            return self._handle_response(response)

        except requests.RequestException as e:
            logger.exception("API request failed")
            return {
                "status": "error",
                "message": str(e),
            }

    def delete(self, endpoint: str):

        try:
            logger.info("DELETE %s", endpoint)
            response = requests.delete(
                f"{self.base_url}{endpoint}",
                headers=self._headers(),
                timeout=30,
            )

            return self._handle_response(response)

        except requests.RequestException as e:
            logger.exception("API request failed")
            return {
                "status": "error",
                "message": str(e),
            }


api_client = APIClient()