import sys
import datetime

sys.path.append('.')
sys.path.append("./vendored")
from cloudwatch import cloudwatch

endTime = datetime.datetime.utcnow().replace(second=0, microsecond=0) - datetime.timedelta(minutes=1)
startTime = endTime - datetime.timedelta(minutes=15)

for i in xrange(1, 5):
	print "StartTime: %s" % startTime
	print "EndTime: %s" % endTime
	print cloudwatch.get_cluster_metric_value('StagingTask', 'CPUMemoryUtilizationNormalized', startTime, endTime)
	endTime = startTime
	startTime = endTime - datetime.timedelta(minutes=15)