#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print ("Stopping " + instance.id + "\n")
    instance = ec2.Instance(instance.id)
    response = instance.stop()
    print response
