#!/usr/bin/env python

import signal
import os
import time
import sys

ALARM_MAX = 2
ALARM_SECONDS = 5
alarm_count = 0
text = ""

def handler(signum, frame):
	print "Signal handler called with signal", signum
	signal.alarm(ALARM_SECONDS)
	global alarm_count
	alarm_count += 1
	if alarm_count == ALARM_MAX:
		signal.alarm(0)

	global text
	text = ""

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

while True:
	text += "."
	sys.stdout.write('\r')
	sys.stdout.write(text)
	sys.stdout.flush()

	if len(text) == 50:
		text = ""
		print text

	time.sleep(1)

# Disable the alarm
signal.alarm(0)
