import sys

sys.path.append('.')
sys.path.append("./vendored")
from ec2 import ec2
from autoscaling import autoscaling

minSize, desiredCapacity, instanceIds = autoscaling.describe_auto_scaling_group('StagingTaskECSAutoScaleGroup')
print "OLDEST"
print ec2.get_oldest_instance(instanceIds)
print
print "LATEST"
print ec2.get_latest_instance(instanceIds)