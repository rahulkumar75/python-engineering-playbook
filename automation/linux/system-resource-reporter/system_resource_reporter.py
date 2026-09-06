import psutil


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


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
    resources = get_system_resources()
    warnings = check_thresholds(resources)

    print(f"CPU Usage: {resources['cpu']}%")
    print(f"Memory Usage: {resources['memory']}%")
    print(f"Disk Usage: {resources['disk']}%")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("\nSystem resources are within normal thresholds.")