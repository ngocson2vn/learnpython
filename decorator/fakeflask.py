import hashlib
import pprint

class FakeFlask:
	def __init__(self, app_name):
		self.app_name = app_name
		self.handlers = {}

	def route(self, route, methods):
		def decorator(handler):
			for m in methods:
				h = hashlib.sha256((route + m.capitalize()).encode('utf-8')).hexdigest()
				self.handlers[h] = handler

		return decorator

	def run(self):
		pprint.PrettyPrinter(indent=2).pprint(self.handlers)
		print("Input * to quit")
		while True:
			matched = False
			route = input('route: ')
			if route == "*":
				print("Bye")
				break

			method = input('method: ')
			h = hashlib.sha256((route + method.capitalize()).encode('utf-8')).hexdigest()
			if h in self.handlers:
				matched = True
				r = self.handlers[h]()
				print("{}\n".format(r))

			if not matched:
				print("Could not find a match, please try different inputs.\n")
