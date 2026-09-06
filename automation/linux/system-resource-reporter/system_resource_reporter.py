import psutil


def get_system_resources():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
    }


if __name__ == "__main__":
    resources = get_system_resources()

    print(f"CPU Usage: {resources['cpu']}%")
    print(f"Memory Usage: {resources['memory']}%")
    print(f"Disk Usage: {resources['disk']}%")