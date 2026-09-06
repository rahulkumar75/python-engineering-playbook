import boto3


def get_ec2_instances():
    ec2 = boto3.client("ec2")

    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append(
                {
                    "id": instance["InstanceId"],
                    "state": instance["State"]["Name"],
                    "type": instance["InstanceType"],
                }
            )

    return instances


if __name__ == "__main__":
    instances = get_ec2_instances()

    if not instances:
        print("No EC2 instances found.")
        raise SystemExit(0)

    for instance in instances:
        print(
            f"ID: {instance['id']} | "
            f"State: {instance['state']} | "
            f"Type: {instance['type']}"
        )