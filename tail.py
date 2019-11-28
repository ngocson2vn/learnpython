#!/usr/bin/python

import sys
import os
import time

fname = sys.argv[1]
with open(fname) as f:
	f.seek(0, 2)
	while True:
		line = f.readline()
		if len(line) > 0:
			sys.stdout.write(line)
		else:
			time.sleep(0.001)
