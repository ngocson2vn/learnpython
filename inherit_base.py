from base_class import Base

class InheritBase(Base):

    counter = 0

    def __init__(self):
        print "In constructor of InheritBase"

    def display(self):
        print "This is a subclass of Base class"
        print dir(self)