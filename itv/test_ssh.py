#!/usr/bin/python

import paramiko
import os
import sys

h = sys.argv[1]
user = sys.argv[2]

home = os.environ["HOME"]
key = paramiko.RSAKey.from_private_key_file("{home}/.ssh/id_rsa".format(home=home))
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=h, username=user, pkey=key)
print "Connected {0}@{1}".format(user, h)
_, stdout, stderr = client.exec_command("uname -a")
err = stderr.read()
out = stdout.read()
if len(err) > 0:
	print err
else:
	print out