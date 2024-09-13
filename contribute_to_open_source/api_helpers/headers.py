from __future__ import annotations


def construct_github_header(accepted_format: str = "json") -> dict[str, str]:
    """Construct GitHub API header.

    Construct the header for calls to the GitHub API, version 3. We specify the applications and the output format
    that are accepted.

    :param accepted_format: Accepted output format. Defaults to "json".
    :return: Header for GitHub API call.
    """
    return {"Accept": f"application/vnd.github.v3+{accepted_format}"}
