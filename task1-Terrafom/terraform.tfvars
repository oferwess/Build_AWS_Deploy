############################
## Application Definition ##
############################
app_name        = "task1" # Do NOT enter any spaces
app_environment = "dev"       # Dev, Test, Staging, Prod, etc

# Network
vpc_cidr           = "10.11.0.0/16"
public_subnet_cidr = "10.11.1.0/24"

# AWS Settings
aws_access_key = "Type your AWS Access Key"
aws_secret_key = "Type your AWS Secret Key"
aws_region     = "eu-west-1"

# Linux Virtual Machine
instance_count                    = 2
linux_instance_type               = "t2.micro"
linux_associate_public_ip_address = true
linux_root_volume_size            = 20
linux_root_volume_type            = "gp2"
linux_data_volume1_size            = 1
linux_data_volume1_type            = "standard"
linux_data_volume2_size            = 1
linux_data_volume2_type            = "standard"