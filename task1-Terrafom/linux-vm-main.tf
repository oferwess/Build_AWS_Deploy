###################################
## Virtual Machine Module - Main ##
###################################

# Create Elastic IP for the EC2 instance
resource "aws_eip" "linux-eip" {
  count = var.instance_count
  vpc  = true
  instance = aws_instance.linux-server[count.index].id
  tags = {
    Name        = "${lower(var.app_name)}-${var.app_environment}-linux-eip ${count.index}"
    Environment = var.app_environment
  }
}

# Create EC2 Instance
resource "aws_instance" "linux-server" {
  count					          	  = var.instance_count
  ami                         = data.aws_ami.centos-8.id
  instance_type               = var.linux_instance_type
  subnet_id                   = aws_subnet.public-subnet.id
  vpc_security_group_ids      = [aws_security_group.aws-linux-sg.id]
  associate_public_ip_address = var.linux_associate_public_ip_address
  source_dest_check           = false
  key_name                    = aws_key_pair.key_pair.key_name
  user_data                   = "${file("aws-user-data.sh")}"
  tags						  = {
	Name = "linux-server ${count.index}"
	Inventory = "dev"
  }
  
  # root disk
  root_block_device {
    volume_size           = var.linux_root_volume_size
    volume_type           = var.linux_root_volume_type
    delete_on_termination = true
    encrypted             = true
  }

  # data disk1
  ebs_block_device {
    device_name           = "/dev/xvdb"
    volume_size           = var.linux_data_volume1_size
    volume_type           = var.linux_data_volume1_type
    encrypted             = true
    delete_on_termination = true
	tags = {
		Name = "/data1"
	}
  }
  
  # data disk2
  ebs_block_device {
    device_name           = "/dev/xvdc"
    volume_size           = var.linux_data_volume2_size
    volume_type           = var.linux_data_volume2_type
    encrypted             = true
    delete_on_termination = true
	tags = {
		Name = "/data2"
	}
  }

}


# Associate Elastic IP to Linux Server
resource "aws_eip_association" "linux-eip-association" {
  count		    	=  var.instance_count
  instance_id   =  aws_instance.linux-server[count.index].id
  allocation_id =  aws_eip.linux-eip[count.index].id
}

# Define the security group for the Linux server
resource "aws_security_group" "aws-linux-sg" {
  name        = "${lower(var.app_name)}-${var.app_environment}-linux-sg"
  description = "Allow incoming HTTP connections"
  vpc_id      = aws_vpc.vpc.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow incoming HTTP connections"
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow incoming SSH connections"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
	    description = "Allow outgoing connections out of the instance"
  }

  tags = {
    Name        = "${lower(var.app_name)}-${var.app_environment}-linux-sg"
    Environment = var.app_environment
  }
}
