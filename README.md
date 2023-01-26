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

Test with V1 Script

- Clone or download the script to your local machine. 
 
- In the code, make sure to replace the instance_id variable with the actual instance ID of the EC2 instance you want to query, and update the keys_to_extract list with the keys you want to extract.

- You need to set your AWS credentials to access the EC2 service, you can do this by creating an AWS access key and secret access key and set them in the environment or in the boto3 client. You can also set them in the ~/.aws/credentials file on your local machine

- Run the script by executing the following command in your terminal:
 
 ``` python Challenge-2v1.py ```
 
- The script will return the metadata in JSON format for the specified keys.

 
