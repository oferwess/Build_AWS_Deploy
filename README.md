# Voyager Labs Task

1.	Terraform
Create terraform deployment which does the following:
a.	- creates 2 EC2 instances in AWS (most small size) (based on any Centos image)
b.	- each node should has 2 external disks 1Gb each
c.	- external disks must be mounted to /data & /data1 directories (persistent over the reboot)
d.	- instance must be accessible from Internet
e.	- applies elastic IP to every node 
f.	- create user 'dev'
g.	- allow SSH connection to user 'dev' using your SSH key

2.	Ansible
  Write an Ansible playbook which does the following over 2 hosts from the previous task:
•	installs 3 packages:
  	chrome
    bzip2
    perl
•	start chrome application
•	downloads tgz file from http://www.sbeams.org/sample_data/Microarray/External_test_data.tar.gz and open it to /var/tmp directory 
•	add the following entries to /etc/hosts file (create backup before the changes):
    1.2.3.4 host1
    3.4.2.1 host2
    5.6.3.2 host3

3.	Scripting
 
  Write a python script for taking AWS EBS snapshots on EC2 instance external disk (see the task #1)
  The script will accept the following command-line arguments:
    - Snapshot name  
    - EBS by volume id
    - Number of snapshot to archive (automatically deletes the old ones)

4.	Kubernetes
- Install Kubernetes minimal installation on some of the nodes from task #1
- deploy apache server (https://hub.docker.com/_/httpd) as deployment (not just a pod)
- check using rest api that server is up & running from the command line of the Centos node (not from the Pod itself)

