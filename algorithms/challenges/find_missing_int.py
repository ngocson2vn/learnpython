#!/usr/bin/python
import sys
import subprocess

p = subprocess.Popen("pip install bitstring", shell=True)
p.wait()
sys.path.append(".local/lib/python2.7/site-packages")
from bitstring import BitArray


def find_missing_int(ints, max_size):
    bits = BitArray(max_size)
    print sys.getsizeof(bits)
    for i in ints:
        bits[i] = True
    for index, value in enumerate(bits):
        if not value:
            return index
            
n = 32
ints = []
for i in xrange(10):
    ints.append(i)
for i in xrange(11, n):
    ints.append(i)

print find_missing_int(ints, n)