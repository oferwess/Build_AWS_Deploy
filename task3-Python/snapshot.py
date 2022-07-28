import boto3
from datetime import datetime

def building_snapshots_per_vol_aray (snapshots_list):
    snapshots_per_vol_array = []
    count = 0
    for snapshot in snapshots_list: 
        count = count + 1
        snapshots_per_vol_list = {"snapshot_tags":snapshot.tags,"snapshot_id":snapshot.id, "volume_id":snapshot.volume_id,"date":snapshot.start_time}
        snapshots_per_vol_array.append(snapshots_per_vol_list)
    return(snapshots_per_vol_array)

def makes_first_napshot(EC2_RESOURCE,VOLUME_ID):
    snapshot_count = str(1)
    snapshot = EC2_RESOURCE.create_snapshot(
        VolumeId=VOLUME_ID,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                {'Key': 'Name','Value': "snapshot1_"+str(VOLUME_ID)},
                {'Key': 'volumeid','Value': VOLUME_ID},
                {'Key': 'snapshot_count','Value': snapshot_count}
                ]
                    },
                ]
            
    )
    print (f'Snapshot {snapshot.id} created for volume {VOLUME_ID}')

def makesnapshot(EC2_RESOURCE,VOLUME_ID,number_of_snapshots,snapshot_count):
    snapshot_count = str((int(snapshot_count))+1)
    snapshot = EC2_RESOURCE.create_snapshot(
        VolumeId=VOLUME_ID,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {'Key': 'Name','Value': "snapshot" + snapshot_count + "_"+str(VOLUME_ID)},
                    {'Key': 'volumeid','Value': VOLUME_ID  },
                    {'Key': 'snapshot_count','Value': snapshot_count}
                ]
            },
        ]
    )
    print (f'Snapshot {snapshot.id} created for volume {VOLUME_ID}')

def find_minimum (snapshots_array):
        index=0
        minimum = 0
        for eachitem in snapshots_array:
            if eachitem["date"] < snapshots_array[minimum]["date"]:
                minimum=index
            index=index+1
        return (snapshots_array[minimum])

def find_maximum (snapshots_array):
        index=0
        maximum = 0
        for eachitem in snapshots_array:
            if eachitem["date"] > snapshots_array[maximum]["date"]:
                maximum=index
            index=index+1    
        return (snapshots_array[maximum])


def delete_oldest_snapshot(EC2_RESOURCE,minimum_snapshot_id):
    snapshot = EC2_RESOURCE.Snapshot(minimum_snapshot_id)
    snapshot.delete()
    print(f'Snapshot {minimum_snapshot_id} has been deleted')


AWS_REGION = input("type your Region. For example: eu-west-1\n")
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
VOLUME_ID = input("Please provide Volume ID\n")

STS_CLIENT = boto3.client('sts')
CURRENT_ACCOUNT_ID = STS_CLIENT.get_caller_identity()['Account']
snapshots_list = EC2_RESOURCE.snapshots.filter(
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [VOLUME_ID]
        }
    ]
)


snapshots_array = building_snapshots_per_vol_aray(snapshots_list)
if snapshots_array: #if snapshots exists in the array
    number_of_snapshots =  (len(snapshots_array))
    minimum_snapshot_date = find_minimum (snapshots_array)["date"]
    minimum_snapshot_id = find_minimum (snapshots_array)["snapshot_id"]
    maximum_snapshot_tags = find_maximum (snapshots_array)["snapshot_tags"]
    snapshot_count = sorted(maximum_snapshot_tags, key=lambda  i: i['Key'])[1]["Value"]
    if number_of_snapshots < 3:
        makesnapshot (EC2_RESOURCE,VOLUME_ID,number_of_snapshots,snapshot_count)
    else:
        delete_oldest_snapshot(EC2_RESOURCE,minimum_snapshot_id)
        makesnapshot (EC2_RESOURCE,VOLUME_ID,number_of_snapshots,snapshot_count)
        
else:
    makes_first_napshot(EC2_RESOURCE,VOLUME_ID)
