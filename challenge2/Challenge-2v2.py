import boto3
import json
import sys

# Function to extract specified keys from EC2 instance metadata
def get_ec2_metadata(instance_id, keys_to_extract):
    # Create a boto3 client for EC2
    client = boto3.client('ec2')
    
    # Use the client to get the metadata for the specified instance
    response = client.describe_instances(InstanceIds=[instance_id])
    
    # Get the instance data from the response
    instance_data = response['Reservations'][0]['Instances'][0]
    
    # Create a dictionary to store the extracted data
    extracted_data = {}
    
    # Iterate through the keys to extract
    for key in keys_to_extract:
        # Extract the value of the key from the instance data
        extracted_data[key] = instance_data.get(key, "Key not found")
    
    # Return the extracted data in JSON format
    return json.dumps(extracted_data, indent=4)

if __name__ == '__main__':
    # Check if the required number of arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python ec2_metadata.py <instance_id> <keys_to_extract>")
        sys.exit()
    
    # Get the instance ID and keys to extract from the command-line arguments
    instance_id = sys.argv[1]
    keys_to_extract = sys.argv[2:]
    
