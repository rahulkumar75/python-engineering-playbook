import pytest

from automation.linux.system_resource_reporter.system_resource_reporter import (
    check_thresholds,
    validate_thresholds,
)


def test_no_threshold_exceeded():
    resources = {
        "cpu": 20,
        "memory": 40,
        "disk": 50,
    }

    thresholds = {
        "cpu": 80,
        "memory": 80,
        "disk": 80,
    }

    assert check_thresholds(resources, thresholds) == []


def test_memory_threshold_exceeded():
    resources = {
        "cpu": 20,
        "memory": 90,
        "disk": 50,
    }

    thresholds = {
        "cpu": 80,
        "memory": 80,
        "disk": 80,
    }

    assert check_thresholds(resources, thresholds) == ["High memory usage"]


def test_valid_thresholds():
    thresholds = {
        "cpu": 50,
        "memory": 70,
        "disk": 90,
    }

    validate_thresholds(thresholds)


def test_invalid_threshold():
    thresholds = {
        "cpu": 150,
        "memory": 70,
        "disk": 90,
    }

    with pytest.raises(ValueError):
        validate_thresholds(thresholds)