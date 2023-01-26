# infra-automation

Challenge 1






## Challenge 2 ##

This script is used to extract metadata from an EC2 instance on AWS. The script can be used to extract specific keys from the metadata of an instance by passing the keys as command-line arguments.

### Prerequisites ###

- AWS account
- Python 3
- Boto3 library
- IAM user with permissions to access EC2 instances


### Usage ###

- Install the required libraries by running pip install boto3 on your command line.

- Run the script by providing the instance ID and the keys you want to extract as command-line arguments
'python ec2_metadata.py <instance_id> <keys_to_extract>'

- The script will return the metadata in JSON format for the specified keys.
