#! /usr/bin/env python

class Mapping:
	"""Mapping class"""

	def __init__(self):
		self.__update()

	def update(self):
		self.name = 'Mapping'
		print "_Mapping_name:", self.name

	__update = update

class MappingSubclass(Mapping):
	"Subclass of Mapping"

	def update(self):
		self.name = 'MappingSubclass'
		print self.__class__, self.name

ms = MappingSubclass()
ms.update()
