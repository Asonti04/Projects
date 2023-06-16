#Stop running instances except this one
#Asonti Ginn
import boto3
ec2 = boto3.client('ec2')

response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:   
        if instance['State']['Name'] == 'running' and instance['InstanceId'] != 'i-03ed3b4d17e2297d8':
            print(instance['InstanceId'])
            response2 = ec2.stop_instances(
            InstanceIds=[instance['InstanceId'],
        ],
)

print(response2)