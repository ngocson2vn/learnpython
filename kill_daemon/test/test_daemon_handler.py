#!/usr/bin/python
import sys
import json

sys.path.append('.')
sys.path.append("./vendored")
import daemon_handler
from ec2 import ec2
from s3 import s3
from autoscaling import autoscaling

STAGE = 'Staging'

minSize, desiredCapacity, instanceIds = autoscaling.describe_auto_scaling_group(asGroupName)
instanceId, ipAddress = ec2.get_oldest_instance(instanceIds)
print "ipAddress: %s" % ipAddress

stage = STAGE.lower()
sshkey = 'ecs-%s.pem' % stage
print "SSH key: %s" % sshkey

s3.get_object('finc-secrets', 'ssh-key/%s' % sshkey, '/tmp/%s' % sshkey)
if not os.path.exists('/tmp/%s' % sshkey):
	print '/tmp/%s does not exist' % sshkey
	sys.exit(1)

keydata = ''
with open('/tmp/%s' % sshkey, 'rb') as fd:
	keydata = base64.b64encode(fd.read())

event = {'ip': ipAddress, 'keydata': keydata}
daemon_handler.kill_daemon(event, 0)
