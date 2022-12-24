from time import time
import json



# A Dynamic Programming problem has 2 properties:
# 1. Overlapping subproblems
#			f(n) = f(n - 2) + f(n - 1)
# 2. Optimal Substructures
#			shortest_path(u --- x --- v) = shortest_path(u --- x) + shortest_path(x --- v)

# Suppose we have n items, and find_max_value(items) is the function that calculate max_value.
# max_value = max(value of nth item + find_max_value(total_weight - weight of nth item, items - nth item), 
#                 find_max_value(total_weight, items - nth item))




#A naive recursive implementation of 0 - 1 Knapsack Problem

# Returns the maximum value that can be put in a knapsack of
# capacity 
def knapSack(W, wt, val, n):
	# Base Case
	if n == 0 or W == 0:
		return 0

	# If weight of the nth item is more than Knapsack of capacity
	# W, then this item cannot be included in the optimal solution
	if (wt[n - 1] > W):
		return knapSack(W, wt, val, n - 1)

	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		v1 = knapSack(W, wt, val, n - 1)
		v2 = knapSack(W - wt[n - 1], wt, val, n - 1) + val[n - 1]
		return max(v1, v2)








# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def ks(W, wt, val, n, K):
	for i in xrange(n + 1):
		for w in xrange(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i - 1] <= w:
				K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
			else:
				K[i][w] = K[i - 1][w]

	results = []
	i = n
	w = W
	while w >= 0 and i >= 0:
		if K[i][w] == K[i - 1][w]:
			i -= 1
		elif K[i][w] == K[i][w - 1]:
			w -= 1
		else:
			results.append(i - 1)
			w -= wt[i - 1]
			i -= 1

	return K[n][W], results









# To test above function
val = [60, 100, 120, 30, 20, 200, 22, 53, 29]
wt = [10, 20, 30, 9, 11, 23, 99, 5, 33]
W = 50
n = len(val)

t1 = time()
max_value = knapSack(W, wt, val, n)
t2 = time()
print max_value
print t2 - t1

t1 = time()
K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
max_value, results = ks(W, wt, val, n, K)
t2 = time()
print
print max_value
for i in results:
	print (wt[i], val[i])
print t2 - t1
