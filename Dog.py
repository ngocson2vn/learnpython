#! /usr/bin/env python

class Dog:
	"""Dog class"""

	kind = 'canine'

	def __init__(self, name):
		self.name = name

d = Dog('Fido')
d.height = 5

e = Dog('Buddy')
e.speed = 20

print "d.kind:", d.kind
print "e.kind:", e.kind
print "d.name:", d.name
print "e.name:", e.name
print "d.height:", d.height
print "e.speed:", e.speed
