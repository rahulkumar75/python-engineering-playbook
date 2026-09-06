import argparse
import logging

import psutil


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Report system resource usage."
    )

    parser.add_argument("--cpu", type=float, default=80)
    parser.add_argument("--memory", type=float, default=80)
    parser.add_argument("--disk", type=float, default=80)

    return parser.parse_args()


def get_system_resources():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
    }


def check_thresholds(resources, thresholds):
    warnings = []

    if resources["cpu"] >= thresholds["cpu"]:
        warnings.append("High CPU usage")

    if resources["memory"] >= thresholds["memory"]:
        warnings.append("High memory usage")

    if resources["disk"] >= thresholds["disk"]:
        warnings.append("High disk usage")

    return warnings


if __name__ == "__main__":
    args = get_arguments()

    logger.info("Collecting system resources")

    resources = get_system_resources()

    thresholds = {
        "cpu": args.cpu,
        "memory": args.memory,
        "disk": args.disk,
    }

    warnings = check_thresholds(resources, thresholds)

    print(f"CPU Usage: {resources['cpu']}%")
    print(f"Memory Usage: {resources['memory']}%")
    print(f"Disk Usage: {resources['disk']}%")

    if warnings:
        logger.warning("Resource threshold exceeded")

        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        logger.info("System resources are within normal thresholds")
        print("\nSystem resources are within normal thresholds.")