import base

class ClassB(base.Cb):
    def __init__(self):
        self.name = "NameB"
        base.Cb.__init__(self)

    def get_name(self):
        print self.name
