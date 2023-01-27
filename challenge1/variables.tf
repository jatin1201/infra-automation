variable "project" {
  description = "The project to use for unique resource naming"
  default     = "js-infra"
  type        = string
}


variable "ssh_keypair" {
  description = "SSH keypair to use for EC2 instance"
  default     = "test-devops-keypair"
  type        = string
}


variable "region" {
  description = "AWS region"
  default     = "us-west-2"
  type        = string
}
