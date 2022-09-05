#! /bin/bash
#Creating User dev and importing PEM ssl public key for SSH connection
adduser dev

#Use shell script to realize partition, formatting and mounting data disks

for V in $(ls /dev/xvd[b-z])
do
 echo -e "n\np\n\n\n\nw\n" |fdisk $V
 mkfs.xfs -i size=512 ${V}1 &>/dev/null
 sleep 1
 M=$(echo "$V" |awk -F "/" '{print $3}')
 mkdir -p /data-${M}1/ &>/dev/null
 echo -e "${V}1 /data-${M}1/ xfs defaults 0 0\n" >>/etc/fstab
 mount -a &>/dev/null
done