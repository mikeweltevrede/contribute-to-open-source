from __future__ import annotations

from contribute_to_open_source.searchers import issues


class TestGenerateGithubApiQuery:
    def test_languages_for_single_element_is_added_to_query(self):
        expected = "language:python"
        params = issues.QueryParameters(languages=["python"])

        assert issues.generate_github_api_query(params) == expected
