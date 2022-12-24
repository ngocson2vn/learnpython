#!/usr/bin/env python

import os
import time

print "\nPID = ", os.getpid()
print "\nCreate pipe\n"
fd_r, fd_w = os.pipe()
os.close(fd_r)

print "Duplicate fd_w to fd 20\n"
os.dup2(fd_w, 20)

time.sleep(30)
print "Write to fd 20\n"
os.write(20, "test")

print "Read from fd_r\n"
print "Read text:", os.read(fd_r, 10)

time.sleep(120)

os.close(fd_w)
os.close(20)
