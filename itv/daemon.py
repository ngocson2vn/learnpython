#!/usr/bin/python

import os
import sys
import time

class SampleServer(object):
	def __init__(self, config):
		self.config = config

	def daemonize(self):
		child_pid = os.fork()
		if child_pid > 0:
			return

		# Child process
		print os.getpid()

		try:
			if "logfile" in self.config:
				logger = open(self.config["logfile"], "a")
			else:
				logger = open('/tmp/sample_server.log', "a")
		except IOError as ioe:
			print ioe
			return

		# Leave control terminal
		os.setsid()
		os.close(sys.stdin.fileno())
		os.close(sys.stdout.fileno())
		os.close(sys.stderr.fileno())
		while True:
			try:
				logger.write("Processing data\n")
				logger.flush()
				time.sleep(1)
			except Exception as ex:
				print logger.write("%s\n" % ex)
				logger.close()

server = SampleServer({'logfile': '/tmp/sample_server.log'})
server.daemonize()