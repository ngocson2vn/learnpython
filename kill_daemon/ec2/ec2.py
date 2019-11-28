import boto3
import pytz
import datetime

def get_public_ip(instanceId):
	client = boto3.client('ec2')
	instDict=client.describe_instances(
		Filters=[{'Name':'instance-id','Values':[instanceId]}]
	)

	publicIPAddress = ''
	for r in instDict['Reservations']:
		for inst in r['Instances']:
			publicIPAddress = inst['PublicIpAddress']

	return publicIPAddress

def get_private_ip(instanceId):
	client = boto3.client('ec2')
	instDict=client.describe_instances(
		Filters=[{'Name':'instance-id','Values':[instanceId]}]
	)

	privateIPAddress = ''
	for r in instDict['Reservations']:
		for inst in r['Instances']:
			privateIPAddress = inst['PrivateIpAddress']

	return privateIPAddress

def get_latest_instance(instanceIds):
	client = boto3.client('ec2')
	instDict=client.describe_instances(InstanceIds=instanceIds)
	launchTime = datetime.datetime(1970, 1, 1, 0, 0, 0, 0).replace(tzinfo=pytz.UTC)
	instanceId = ''
	ipAddress = ''

	for r in instDict['Reservations']:
		for instance in r['Instances']:
			print instance['LaunchTime'], instance['PrivateIpAddress']
			if launchTime < instance['LaunchTime']:
				launchTime = instance['LaunchTime']
				instanceId = instance['InstanceId']
				ipAddress = instance['PrivateIpAddress']

	return instanceId, ipAddress

def get_oldest_instance(instanceIds):
	client = boto3.client('ec2')
	instDict=client.describe_instances(InstanceIds=instanceIds)
	launchTime = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=pytz.UTC)
	ipAddress = ''

	for r in instDict['Reservations']:
		for instance in r['Instances']:
			print instance['LaunchTime'], instance['PrivateIpAddress']
			if launchTime > instance['LaunchTime']:
				launchTime = instance['LaunchTime']
				instanceId = instance['InstanceId']
				ipAddress = instance['PrivateIpAddress']

	return instanceId, ipAddress

def get_terminable_instance(tagKey, tagValue, instanceIds):
	client = boto3.client('ec2')
	instDict=client.describe_instances(
		Filters=[
			{
				'Name':'tag:%s' % tagKey,
				'Values':[
					tagValue
				]
			},
		], 
		InstanceIds=instanceIds
	)

	instanceId = ''
	if len(instDict['Reservations']):
		instanceId = instDict['Reservations']['Instances'][0]["InstanceId"]
	return instanceId

def terminate_instance(instanceId):
	client = boto3.client('ec2')
	client.terminate_instances(
		InstanceIds=[instanceId],
		DryRun=False
	)
