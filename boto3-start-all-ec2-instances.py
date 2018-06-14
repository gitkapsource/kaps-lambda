#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print ("Starting " + instance.id + "\n")
    instance = ec2.Instance(instance.id)
    response = instance.start()
    print response
