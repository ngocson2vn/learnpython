import logging
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

def lock_holder(lock):
	logging.debug('Starting')
	while True:
		

def worker(c):
	

logging.debug('Waiting for worker threads')
main_thread = threading.currentThread()
for t in threading.enumerate():
	if t is not main_thread:
		t.join()

logging.debug('Counter: %d', counter.value)