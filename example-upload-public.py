# My IAM User inline policy is:
#
# {
#   "Version": "2012-10-17",
#   "Statement": [
#           {
#               "Effect": "Allow",
#               "Action": [
#                   "s3:ListAllMyBuckets",
#                   "s3:PutObject",
#                   "s3:GetObject",
#                   "s3:PutObjectAcl",
#                   "s3:GetObjectAcl"
#               ],
#               "Resource": [
#                   "arn:aws:s3:::*"
#               ]
#           }
#   ]
# }


import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAJS74K3M7HKCCAZYA'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'otc-cashaa'
FILE_NAME = 'bitmoji.png';


data = open(FILE_NAME, 'rb')

# S3 Connect
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

# Image Uploaded
s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data, ACL='public-read')

print ("Done")
