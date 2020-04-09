import boto3
from pprint import pprint

bucket_name = 'my-bucket'

content = open('local-file.txt', 'rb')
s3 = boto3.client('s3')
response = s3.put_object(
   Bucket=bucket_name, 
   Key='directory-in-bucket/remote-file.txt', 
   Body=content
)

pprint(response)