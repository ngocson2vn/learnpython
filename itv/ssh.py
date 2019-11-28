#!/usr/bin/python

import os
import sys
import paramiko
import json
from collections import OrderedDict

h = sys.argv[1]

home = os.environ.get("HOME")

key = paramiko.RSAKey.from_private_key_file("{home}/.ssh/id_rsa".format(home = home))
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname = "%s" % h, username = "nguyen.son", pkey = key)

stdin, stdout, stderr = client.exec_command("TERM=xterm top -n 1 -b | grep Cpu")
d = stdout.read().replace("\n", "").replace(",", "").split()[1:]
r = OrderedDict(zip(d[1::2], d[0::2]))
print json.dumps(r, indent=2)


while True:
  try:
    print next(stderr)
  except StopIteration:
    break
