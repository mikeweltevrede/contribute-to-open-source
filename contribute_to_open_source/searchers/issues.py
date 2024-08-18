from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class QueryParameters:
    """Parameters for GitHub API search."""

    languages: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Post-initialization, doing data validation."""
        if len(self.languages) > 1:
            raise NotImplementedError("Currently no support for multiple languages")


def generate_github_api_query(query_params: QueryParameters) -> str:
    """Generate query with filters to retrieve issues with.

    Filters should match those for the GitHub API.

    :param query_params: Query parameters.
    :return: Query with filters.
    """
    query = ""
    query += " OR ".join(f"language:{lang}" for lang in query_params.languages)

    return query
