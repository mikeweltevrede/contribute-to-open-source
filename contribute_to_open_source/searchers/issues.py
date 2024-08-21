from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class QueryParameters:
    """Parameters for GitHub API search."""

    languages: list[str] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)
    states: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Post-initialization, doing data validation."""
        # Currently do not support more than one element in the fields. However, for backwards compatibility's sake,
        # we do define the fields as a list and do validation in post-init.
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
