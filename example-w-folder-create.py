import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAJS74K3M7HKCCAZYA'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'otc-cashaa'

data = open('bitmoji.png', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='users-kyc-ducuments/user@mail.com/bitmoji.png', Body=data)

print ("Done")
