from class_a import ClassA

class ClassB(ClassA):
	def __init__(self):
		self.name = "NameB"
	#	ClassA.__init__(self)

	def get_name(self):
		print self.name
