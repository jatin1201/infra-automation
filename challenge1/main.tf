provider "aws" {
  region = var.region
}

module "vpc" {
  source = "./modules/vpc"
  region = var.region
  public_subnet_cidrs = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
  db_subnet_cidrs = var.db_subnet_cidrs
}

module "app_tier" {
  source = "./modules/app_tier"
  public_subnet_ids = module.vpc.public_subnet_ids
}

module "db_tier" {
  source = "./modules/db_tier"
  db_subnet_ids = module.vpc.db_subnet_ids
}
