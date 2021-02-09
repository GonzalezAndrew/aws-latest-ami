import pytest
import boto3  
from moto import mock_ec2
from moto.ec2.models import OWNER_ID


@mock_ec2
def test_get_ami():
    ec2 = boto3.client("ec2", "us-east-2")
    data = ec2.describe_images(Filters=[{"Name": "image-id", "Values": ["ami-03cf127a"]}])
    
    if data["Images"]:
        amis = sorted(data["Images"], key=lambda x: x["CreationDate"], reverse=True)
        latest_ami = amis[0]["ImageId"]
        return latest_ami

def test_ami():
    assert "ami-03cf127a" == test_get_ami()

