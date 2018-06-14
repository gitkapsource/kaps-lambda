#!/usr/bin/env python
import boto3

s3 = boto3.client("s3")
bucket_name = 'katkapsforever'
filename = 'boto3-s3-list.py'

s3.upload_file(filename, bucket_name, filename)
print ("File "+ filename +" uploaded successfully to the bucket " + bucket_name + "\n")
