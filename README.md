# infra-automation

## Challenge 1 ##

This module will launch 3-tier application infrastructure over the aws

### Prerequisites ###

- AWS Account  

- Terraform 

- Add aws profile name in the provider.tf

- AWS CLI must be configured 

- SSH Key (must be created prior execution of the code and update variable file also please make sure key was created in same region as the provider, and if you need to go with default ssh key name you need to create key named as test-devops-keypair in us-west-2 region)

- Change variables.tf if needed (just in case you need to change some naming conventions this is totally optional)


### Usage ###

- Clone this github repo

- cd into challenge1

- Run terraform init

- After the successful execution of init phase of terraform we need to test our code via dry run or more of validation of the code need to be done for that run below command

- Run terraform plan 

- Run terraform apply 




## Challenge 2 ##

This script is used to extract metadata from an EC2 instance on AWS. The script can be used to extract specific keys from the metadata of an instance by passing the keys as command-line arguments.

### Prerequisites ###

- AWS account
- Python 3
- Boto3 library
- IAM user with permissions to access EC2 instances


### Usage ###

TEST with v1 Script

- Clone or download the script to your local machine. 
 
- In the code, make sure to replace the instance_id variable with the actual instance ID of the EC2 instance you want to query, and update the keys_to_extract list with the keys you want to extract.

- You need to set your AWS credentials to access the EC2 service, you can do this by creating an AWS access key and secret access key and set them in the environment or in the boto3 client. You can also set them in the ~/.aws/credentials file on your local machine

- Run the script by executing the following command in your terminal:
 
  ``` python Challenge-2v1.py ```
 
- The script will return the metadata in JSON format for the specified keys.


TEST With v2 Script 

- Install the required libraries by running pip install boto3 on your command line. 

- Run the script by providing the instance ID and the keys you want to extract as command-line arguments (USE this with v2 Script)

``` python Challenge-2v2.py  <instance_id> <keys_to_extract> ```

- The script will return the metadata in JSON format for the specified keys.

 
 ## Challenge 3 ##
 
This function takes in a nested object and a key in the format "a/b/c" and returns the corresponding value. This function uses the "/" as a delimiter to split the key and access the nested object:
 
 
 ### Prerequisites ###
 
 - Python 3

 ### Usage ###
 
 - Clone this repo or download this script 
 
 - Open a terminal or command prompt.

 - Navigate to the directory where you have cloned/download the code file.

 - Run the command ```python <filename>.py```, where <filename> is the name of the code file.

 - The code will execute and the output will be displayed on the terminal/command prompt.

 - If you have added any test cases in the test_get_value() function, you can check the output of the code by running the test function.
