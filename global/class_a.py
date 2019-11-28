import base

class ClassA(base.Ca):
    def __init__(self):
        self.family = "AAA"
        base.Ca.__init__(self)

    def get_family(self):
        print self.family
