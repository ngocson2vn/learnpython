#!/usr/bin/python

import time

file = "/bin/cat"
fh = open(file, 'rb')

data = b''
byte = fh.read(1)
print type(byte)

while len(byte):
    print "%r" % byte
    byte = fh.read(1)
    time.sleep(2)
