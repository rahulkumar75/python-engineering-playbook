# System Resource Reporter


A Python utility for checking CPU, memory, and disk usage with configurable thresholds.

## Objective

Build a Python utility to quickly collect basic system resource metrics.




## Usage

From the repository root:

```bash
python automation/linux/system_resource_reporter/system_resource_reporter.py
````

Custom thresholds:

```bash
python automation/linux/system_resource_reporter/system_resource_reporter.py \
  --cpu 50 \
  --memory 70 \
  --disk 90
```

## Example

```text
CPU Usage: 16.5%
Memory Usage: 82.9%
Disk Usage: 22.0%

Warnings:
- High memory usage
```

## Tests

Run from the repository root:

```bash
python -m pytest
```

## Current Features

* CPU monitoring
* Memory monitoring
* Disk monitoring
* Configurable thresholds
* Logging
* CLI arguments
* Unit tests

## Next

* Improve input validation
* Add JSON output
* Improve error handling

