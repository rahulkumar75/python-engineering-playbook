# Log Analyzer

A Python utility for quickly analyzing application logs.

## Problem

During troubleshooting, manually counting log levels in large log files is repetitive.

## Objective

Build a simple Python utility that summarizes common log levels.

## Current Features

- Count total log lines
- Count `INFO` messages
- Count `WARNING` messages
- Count `ERROR` messages
- Detect missing log files

## Usage

From the project directory:

```bash
python log_analyzer.py
```

## Example Output
Total lines: 6
INFO: 3
WARNING: 1
ERROR: 2