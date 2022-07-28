import boto3

def building_snapshots_per_vol_aray (snapshots_list): #Build snapshot per volume array based on snapshot list of specific volume
    snapshots_per_vol_array = []
    count = 0
    for snapshot in snapshots_list: 
        count = count + 1
        snapshots_per_vol_list = {"snapshot_tags":snapshot.tags,"snapshot_id":snapshot.id, "volume_id":snapshot.volume_id,"date":snapshot.start_time}
        snapshots_per_vol_array.append(snapshots_per_vol_list)
    return(snapshots_per_vol_array)

def makes_first_napshot(EC2_RESOURCE,VOLUME_ID):
    snapshot = EC2_RESOURCE.create_snapshot(
        VolumeId=VOLUME_ID,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                {'Key': 'Name','Value': "snapshot1_"+str(VOLUME_ID)},
                {'Key': 'volumeid','Value': VOLUME_ID},
                {'Key': 'snapshot_count','Value': str(1)}
                ]
                    },
                ]
            
    )
    print (f'Snapshot {snapshot.id} created for volume {VOLUME_ID}')

def makesnapshot(EC2_RESOURCE,VOLUME_ID,snapshot_count):
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

def find_minimum_maximum (snapshots_array):
    index=0
    minimum = 0
    maximum = 0
    for each_snapshot in snapshots_array:
        if each_snapshot["date"] < snapshots_array[minimum]["date"]:
            minimum=index
        elif each_snapshot["date"] > snapshots_array[maximum]["date"]:
            maximum=index
        index=index+1
    min_max_dict = {"minimum":snapshots_array[minimum],"maximum":snapshots_array[maximum]}
    return (min_max_dict)

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
    minimum_snapshot_date = find_minimum_maximum (snapshots_array)["minimum"]["date"]
    minimum_snapshot_id = find_minimum_maximum (snapshots_array)["minimum"]["snapshot_id"]
    maximum_snapshot_tags = find_minimum_maximum (snapshots_array)["maximum"]["snapshot_tags"]
    snapshot_count = sorted(maximum_snapshot_tags, key=lambda  i: i['Key'])[1]["Value"] #sorting the tags to keep the tags order
    if number_of_snapshots < 3:
        makesnapshot (EC2_RESOURCE,VOLUME_ID,snapshot_count)
    else:
        delete_oldest_snapshot(EC2_RESOURCE,minimum_snapshot_id)
        makesnapshot (EC2_RESOURCE,VOLUME_ID,snapshot_count)
        
else:
    makes_first_napshot(EC2_RESOURCE,VOLUME_ID) #If there are no old snapshots