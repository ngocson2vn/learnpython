#!/usr/bin/python

def count_flip_bits(a, b):
    x = a ^ b
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count

a = -9
b = 9
print "{0:032b}".format(a)
print "{0:032b}".format(b)
print count_flip_bits(a, b)