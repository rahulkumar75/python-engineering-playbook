import pytest

from troubleshooting.logs.log_analyzer.log_analyzer import analyze_log


def test_analyze_log(tmp_path):
    log_file = tmp_path / "application.log"

    log_file.write_text(
        "INFO Application started\n"
        "WARNING High memory usage\n"
        "ERROR Database failed\n"
        "INFO Request completed\n"
    )

    total_lines, counts = analyze_log(log_file)

    assert total_lines == 4
    assert counts["INFO"] == 2
    assert counts["WARNING"] == 1
    assert counts["ERROR"] == 1


def test_missing_log_file():
    with pytest.raises(FileNotFoundError):
        analyze_log("missing.log")