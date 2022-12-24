# LIS: Longest Increasing Subsequence
# LIS(i) = 1 + max(LIS(j)), where, 0 < j < i and arr[j] < a[i]

def calculate(arr, i, cache, prev):
	if i in cache:
		return cache[i]

	max_sub_lis = 0
	for j in xrange(i):
		ret = calculate(arr, j, cache, prev)
		if arr[j] < arr[i] and ret > max_sub_lis:
			max_sub_lis = ret
			prev[i] = j

	cache[i] = max_sub_lis + 1

	return cache[i]

def lis(arr):	
	cache = {}
	cache[0] = 1

	prev = {}
	results = []

	calculate(arr, len(arr) - 1, cache, prev)

	items = sorted(cache.items(), key=lambda kv: kv[1])
	index = items[-1][0]
	results.append(arr[index])
	print index
	print prev
	
	while index in prev:
		index = prev[index]
		results.append(arr[index])

	return len(results), results[::-1]


# Driver program to test the above function 
arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60, 2, 8, 35, 90]
# arr = [3, 4, -1, 0, 6, 2, 3]
length, results = lis(arr)
print "length = {0}, results = {1}".format(length, results)
