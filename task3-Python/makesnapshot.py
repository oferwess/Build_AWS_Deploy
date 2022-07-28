import boto3
AWS_REGION = "eu-west-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
VOLUME_ID = input("Please provide Volume ID\n")
count = 1
snapshot = EC2_RESOURCE.create_snapshot(
        VolumeId=VOLUME_ID,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': "snap" + str(count)
                    },
                ]
            },
        ]
    )
print (f'Snapshot {snapshot.id} created for volume {VOLUME_ID}')