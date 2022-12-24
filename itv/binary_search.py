#!/usr/bin/python

def radix_sort(a, base=10):
	max_a = max(a)
	max_digits = len(str(max_a))
	current_array = a
	for i in xrange(max_digits):
		buckets = [[] for _ in xrange(base)]
		for item in current_array:
			buckets[(item // (base ** i)) % base].append(item)
		current_array = []
		for bucket in buckets:
			current_array.extend(bucket)
	return current_array





def binary_search(a, l, r, value):
	if l == r:
		if a[l] == value:
			return l
		else:
			return -1

  # 0 1 2 3 4
	mid = (r + l) // 2
	
	if value == a[mid]:
		return mid
	elif value < a[mid]:
		print mid, a[l:mid]
		index = binary_search(a, l, mid - 1, value)
	else:
		print mid, a[mid + 1:r + 1]
		index = binary_search(a, mid + 1, r, value)
	return index






a = [1, 20, 30, 9, 8, 6, 5, 40, 200, 9, 230, 110]
sorted_a = radix_sort(a)
print sorted_a
index = binary_search(sorted_a, 0, len(sorted_a) - 1, 230)
if index >= 0:
	print "a[{0}] = {1}".format(index, sorted_a[index])
else:
	print "Not found"