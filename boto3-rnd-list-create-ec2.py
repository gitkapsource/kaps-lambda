#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print (instance.id, instance.state)


instance = ec2.create_instances(
    ImageId='ami-76d6f519',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
print ("AWS EC2 instance created with Instance ID : " + instance[0].id + "\n")

for instance in ec2.instances.all():
    print ("Second Loop\n")
    print (instance.id, instance.state)
