import boto3

def get_object(bucket, key, path):
	client = boto3.client('s3')
	client.download_file(bucket, key, path)