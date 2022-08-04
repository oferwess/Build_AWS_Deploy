1) Please insert your AWS credentioanls into your ENV by ~/.bashrc or manually in terraform.tfvars line 23-25 (more details you will find there)
        You can change number of instances by editing terraform.tfvars line 31
        You can change volume size or type by editing terraform.tfvars line 32-39
        You can change CentOS version of instance as you wish from linux-vm-main.tf line 19
2) To run this deployment:
    A) clone the repo.
    B) cd to repo location.
    C) Run this command ===>  terraform apply -auto-approve
