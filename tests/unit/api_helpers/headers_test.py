from __future__ import annotations

from contribute_to_open_source.api_helpers import headers


class TestConstructGithubHeader:
    def test_format_for_accepted_responses_defaults_to_json(self):
        actual = headers.construct_github_header()

        assert actual["Accept"].endswith("+json")

    def test_format_for_accepted_responses_can_be_provided(self):
        actual = headers.construct_github_header(accepted_format=(fmt := "xml"))

        assert actual["Accept"].endswith(f"+{fmt}")

    def test_response_is_accepted_to_be_from_github_vendor_v3(self):
        actual = headers.construct_github_header()

        assert actual["Accept"].startswith("application/vnd.github.v3+")

    def test_header_uses_authorization_from_token_argument_if_provided(self):
        actual = headers.construct_github_header(token=(token := "test_token_123"))

        assert actual["Authorization"] == token

    def test_header_uses_authorization_from_env_var_GITHUB_TOKEN_if_token_argument_not_provided(self, monkeypatch):
        monkeypatch.setenv("GITHUB_TOKEN", token := "test_token_123")

        actual = headers.construct_github_header()

        assert actual["Authorization"] == token

    def test_when_token_not_provided_and_not_in_env_var_GITHUB_TOKEN_then_do_not_add_Authorization_to_header(
        self, monkeypatch
    ):
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)

        actual = headers.construct_github_header()

        assert "Authorization" not in actual
