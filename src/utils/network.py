from typing import Optional

import requests


def make_request(
    url: str,
    method: str = "GET",
    headers: Optional[dict] = None,
    params: Optional[dict] = None,
    data: Optional[dict] = None,
    token: Optional[str] = None,
) -> dict:
    """
    Makes a network request to the specified URL.

    :param url: URL to which the request is made.
    :param method: HTTP method (e.g., 'GET', 'POST').
    :param headers: Optional HTTP headers.
    :param params: Optional query parameters for 'GET' requests.
    :param data: Optional body data for 'POST' requests.
    :param token: Optional GitHub token for authentication.
    :return: A dictionary with the response data.
    """
    try:
        if headers is None:
            headers = {}
        headers["Accept"] = "application/vnd.github.v3+json"
        if token:
            headers["Authorization"] = f"token {token}"

        response = requests.request(method=method, url=url, headers=headers, params=params, json=data)

        # Check if the response was successful
        response.raise_for_status()

        # Return JSON response if available, else return empty dict
        return response.json() if response.text else {}
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return {}


def get_github_api(url: str, params: Optional[dict] = None, token: Optional[str] = None) -> dict:
    """
    Convenience function for making GET requests to the GitHub API.

    :param url: The GitHub API URL.
    :param params: Optional query parameters.
    :param token: Optional GitHub token for authentication.
    :return: A dictionary with the API response.
    """
    return make_request(url, method="GET", params=params, token=token)
