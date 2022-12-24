class Call:
	def __init__(self):
		self.name = "Call"
	
	def __call__(self):
		self.info()

	def get_name(self):
		return self.name
	
	def display(self):
		print self.get_name()

	def info(self):
		print "You are calling me!"
