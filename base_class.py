import md5


class Base:
    """A simple base class"""

    baseid = 1

    def __init__(self):
        hash = md5.new()
        hash.update("Son")
        self.name = hash.digest()
        print "Calling Base.__init__"

    def __repr__(self):
    	return self.__class__.__module__ + "." + self.__class__.__name__

    def info(self):
        return "This is Base class"
