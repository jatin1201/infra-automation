Our Goal is to jsp backend & frontend infrastructure which is highly scalable in nature as well resiliant too also following the industry recommended security standards

Lets follow the below steps to execute the code to deploy Infrastructure 

Prerequisites 
- AWS Account 
- Terraform 
- Add aws profile name in the provider.tf
- AWS CLI must be configured 
- SSH Key (must be created prior execution of the code and update variable file also please make sure key was created in same region as the provider, and if you need to go with default ssh key name you need to create key named as test-devops-keypair in us-west-2 region)
- Change variables.tf if needed (just in case you need to change some naming conventions this is totally optional)

Before executing the code lets understand bit of this code, i followed the terraform module approach (A group of Terraform configuration files contained in a single directory constitute a Terraform module. even a straightforward configuration with a single directory and one or more. A module is tf files. It is regarded as the root module when Terraform commands are executed directly from such a directory.) to launch our desired infrastruture over the aws 

This code is reusable and easy to jsp.


Run the code 

- Clone this github repo
- cd into Terraform-js

Once we inside the js directory as i mention we are using terraform module so we need to install all the modules of our infrastructure, to do so

- run terraform init
this will take couple minutes to installed all the modules into root 

- after the successful execution of init phase of terraform we need to test our code via dry run or more of validation of the code need to be done for that run below command

- run terraform plan 
This will also take few mooment to load up and generate the output

once you validate the code successfully we need to enforce the changes to the aws account 
- run terraform apply 
this will take sometime to compelete the process and once it done you'll have your assets ready 

just log into the aws account >> switch your region >> check all the assets on the aws console








