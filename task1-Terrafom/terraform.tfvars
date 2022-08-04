############################
## Application Definition ##
############################
app_name        = "task1" # Do NOT enter any spaces
app_environment = "dev"       # Dev, Test, Staging, Prod, etc

# Network
vpc_cidr           = "10.11.0.0/16"
public_subnet_cidr = "10.11.1.0/24"

# AWS Settings 

# Option 1:
# Edit your bash profile using ~/.bashrc file
# You need to have these varibles:
# export TF_VAR_aws_access_key="YOUR_AWS_ACCESS_KEY"
# export TF_VAR_aws_secret_key="YOUR_AWS_SECRET_KEY"
# export TF_VAR_aws_region="YOUR_AWS_REGION"

# Option 2:
# Uncomment the lines below and insert you AWS credentaionlas and region staticly

#aws_access_key = "YOUR_AWS_ACCESS_KEY"
#aws_secret_key = "YOUR_AWS_SECRET_KEY"
#aws_region     = "YOUR_AWS_REGION"


# Linux Virtual Machine
instance_count                    = 1
linux_instance_type               = "t2.micro"
linux_associate_public_ip_address = true
linux_root_volume_size            = 20
linux_root_volume_type            = "gp2"
linux_data_volume1_size            = 1
linux_data_volume1_type            = "standard"
linux_data_volume2_size            = 1
linux_data_volume2_type            = "standard"