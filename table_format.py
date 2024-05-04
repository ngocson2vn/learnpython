import json

class DictObj:
  def __init__(self, in_dict):
    assert isinstance(in_dict, dict)
    for key, val in in_dict.items():
      if isinstance(val, (list, tuple)):
        setattr(self, key, [DictObj(x) if isinstance(x, dict) else x for x in val])
      else:
        setattr(self, key, DictObj(val) if isinstance(val, dict) else val)

nodes = {
  "nodes": [
    {"name": "node1", "op": "op1"},
    {"name": "node2", "op": "op2"},
    {"name": "node3", "op": "op3"}
  ]
}

obj = DictObj(nodes)

idx = 0
print("{0:10} {1:20} {2:20}".format("Index", "Name", "Op"))
print("-" * (10+20+20))
for node in obj.nodes:
  print("{0:10} {1:20} {2:20}".format(str(idx), node.name, node.op))
  idx += 1
