from pathlib import Path


def analyze_log(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {file_path}")

    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
    }

    total_lines = 0

    with path.open("r") as log_file:
        for line in log_file:
            total_lines += 1

            for level in counts:
                if level in line:
                    counts[level] += 1

    return total_lines, counts


if __name__ == "__main__":
    total_lines, counts = analyze_log("application.log")

    print(f"Total lines: {total_lines}")
    print(f"INFO: {counts['INFO']}")
    print(f"WARNING: {counts['WARNING']}")
    print(f"ERROR: {counts['ERROR']}")