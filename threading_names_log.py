import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
					format='[%(levelname)s] (%(threadName)-10s) %(message)s'	
				   )

def worker():
	logging.debug('Starting')
	time.sleep(0)
	logging.debug('Exiting')

def my_service():
	logging.debug('Starting')
	time.sleep(3)
	logging.debug('Exiting')


t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)

w.start()
w2.start()
t.start()
