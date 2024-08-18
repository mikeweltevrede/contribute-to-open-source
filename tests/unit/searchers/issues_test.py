from __future__ import annotations

import pytest
from contribute_to_open_source.searchers import issues


class TestGenerateGithubApiQuery:
    def test_languages_for_single_element_is_added_to_query(self):
        expected = "language:python"
        params = issues.QueryParameters(languages=["python"])

        assert issues.generate_github_api_query(params) == expected

    @pytest.mark.xfail(reason="Currently no support for multiple languages")
    def test_languages_for_multiple_elements_is_added_to_query(self):
        expected = "language:python OR language:java"
        params = issues.QueryParameters(languages=["python", "java"])

        assert issues.generate_github_api_query(params) == expected
