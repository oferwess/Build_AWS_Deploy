1. The ansible-playbook yml using aws_ec2 module for dynamic inventory
requirements should be installed on ansbile server (beside ansible pakages and dependencies) 
    python3     --> yum install python3 -y
    python3-pip --> yum –y install python3-pip
    boto3       --> pip3 install boto3

2. Please insert your AWS credentioanls aws_access_key and aws_secret_key into aws_ec2.yaml file lines 3-4
or use ENV varibles on your ~/.bashrc profile:
    export AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"
    export AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_ACCESS_KEY"
    export AWS_DEFAULT_REGION=YOUR_AWS_DEFAULT_REGION
    export ANSIBLE_CONFIG="repo_location/ansible-playbook/ansible.cfg"

3. from task2-Ansible directory run this command: ansible-playbook ansible-playbook.yml