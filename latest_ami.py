#! /usr/bin/env python3
import boto3
import json
import sys
import argparse


def write_to_file(data, file):
    with open(file, "w") as fout:
        fout.write(json.dumps(data, indent=4, sort_keys=True))
    fout.close()
    return {"message": "sucessfully wrote data to file."}


def ubuntu(version):
    if version == "ubuntu1404":
        return [
            {
                "Name": "name",
                "Values": ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"],
            },
            {"Name": "virtualization-type", "Values": ["hvm"]},
            {"Name": "owner-id", "Values": ["099720109477"]},
        ]

    if version == "ubuntu1604":
        return [
            {
                "Name": "name",
                "Values": ["ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-*"],
            },
            {"Name": "virtualization-type", "Values": ["hvm"]},
            {"Name": "owner-id", "Values": ["099720109477"]},
        ]

    if version == "ubuntu1804":
        return [
            {
                "Name": "name",
                "Values": ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*"],
            },
            {"Name": "virtualization-type", "Values": ["hvm"]},
            {"Name": "owner-id", "Values": ["099720109477"]},
        ]

    if version == "ubuntu1904":
        return [
            {
                "Name": "name",
                "Values": ["ubuntu/images/hvm-ssd/ubuntu-disco-19.04-amd64-server-*"],
            },
            {"Name": "virtualization-type", "Values": ["hvm"]},
            {"Name": "owner-id", "Values": ["099720109477"]},
        ]


def amzn(version):
    if version == "amzn":
        return [
            {"Name": "name", "Values": ["amzn-ami-*-x86_64-gp2"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["137112412989"]},
        ]

    if version == "amzn2":
        return [
            {"Name": "name", "Values": ["amzn2-ami-hvm*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["137112412989"]},
        ]


def centos(version):
    if version == "centos6":
        return [
            {"Name": "name", "Values": ["CentOS Linux 6*x86_64*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["679593333241"]},
        ]

    if version == "centos7":
        return [
            {"Name": "name", "Values": ["CentOS Linux 7*x86_64*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["679593333241"]},
        ]

    if version == "centos8":
        return [
            {"Name": "name", "Values": ["CentOS Linux 8*x86_64*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["679593333241"]},
        ]


def debian(version):
    if version == "debian8":
        return [
            {"Name": "name", "Values": ["debian-jessie*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["679593333241"]},
        ]

    if version == "debian9":
        return [
            {"Name": "name", "Values": ["debian-stretch*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["679593333241"]},
        ]

    if version == "debian10":
        return [
            {"Name": "name", "Values": ["debian-10*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["679593333241"]},
        ]


def redhat(version):
    if version == "redhat6":
        return [
            {"Name": "name", "Values": ["RHEL-6.*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["309956199498"]},
        ]

    if version == "redhat7":
        return [
            {"Name": "name", "Values": ["RHEL-7.*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["309956199498"]},
        ]

    if version == "redhat8":
        return [
            {"Name": "name", "Values": ["RHEL-8.*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["309956199498"]},
        ]


def windows(version):
    if version == "windows2012":
        return [
            {
                "Name": "name",
                "Values": ["Windows_Server-2012-R2_RTM-English-64Bit-Base-*"],
            },
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["137112412989"]},
        ]

    if version == "windows2016":
        return [
            {"Name": "name", "Values": ["Windows_Server-2016-English-Full-Base*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["137112412989"]},
        ]

    if version == "windows2019":
        return [
            {"Name": "name", "Values": ["Windows_Server-2019-English-Full-Base*"]},
            {"Name": "root-device-type", "Values": ["ebs"]},
            {"Name": "architecture", "Values": ["x86_64"]},
            {"Name": "owner-id", "Values": ["137112412989"]},
        ]


def get_filters(distro):
    if "amzn" in distro:
        return amzn(distro)

    elif "ubuntu" in distro:
        return ubuntu(distro)

    elif "centos" in distro:
        return centos(distro)

    elif "debian" in distro:
        return debian(distro)

    elif "redhat" in distro:
        return redhat(distro)

    elif "windows" in distro:
        return windows(distro)
    else:
        print(f"User specified an unknown distribution: {distro}")
        print("Please try again with a valid argument.")
        sys.exit(1)


def get_all_regions():
    ec2 = boto3.client("ec2")
    regions = sorted(
        [region["RegionName"] for region in ec2.describe_regions()["Regions"]]
    )
    return regions


def get_all_amis(distro):
    regions = get_all_regions()
    base = []
    print(
        "Grabbing all amis for the specified distribution, from every region, this will take a few seconds..."
    )
    for region in regions:
        client = boto3.client("ec2", region_name=region)
        filters = get_filters(distro)
        response = client.describe_images(Filters=filters)
        if response["Images"]:
            amis = sorted(
                response["Images"], key=lambda x: x["CreationDate"], reverse=True
            )
            row = {region: amis[0]["ImageId"]}
        else:
            row = {region: "AMI not avaliable in this region"}
        base.append(row)
    return base


def get_ami(region, filters):
    print("Retrieving the AMI that was requested...")
    client = boto3.client("ec2", region)
    response = client.describe_images(Filters=filters)
    if response["Images"]:
        metadata = sorted(
            response["Images"], key=lambda x: x["CreationDate"], reverse=True
        )
        latest_ami = metadata[0]["ImageId"]
        return latest_ami
    else:
        print("Ran into an unexpected error.")


def cli(args):
    if args.filters and not args.distribution:
        filters = args.filters
        if args.region and not args.all_regions:
            return get_ami(args.region, filters)
        elif args.all_regions and not args.region:
            return get_all_amis(filters)

    elif args.distribution and not args.filters:
        if args.region and not args.all_regions:
            filters = get_filters(args.distribution)
            return get_ami(args.region, filters)
        else:
            return get_all_amis(args.distribution)
    else:
        print(f"Error. User specified an unknown argument. {str(args)}")
        args.print_help()
        sys.exit()


def main():
    parser = argparse.ArgumentParser(
        description="Get the latest AMI for a given distribution.", add_help=False
    )

    parser.add_argument(
        "--distribution",
        type=str,
        required=False,
        default="amzn2",
        help="The distribution of the latest AMI you'd like to retrieve from the default list (Amazon, Ubuntu, Centos, Windows, RedHat, Debian).",
    )

    parser.add_argument(
        "--output-file",
        type=str,
        required=False,
        default=None,
        help="Send the retrieved AMI data to a output JSON file.",
    )

    parser.add_argument(
        "--region",
        type=str,
        required=False,
        default="us-east-2",
        help="The region to the pull the latest AMI information from. (Overrides environment variable)",
    )

    parser.add_argument(
        "--all-regions",
        required=False,
        action="store_true",
        help="To get the latest AMI from all of the avaliable regions.",
    )

    parser.add_argument(
        "--filters",
        type=str,
        required=False,
        default=None,
        help="Custom filters to use when searching for the an AMI.",
    )

    parser.add_argument(
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show this message and exit.",
    )

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    ami = cli(args)
    if args.output_file:
        write_to_file(ami, args.output_file)

    print(f"The requested latest AMI(s): {ami}")


if __name__ == "__main__":
    main()