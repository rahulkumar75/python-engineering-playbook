import requests
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(
        description="Check HTTP endpoint health."
    )

    parser.add_argument(
        "url",
        help="URL to check",
    )

    return parser.parse_args()

def check_health(url):
    response = requests.get(url, timeout=5)

    return {
        "url": url,
        "status_code": response.status_code,
        "response_time": response.elapsed.total_seconds(),
    }


if __name__ == "__main__":
    args = get_arguments()

    result = check_health(args.url)

    print(f"URL: {result['url']}")
    print(f"Status Code: {result['status_code']}")
    print(f"Response Time: {result['response_time']:.3f}s")