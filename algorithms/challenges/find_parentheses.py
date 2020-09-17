#!/usr/bin/python

"""
1 -> ["()"]
2 -> ["(())", "()()"]
3 -> ["((()))", "(()())", "(())()", "()(())", "()()()"]

"""


def find_pair(nleft, nright, curr_results, results):
	if nleft == 0 and nright == 0:
		results.append(''.join(curr_results))
	else:
		if nleft > 0:
			find_pair(nleft - 1, nright, curr_results + ['('], results)
		if nright > nleft:
			find_pair(nleft, nright - 1, curr_results + [')'], results)

num_pairs = 14
results = []
curr_results = []
find_pair(num_pairs, num_pairs, curr_results, results)
for p in results[:10]:
	print p