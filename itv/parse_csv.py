#!/usr/bin/python

import csv
import sys

fname = sys.argv[1]
with open(fname) as csv_file_object:
	reader = csv.reader(csv_file_object)
	header = next(reader)
	for row in reader:
		d = zip(header, row)
		print(d)
		p = dict(d)
		if int(p['age']) >= 30:
			print p
			break
