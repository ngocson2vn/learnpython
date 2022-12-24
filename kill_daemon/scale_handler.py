import os
import sys
import json
import base64
import datetime

sys.path.append("./vendored")
from ec2 import ec2
from s3 import s3
from ld import ld
from autoscaling import autoscaling
from cloudwatch import cloudwatch
from slack import slack

SERVICE_NAME = 'ScaleInECSTaskCluster'
STAGE = os.environ['STAGE']
SLACK_URL = os.environ['SLACK_URL']
SCALE_IN_THRESHOLD = int(os.environ['SCALE_IN_THRESHOLD'])
DATAPOINT_PERIOD = int(os.environ['DATAPOINT_PERIOD'])
DATAPOINT_COUNT = int(os.environ['DATAPOINT_COUNT'])


def get_datapoints(clusterName, asGroupName):
	endTime = datetime.datetime.utcnow().replace(second=0, microsecond=0) - datetime.timedelta(minutes=1)
	startTime = endTime - datetime.timedelta(minutes=15)

	datapoints = []

	for i in xrange(1, DATAPOINT_COUNT + 1):
		metricValue = cloudwatch.get_cluster_metric_value(clusterName, 'CPUMemoryUtilizationNormalized', startTime, endTime)
		print 'StartTime: %s, EndTime: %s, CPUMemoryUtilizationNormalized: %s' % (startTime, endTime, metricValue)

		if metricValue is not None and metricValue < SCALE_IN_THRESHOLD:
			datapoints.append(metricValue)

		endTime = startTime
		startTime = endTime - datetime.timedelta(minutes=DATAPOINT_PERIOD)

	return datapoints


def terminate_terminable_instance(clusterName, asGroupName, instanceIds):
	tagKey = 'AutoScalingState2'
	tagValue = '%sECSTerminable' % clusterName
	instanceId = ec2.get_terminable_instance(tagKey, tagValue, instanceIds)

	if len(instanceId) > 0:
		autoscaling.detach_instance(asGroupName, instanceId)
		ec2.terminate_instance(instanceId)
		text = "Description: Terminating EC2 instance: %s\n" % instanceId
		text = text + "Cause: The scale-in conditions were satisfied. MinSize: %s < DesiredCapacity: %s " % (minSize, desiredCapacity)
		text = text + "and Threshold Crossed: %s datapoints %s were less than the threshold (%s)" % (DATAPOINT_COUNT, datapoints, SCALE_IN_THRESHOLD)
		slack.post_to_slack(SLACK_URL, asGroupName, text, "warn")
		return True, instanceId

	return False, None


def trigger_scale_in(event, context):
	clusterName = '%sTask' % STAGE
	asGroupName = '%sTaskECSAutoScaleGroup' % STAGE
	print "clusterName: %s, asGroupName: %s" % (clusterName, asGroupName)

	minSize, desiredCapacity, azInstanceIds = autoscaling.describe_auto_scaling_group(asGroupName)

	instanceIds = []
	for key in azInstanceIds.keys():
		instanceIds += azInstanceIds[key]

	done, terminatedInstanceId = terminate_terminable_instance(clusterName, asGroupName, instanceIds)
	if done:
		return {'message': 'Terminated instance: %s' % terminatedInstanceId}

	datapoints = get_datapoints(clusterName, asGroupName)
	if (len(datapoints) < DATAPOINT_COUNT) or (desiredCapacity == minSize):
		return {'message': 'The scale-in conditions are not satisfied.'}

	# Get AZ with maximum instance count
	count = 0
	az = ''
	for key in azInstanceIds.keys():
		if len(azInstanceIds[key]) > count:
			count = len(azInstanceIds[key])
			az = key

	instanceId, ipAddress = ec2.get_oldest_instance(azInstanceIds[az])
	print "The oldest instance has ipAddress: %s" % ipAddress

	# Mark the oldest instance as retiring
	ec2.mark_instance_as_retiring()
