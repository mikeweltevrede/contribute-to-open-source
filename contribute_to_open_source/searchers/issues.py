from __future__ import annotations

from typing import Any


def generate_github_api_query(**kwargs: Any) -> str:
    """Generate query with filters to retrieve issues with.

    Filters should match those for the GitHub API.

    :param kwargs: Keyword arguments, the following are allowed:
        - language: Programming languages to consider.
    :return: Query with filters.
    """
    query = ""

    languages = kwargs.get("languages")

    query += f"language:{','.join(languages)}"

    return query
