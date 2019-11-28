import base_class
from base_class import Base

print Base.baseid
Base.baseid = 10
print Base.baseid

print "\n==> Creating a Base object:"
b = Base()
print "b.baseid = %s" % b.baseid

print "\n==> dir(b):"
print dir(b)

print "\n==> dir(base_class):"
print dir(base_class)

print "\n==> base_class.__package__:"
print base_class.__package__

print "\n==> Adding a new attribute to instance object"
b.counter = 100
print b.counter

print b