#!/usr/bin/python

class PowerTwo:
	"""
	A custom iterator

	"""

	def __init__(self, max = 0):
		self.max = max

	def __iter__(self):
		self.n = 0
		return self

	def next(self):
		if self.n <= self.max:
			result = 2 ** self.n
			self.n += 1
			return result
		else:
			raise StopIteration


obj = PowerTwo(4)

pt = iter(obj)
print(next(pt))
print(next(pt))
print(next(pt))
print(next(pt))
print(next(pt))
