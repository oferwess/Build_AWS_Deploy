########################################
## Virtual Machine Module - Variables ##
########################################
variable "instance_count" {
  default = 2
}

variable "aws_eip_association" {
  default = 2
}

variable "aws_eip" {
  default = 2
}

variable "linux_instance_type" {
  type        = string
  description = "EC2 instance type for Linux Server"
  default     = "t2.micro"
}

variable "linux_associate_public_ip_address" {
  type        = bool
  description = "Associate a public IP address to the EC2 instance"
  default     = true
}

variable "linux_root_volume_size" {
  type        = number
  description = "Volume size of root volume of Linux Server"
}

variable "linux_data_volume1_size" {
  type        = number
  description = "Volume size of data volume1 of Linux Server"
}

variable "linux_data_volume2_size" {
  type        = number
  description = "Volume size of data volume2 of Linux Server"
}

variable "linux_root_volume_type" {
  type        = string
  description = "Volume type of root volume of Linux Server. Can be standard, gp3, gp2, io1, sc1 or st1"
  default     = "gp2"
}

variable "linux_data_volume1_type" {
  type        = string
  description = "Volume type of data volume of Linux Server. Can be standard, gp3, gp2, io1, sc1 or st1"
  default     = "standard"
}

variable "linux_data_volume2_type" {
  type        = string
  description = "Volume type of data volume2 of Linux Server. Can be standard, gp3, gp2, io1, sc1 or st1"
  default     = "standard"
}