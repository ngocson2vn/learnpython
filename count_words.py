#!/usr/bin/python

import sys
import json
import re
from collections import OrderedDict

fname = sys.argv[1]
n = int(sys.argv[2])
word_dict = {}
regx = re.compile(r'([A-Za-z]+)')

with open(fname) as f:
	for line in f:
		words = line.split()
		for raw_word in words:
			match = regx.match(raw_word)
			if match:
				w = match.group()
				if w in word_dict:
					word_dict[w] += 1
				else:
					word_dict[w] = 1

sorted_list = sorted(word_dict.items(), key=lambda kv: kv[1], reverse=True)
ordered_dict = OrderedDict(sorted_list[:n])
print json.dumps(ordered_dict, indent=2)