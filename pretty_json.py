#!/usr/bin/python

import json

d = {"index": {"number_of_replicas": 0}}
print json.dumps(d, indent=4, sort_keys=True)
