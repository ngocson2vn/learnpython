from inherit_base import InheritBase

print "\nCreating InheritBase ib:"
ib = InheritBase()
ib.baseid = 100
ib.counter = 5

print "\nCreating InheritBase ib2:"
ib2 = InheritBase()
ib2.baseid = 200
ib2.counter = 10

print ""
print "ib.baseid.id = %s" % id(ib.baseid)
print "ib2.baseid.id = %s" % id(ib2.baseid)
print "ib.counter.id = %s" % id(ib.counter)
print "ib2.counter.id = %s" % id(ib2.counter)

print ""
print "ib.baseid = %s" % ib.baseid
print "ib2.baseid = %s" % ib2.baseid

print ""
print "ib.counter = %s" % ib.counter
print "ib2.counter = %s" % ib2.counter

print ""
print "ib: %s" % ib
print "ib: %s" % ib.__repr__()
