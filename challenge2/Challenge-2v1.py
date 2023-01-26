import boto3
import json

# Connect to the AWS EC2 service
ec2 = boto3.client('ec2')

# Specify the instance ID to query , do add instance ID which meta you want fetch.
instance_id = 'i-xxxxxxxxxxx'

# Query the meta data of the specified instance
response = ec2.describe_instances(InstanceIds=[instance_id])

# Extract the meta data from the response
meta_data = response['Reservations'][0]['Instances'][0]

# Extracting specific keys
keys_to_extract = ["InstanceType", "State", "PrivateIpAddress"]
extracted_data = {}

# Extracting the specific keys and adding them to the extracted_data dictionary
for key in keys_to_extract:
    extracted_data[key] = meta_data[key]

# Converting the extracted data to json
json_output = json.dumps(extracted_data, indent=4)

#Printing the json object
print(json_output)
