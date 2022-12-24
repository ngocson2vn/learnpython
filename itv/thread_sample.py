import threading

x = 0

def increment():
	global x
	x += 1

def mine(lock):
	for i in xrange(1000):
		lock.acquire()
		increment()
		lock.release()

def main():
	global x
	x = 0
	
	lock = threading.Lock()
	t1 = threading.Thread(target=mine, args=(lock,))
	t2 = threading.Thread(target=mine, args=(lock,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()

if __name__ == "__main__":
	for i in xrange(100):
		main()
		print("Iteration {0}: x = {1}".format(i, x))