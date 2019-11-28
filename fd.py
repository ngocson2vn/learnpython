#!/usr/bin/env python

import os
import time

print "Process ID = %s" % os.getpid()
print "Close stdin os.close(0)"
os.close(0)
os.open("/dev/null", os.O_RDONLY)

print "Close stdout os.close(1)"
os.close(1)
os.open("/tmp/fd26061985.log", os.O_CREAT | os.O_WRONLY)

print "You should see this text in file /tmp/fd26061985.log"

while 1:
	print "OK"
	time.sleep(1)
