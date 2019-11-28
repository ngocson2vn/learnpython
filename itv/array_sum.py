#!/usr/bin/python

"""
Add each number in an array until the sum equals the rest  of the array
"""
arr = [1, -2, 3, 2, 0, -1, 10, -9, 2]
arr_sum = sum(arr)
  
i_sum = 0
found = None

for i in range(0, len(arr)):
	i_sum += arr[i]
	if i_sum == (arr_sum - i_sum):
		found = i
		break

if found is None:
	print("No index found that satisfied the given requirement")
else:
	print("Array: {}".format(arr))
	print("Found index: {}".format(found))
	print("First: {}, Sum: {}".format(arr[:found + 1], sum(arr[:found + 1])))
	print("Second: {}, Sum: {}".format(arr[found + 1:], sum(arr[found + 1:])))
