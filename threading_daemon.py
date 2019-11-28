import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s'
				   )

def daemon():
	logging.debug('Starting')
	time.sleep(10)
	logging.debug('Exiting')

def non_daemon():
	logging.debug('Starting')
	time.sleep(2)
	logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

print threading.currentThread().getName(), 'Starting'
d.start()
t.start()
print threading.currentThread().getName(), 'Waiting'

d.join()

#time.sleep(10)
