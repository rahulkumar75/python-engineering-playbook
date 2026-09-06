from automation.linux.system_resource_reporter.system_resource_reporter import (
    check_thresholds,
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