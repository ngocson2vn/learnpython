#! /usr/bin/env python

def fib(n):
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a + b

# Now call the function we just defined:
fib(2000)
