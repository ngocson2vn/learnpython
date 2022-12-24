#!/usr/bin/python

import sys
import json

fname = sys.argv[1]

with open(fname) as json_file_object:
  d = json.load(json_file_object)
  for p in d["people"]:
    if p["age"] >= 30:
      print p
      break
