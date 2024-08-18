from __future__ import annotations

from dataclasses import dataclass


@dataclass
class QueryParameters:
    """Parameters for GitHub API search."""

    languages: list[str] | None = None


def generate_github_api_query(query_params: QueryParameters) -> str:
    """Generate query with filters to retrieve issues with.

    Filters should match those for the GitHub API.

    :param query_params: Query parameters.
    :return: Query with filters.
    """
    query = ""
    query += f"language:{','.join(query_params.languages)}"

    return query
