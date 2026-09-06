import logging

import psutil


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def get_system_resources():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
    }


def check_thresholds(resources):
    warnings = []

    if resources["cpu"] >= CPU_THRESHOLD:
        warnings.append("High CPU usage")

    if resources["memory"] >= MEMORY_THRESHOLD:
        warnings.append("High memory usage")

    if resources["disk"] >= DISK_THRESHOLD:
        warnings.append("High disk usage")

    return warnings


if __name__ == "__main__":
    logger.info("Collecting system resources")

    resources = get_system_resources()
    warnings = check_thresholds(resources)

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