import requests


def check_health(url):
    response = requests.get(url, timeout=5)

    return {
        "url": url,
        "status_code": response.status_code,
        "response_time": response.elapsed.total_seconds(),
    }


if __name__ == "__main__":
    result = check_health("https://google.com")

    print(f"URL: {result['url']}")
    print(f"Status Code: {result['status_code']}")
    print(f"Response Time: {result['response_time']:.3f}s")