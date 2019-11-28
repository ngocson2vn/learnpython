#!/usr/bin/env python

import sys
import json

fname = sys.argv[1]
print(fname)

fd = open(fname)
rd = fd.read()
print(rd)
