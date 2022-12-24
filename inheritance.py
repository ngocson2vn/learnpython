#!/usr/bin/env python

from class_b import ClassB
from class_a import ClassA
from my_class import MyClass

a = ClassA()
b = ClassB()
b.get_family()
c = [a] + [b]
print c, "\n"
print b.__class__

print "\n== MyClass =="
mc = MyClass()
print "mc =", mc
print "mc.i =", mc.i
mc.i = 10
print "mc.i =", mc.i

print "mc.f() =", mc.f()

print "dir(mc) =", dir(mc)

