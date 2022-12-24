import os
import sys
import base64
import StringIO

sys.path.append("./vendored")
import paramiko

STAGE = os.environ['STAGE']
RO_AWS_ID = os.environ['RO_AWS_ID']
RO_AWS_KEY = os.environ['RO_AWS_KEY']
SLACK_POST_URL = os.environ['SLACK_POST_URL']
S3_KILL_DAEMON_PROG = os.environ['S3_KILL_DAEMON_PROG']

def kill_daemon(event, context):
	instanceIPAddress = event['ip']
	print "instanceIPAddress: %s" % instanceIPAddress

	keydata = base64.b64decode(event['keydata'])

	k = paramiko.RSAKey.from_private_key(StringIO.StringIO(keydata))
	sshClient = paramiko.SSHClient()
	sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	print "Connecting to " + instanceIPAddress
	sshClient.connect(hostname=instanceIPAddress, username="ec2-user", pkey=k)
	print "Connected to " + instanceIPAddress

	commands = [
		"AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s aws s3 cp --region ap-northeast-1 %s /home/ec2-user/kill_daemon" % (RO_AWS_ID, RO_AWS_KEY, S3_KILL_DAEMON_PROG),
		"chmod 700 /home/ec2-user/kill_daemon",
		"AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s ECS_CLUSTER_NAME=%s SLACK_POST_URL=%s /home/ec2-user/kill_daemon" % (RO_AWS_ID, RO_AWS_KEY, STAGE, SLACK_POST_URL)
	]

	for command in commands:
		print "Executing %s" % command
		stdin, stdout, stderr = sshClient.exec_command(command)
		print stdout.read()
		err = stderr.read()
		if err is not None and len(err) > 0:
			print err
			return {'message': err, 'status': 'FAILURE'}

	return {'message': 'All deamons in %s have been killed' % instanceIPAddress, 'status': 'SUCCESS'}