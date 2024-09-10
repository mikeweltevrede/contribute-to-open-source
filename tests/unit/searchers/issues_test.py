from __future__ import annotations

from unittest import mock

import pytest
from contribute_to_open_source.searchers import issues


class TestQueryParameters:
    def test_when_languages_not_provided_set_to_empty_list(self):
        assert issues.QueryParameters().languages == []

    def test_when_labels_not_provided_set_to_empty_list(self):
        assert issues.QueryParameters().labels == []

    def test_when_states_not_provided_set_to_empty_list(self):
        assert issues.QueryParameters().states == []

    def test_raises_NotImplementedError_if_more_than_one_elt_for_languages(self):
        with pytest.raises(NotImplementedError, match="Currently no support for multiple languages"):
            issues.QueryParameters(languages=["python", "java"])

    def test_raises_NotImplementedError_if_more_than_one_elt_for_labels(self):
        with pytest.raises(NotImplementedError, match="Currently no support for multiple labels"):
            issues.QueryParameters(labels=["good-first-issue", "help wanted"])

    def test_raises_NotImplementedError_if_more_than_one_elt_for_states(self):
        with pytest.raises(NotImplementedError, match="Currently no support for multiple states"):
            issues.QueryParameters(states=["open", "closed"])

    def test_raises_NotImplementedError_if_more_than_one_elt_for_languages_and_labels(self):
        with pytest.raises(NotImplementedError, match="Currently no support for multiple languages,labels"):
            issues.QueryParameters(languages=["python", "java"], labels=["good-first-issue", "help wanted"])


class TestGenerateGithubApiQuery:
    def test_languages_for_single_element_is_added_to_query(self):
        expected = 'language:"python"'
        params = issues.QueryParameters(languages=["python"])

        assert issues.generate_github_api_query(params) == expected

    @pytest.mark.xfail(reason="Currently no support for multiple languages")
    def test_languages_for_multiple_elements_is_added_to_query(self):
        expected = 'language:"python" OR language:"java"'
        params = issues.QueryParameters(languages=["python", "java"])

        assert issues.generate_github_api_query(params) == expected

    def test_when_languages_not_provided_do_not_add_to_query(self):
        params = issues.QueryParameters()
        assert "language:" not in issues.generate_github_api_query(params)

    def test_labels_for_single_element_is_added_to_query(self):
        expected = 'label:"good-first-issue"'
        params = issues.QueryParameters(labels=["good-first-issue"])

        assert issues.generate_github_api_query(params) == expected

    @pytest.mark.xfail(reason="Currently no support for multiple labels")
    def test_labels_for_multiple_elements_is_added_to_query(self):
        expected = 'label:"good-first-issue" OR label:"help wanted"'
        params = issues.QueryParameters(languages=["good-first-issue", "help wanted"])

        assert issues.generate_github_api_query(params) == expected

    def test_when_labels_not_provided_do_not_add_to_query(self):
        params = issues.QueryParameters()
        assert "label:" not in issues.generate_github_api_query(params)

    def test_states_for_single_element_is_added_to_query(self):
        expected = 'state:"open"'
        params = issues.QueryParameters(states=["open"])

        assert issues.generate_github_api_query(params) == expected

    @pytest.mark.xfail(reason="Currently no support for multiple states")
    def test_states_for_multiple_elements_is_added_to_query(self):
        expected = 'state:"open" OR state:"closed"'
        params = issues.QueryParameters(states=["open", "closed"])

        assert issues.generate_github_api_query(params) == expected

    def test_when_states_not_provided_do_not_add_to_query(self):
        params = issues.QueryParameters()
        assert "state:" not in issues.generate_github_api_query(params)


@mock.patch("contribute_to_open_source.searchers.issues.requests.get")
class TestSearchIssues:
    def test_request_is_made_to_github_api(self, mock_get):
        github_api_url = "https://api.github.com/search/issues"
        params = issues.QueryParameters()

        issues.search_issues(params)

        mock_get.assert_called_once_with(github_api_url, params=mock.ANY, headers=mock.ANY, timeout=mock.ANY)
