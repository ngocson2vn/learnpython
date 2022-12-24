#!/usr/bin/python

class SelectionSort(object):
	"""
	 i   j->
	[10, 9, 20, 5, 8, 16, 7]

	    i  j->
	[5, 9, 20, 10, 8, 16, 7]
	 

	"""
	def sort(self, arr):
		n = len(arr)
		for i in xrange(n):
			min_index = i
			for j in xrange(i + 1, n):
				if arr[j] < arr[min_index]:
					min_index = j
			a[i], a[min_index] = a[min_index], a[i]



a = [10, 9, 20, 5, 8, 16, 7, 1, 100, 78, 25, 22]
print a

SelectionSort().sort(a)
print
print a