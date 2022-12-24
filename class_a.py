from base_class import Base

class ClassA(Base):
	def __init__(self):
		self.family = "AAA"
		print "Initialize ClassA"

	def get_family(self):
		print self.family
