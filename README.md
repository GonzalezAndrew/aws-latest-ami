# Latest Amazon Machine Image
A simple command line interface (CLI) tool that will obtain the most recent AMI for a given distribution. 

# Usage
```
usage: latest_ami.py [--distribution DISTRIBUTION] [--output-file OUTPUT_FILE] [--region REGION] [--all-regions] [--filters FILTERS] [--help]

Get the latest AMI for a given distribution.

optional arguments:
  --distribution DISTRIBUTION
                        The distribution of the latest AMI you'd like to retrieve from the default list (Amazon, Ubuntu, Centos, Windows, RedHat, Debian).
  --output-file OUTPUT_FILE
                        Send the retrieved AMI data to a output JSON file.
  --region REGION       The region to the pull the latest AMI information from. (Overrides environment variable)
  --all-regions         To get the latest AMI from all of the avaliable regions.
  --filters FILTERS     Custom filters to use when searching for the an AMI.
  --help                Show this message and exit.
```

# Example
Example
```
./latest_ami.py --distribution amzn2 --all-regions --output-file="amzn2.json"
Grabbing all amis from every region, this will take a few seconds...
The requested latest AMI(s): [{'ap-northeast-1': 'ami-0992fc94ca0f1415a'}, {'ap-northeast-2': 'ami-09282971cf2faa4c9'}, {'ap-south-1': 'ami-08e0ca9924195beba'}, {'ap-southeast-1': 'ami-0e2e44c03b85f58b3'}, {'ap-southeast-2': 'ami-04f77aa5970939148'}, {'ca-central-1': 'ami-075cfad2d9805c5f2'}, {'eu-central-1': 'ami-0a6dc7529cd559185'}, {'eu-north-1': 'ami-0eb6f319b31f7092d'}, {'eu-west-1': 'ami-0fc970315c2d38f01'}, {'eu-west-2': 'ami-098828924dc89ea4a'}, {'eu-west-3': 'ami-0ea4a063871686f37'}, {'me-south-1': 'AMI not avaliable in this region'}, {'sa-east-1': 'ami-089aac6323aa08aee'}, {'us-east-1': 'ami-047a51fa27710816e'}, {'us-east-2': 'ami-01aab85a5e4a5a0fe'}, {'us-west-1': 'ami-005c06c6de69aee84'}, {'us-west-2': 'ami-0e999cbd62129e3b1'}]
```

### Using Default Distributions
The CLI tool comes with default filters for popular distributions (Amazon Linux, Ubuntu, Centos, Windows, Red Hat, Debian) and have default argument in order to be used.

| Distribution        | Command                      |
|---------------------|------------------------------|
| Amazon Linux (1)    | --distribution='amzn'        |
| Amazon Linux 2      | --distribution='amzn2'       |
| Ubuntu 1404         | --distribution='ubuntu1404'  |
| Ubuntu 1604         | --distribution='ubuntu1604'  |
| Ubuntu 1804         | --distribution='ubuntu1804'  |
| Ubuntu 1904         | --distribution='ubuntu1904'  |
| CentOS 6            | --distribution='centos6'     |
| CentOS 7            | --distribution='centos7'     |
| CentOS 8            | --distribution='centos8'     |
| Debian 8            | --distribution='debian8'     |
| Debian 9            | --distribution='debian9'     |
| Debian 10           | --distribution='debian10'    |
| Red Hat 6           | --distribution='redhat6'     |
| Red Hat 8           | --distribution='redhat8'     |
| Windows Server 2012 | --distribution='windows2012' |
| Windows Server 2016 | --distribution='windows2016' |
| Windows Server 2019 | --distribution='windows2019' |

### Custom Filters
A user has the option to use a custom filter when searching for any given AMI.
```
latest_ami.py --region="us-east-2" --filters="[{"Name": "name","Values": ["amzn-ami-hvm-????.??.?.????????-x86_64-gp2"],},{"Name": "state", "Values": ["available"]}]"
```
