from unittest.mock import Mock, patch

import pytest

from troubleshooting.networking.http_health_checker.http_health_checker import (
    check_health,
)


@patch("troubleshooting.networking.http_health_checker.http_health_checker.requests.get")
def test_check_health_success(mock_get):
    response = Mock()
    response.status_code = 200
    response.elapsed.total_seconds.return_value = 0.25

    mock_get.return_value = response

    result = check_health("https://example.com")

    assert result["url"] == "https://example.com"
    assert result["status_code"] == 200
    assert result["response_time"] == 0.25


@patch("troubleshooting.networking.http_health_checker.http_health_checker.requests.get")
def test_check_health_failure(mock_get):
    import requests

    mock_get.side_effect = requests.exceptions.ConnectionError()

    with pytest.raises(RuntimeError, match="Health check failed"):
        check_health("https://invalid.example")