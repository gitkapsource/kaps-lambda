#!/usr/bin/env python

import boto3
import botocore

BUCKET_NAME = 'katkapsforever' # replace with your bucket name
KEY = 'boto3-s3-list.py' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, '/tmp/s3-download.py')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
