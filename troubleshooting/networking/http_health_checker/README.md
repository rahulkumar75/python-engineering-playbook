# HTTP Health Checker

A Python utility for checking HTTP endpoint availability and response time.

## Problem

During service troubleshooting, engineers need to quickly verify whether an HTTP endpoint is reachable and responding.

## Features

- HTTP status code
- Response time
- Configurable URL
- Request timeout
- Connection error handling
- Unit tests

## Usage

```bash
python http_health_checker.py https://google.com
````

Example:

```text
URL: https://google.com
Status Code: 200
Response Time: 1.238s
```

## Error Handling

Network and request failures are handled without exposing a Python traceback to the user.

Example:

```text
Error: Health check failed for https://invalid-domain-example-12345.com: ConnectionError
```

## Python Concepts

* `requests`
* `argparse`
* Exception handling
* Mocking
* Unit testing

## Engineering Learning

A health check should provide both availability information and useful diagnostic context such as HTTP status and response time.

## Tests

From the repository root:

```bash
python -m pytest
```


