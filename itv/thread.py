#!/usr/bin/python

import threading
import time

class SampleThreading(threading.Thread):
	def __init__(self, thread_id, sleep_interval):
		super(SampleThreading, self).__init__()
		self.thread_id = thread_id
		self.sleep_interval = sleep_interval

	def run(self):
		for _ in xrange(10):
			print "Thread: %s" % self.thread_id
			time.sleep(self.sleep_interval)

thread1 = SampleThreading("Thread-1", 0.5)
thread2 = SampleThreading("Thread-2", 1)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print "Main thread finished"