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
