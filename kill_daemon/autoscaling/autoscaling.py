import boto3

def describe_auto_scaling_group(asGroupName):
	client = boto3.client('autoscaling')
	response = client.describe_auto_scaling_groups(AutoScalingGroupNames=[asGroupName])
	group = response['AutoScalingGroups'][0]
	minSize = group['MinSize']
	desiredCapacity = group['DesiredCapacity']

	azInstanceIds = {}

	for elem in group['Instances']:
		if elem['AvailabilityZone'] not in azInstanceIds:
			azInstanceIds[elem['AvailabilityZone']] = []
		azInstanceIds[elem['AvailabilityZone']].append(elem['InstanceId'])

	return minSize, desiredCapacity, azInstanceIds

def detach_instance(asGroupName, instanceId):
	client = boto3.client('autoscaling')
	client.detach_instances(
		InstanceIds=[instanceId],
		AutoScalingGroupName=asGroupName,
		ShouldDecrementDesiredCapacity=True
	)