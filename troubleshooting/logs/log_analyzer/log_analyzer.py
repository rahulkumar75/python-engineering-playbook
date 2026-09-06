from pathlib import Path
import argparse

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

def get_arguments():
    parser = argparse.ArgumentParser(
        description="Analyze application logs."
    )

    parser.add_argument(
        "file",
        help="Path to the log file",
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = get_arguments()

    try:
        total_lines, counts = analyze_log(args.file)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        raise SystemExit(1)
   

    print(f"Total lines: {total_lines}")
    print(f"INFO: {counts['INFO']}")
    print(f"WARNING: {counts['WARNING']}")
    print(f"ERROR: {counts['ERROR']}")