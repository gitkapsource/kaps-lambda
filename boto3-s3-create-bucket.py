#!/usr/bin/env python
import sys
import boto3

s3 = boto3.resource("s3")
for BucketName in sys.argv[1:]:
    try:
        response = s3.create_bucket(Bucket=BucketName,CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
        print response
    except Exception as error:
        print error


for bucket in s3.buckets.all():
    print bucket.name
    print "---"
    for item in bucket.objects.all():
        print "\t%s" % item.key
