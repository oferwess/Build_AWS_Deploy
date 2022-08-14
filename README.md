# Build AWS Deploy Labs Task

1.	Terraform:
    Create terraform deployment which does the following: <br />
    *	creates 2 EC2 instances in AWS (most small size) (based on any Centos image) <br />
    *	each node should has 2 external disks 1Gb each <br />
    *	external disks must be mounted to /data & /data1 directories (persistent over the reboot) <br />
    *	instance must be accessible from Internet <br />
    *	applies elastic IP to every node <br />
    *	create user 'dev' <br />
    *	allow SSH connection to user 'dev' using your SSH key <br />

2.	Ansible:
     Write an Ansible playbook which does the following over 2 hosts from the previous task: <br />
    *	installs 3 packages: <br />
  	        chrome <br />
            bzip2 <br />
            perl <br />
    *	start chrome application <br />
    *	downloads tgz file from http://www.sbeams.org/sample_data/Microarray/External_test_data.tar.gz and open it to /var/tmp directory <br />
    *	add the following entries to /etc/hosts file (create backup before the changes): <br />
            1.2.3.4 host1 <br />
            3.4.2.1 host2 <br />
            5.6.3.2 host3 <br />

3.	Scripting: 
  Write a python script for taking AWS EBS snapshots on EC2 instance external disk (see the task #1) <br />
  The script will accept the following command-line arguments: <br />
    *   Snapshot name <br />
    *   EBS by volume id <br />
    *   Number of snapshot to archive (automatically deletes the old ones) <br />

4.	Kubernetes:
    *   Install Kubernetes minimal installation on some of the nodes from task #1 <br />
    *   deploy apache server (https://hub.docker.com/_/httpd) as deployment (not just a pod) <br />
    *   check using rest api that server is up & running from the command line of the Centos node (not from the Pod itself) <br />

