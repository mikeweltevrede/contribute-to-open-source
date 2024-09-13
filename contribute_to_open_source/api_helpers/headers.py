from __future__ import annotations

import os


def construct_github_header(token: str | None = None, accepted_format: str = "json") -> dict[str, str]:
    """Construct GitHub API header.

    Construct the header for calls to the GitHub API, version 3. We specify the applications and the output format
    that are accepted.

    :param token: GitHub Personal Access Token. If not provided, try to get from the "GITHUB_TOKEN" environment
        variable. If it is not provided in there, do not add authorization to the header.
    :param accepted_format: Accepted output format. Defaults to "json".
    :return: Header for GitHub API call.
    """
    headers = {"Accept": f"application/vnd.github.v3+{accepted_format}"}

    token: str | None = token or os.getenv("GITHUB_TOKEN")
    if token:
        # If there is no token provided, and it is not found in the environment variable GITHUB_TOKEN, then
        # we should not add the "Authorization" header to our request
        headers["Authorization"] = token

    return headers
