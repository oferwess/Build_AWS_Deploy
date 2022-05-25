1. The ansible-playbook yml using aws_ec2 module for dynamic inventory
requirements should be installed on ansbile server (beside ansible pakages and dependencies) 
    python3     --> yum install python3 -y
    python3-pip --> yum –y install python3-pip
    boto3       --> pip3 install boto3

2. Please insert your AWS credentioanls aws_access_key and aws_secret_key into aws_ec2.yaml file lines 3-4

3. from task2-Ansible directory run this command: ansible-playbook ansible-playbook.yml