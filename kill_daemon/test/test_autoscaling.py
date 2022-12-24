import sys

sys.path.append('.')
sys.path.append("./vendored")
from autoscaling import autoscaling

asGroupName = 'StagingTaskECSAutoScaleGroup'
minSize, desiredCapacity, instanceIds = autoscaling.describe_auto_scaling_group(asGroupName)
print instanceIds

count = 0
az = ''
for key in instanceIds.keys():
  if len(instanceIds[key]) > count:
    count = len(instanceIds[key])
    az = key
print az, instanceIds[az]