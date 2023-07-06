import pathlib

path = pathlib.Path("/Users/bytedance/git/ngocson2vn/learnpython/devops/generators.py")
print(path.read_text())
bytes = path.read_bytes()

import json
from pprint import pprint
with open("policy.json") as opened_file:
  policy = json.load(opened_file)

pprint(policy)