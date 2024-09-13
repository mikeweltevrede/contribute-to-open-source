from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any

import requests

from contribute_to_open_source.api_helpers.headers import construct_github_header


@dataclass
class QueryParameters:
    """Parameters for GitHub API search."""

    languages: list[str] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)
    states: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Post-initialization, doing data validation."""
        # TODO(mike): Currently do not support more than one element in the fields. However, for backwards
        #  compatibility's sake, we do define the fields as a list and do validation in post-init.
        # https://github.com/mikeweltevrede/contribute-to-open-source/issues/9
        multi_elt_fields = [attr for attr, value in self.__dict__.items() if len(value) > 1]

        if multi_elt_fields:
            raise NotImplementedError(f"Currently no support for multiple {','.join(multi_elt_fields)}")


def generate_github_api_query(query_params: QueryParameters) -> str:
    """Generate query with filters to retrieve issues with.

    Filters should match those for the GitHub API.

    :param query_params: Query parameters.
    :return: Query with filters.
    """
    query = ""
    query += " OR ".join(f'language:"{lang}"' for lang in query_params.languages)
    query += " OR ".join(f'label:"{label}"' for label in query_params.labels)
    query += " OR ".join(f'state:"{state}"' for state in query_params.states)

    return query


def search_issues(query_params: QueryParameters, token: str | None = None) -> dict[str, Any]:
    """Search GitHub issues according to the query parameters.

    :param query_params: Query parameters to GitHub's issue API.
    :param token: GitHub Personal Access Token. If not provided, try to get from the "GITHUB_TOKEN" environment
        variable. If it is not provided in there, do not add authorization to the header.
    :return: JSON return value from the request to the issue API.
    """
    github_api_url = "https://api.github.com/search/issues"
    headers = construct_github_header(token=token)

    params: dict[str, str | int] = {
        "q": generate_github_api_query(query_params=query_params),
        "sort": "created",
        "order": "desc",
        # TODO(mike): Un-hardcode these, probably in a pagination dataclass or general params dataclass
        # https://github.com/mikeweltevrede/contribute-to-open-source/issues/7
        "page": 1,
        "per_page": 100,
    }

    github_response = requests.get(github_api_url, params=params, headers=headers, timeout=60)
    return github_response.json()


if __name__ == "__main__":
    import pathlib
    from pprint import pprint

    from dotenv import load_dotenv

    load_dotenv(pathlib.Path.home() / ".env")

    query_params = QueryParameters(languages=["python"], labels=["good first issue"], states=["open"])
    response = search_issues(query_params=query_params, token=os.environ["GITHUB_TOKEN"])

    pprint(response)
