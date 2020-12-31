
import logging
import boto3


bucket_name = 'mrivanlima1'
LocationConstraint = 'us-west-2'


s3_client = boto3.client('s3')
location = {'LocationConstraint' : LocationConstraint}
s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
