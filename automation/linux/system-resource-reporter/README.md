# System Resource Reporter

## Problem

During system troubleshooting, CPU, memory, and disk usage are common
initial checks.

## Objective

Build a Python utility to quickly collect basic system resource metrics.

## Current Implementation

The script reports:

- CPU usage
- Memory usage
- Disk usage

## Python

- `psutil`
- Functions
- Dictionaries
- f-strings

## Usage

```bash
python system_resource_reporter.py
```

### Example Output:
```
CPU Usage: 14.0%
Memory Usage: 82.8%
Disk Usage: 22.0%
```


### Next Improvements
- Add threshold-based warnings
- Add logging
- Add CLI arguments
- Add JSON output
- Add tests