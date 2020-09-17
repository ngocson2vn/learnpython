class Stack:
  def __init__(self):
    self.items = []

  def pop(self):
    if self.is_empty():
      raise RuntimeError("Attempt too pop an empty stack")
    topIdx = len(self.items) - 1
    item = self.items[topIdx]
    del self.items[topIdx]
    return item

  def push(self, item):
    self.items.append(item)

  def top(self):
    if self.is_empty():
      raise RuntimeError("Attempt to get top empty stack")
    topIdx = len(self.items) - 1
    return self.items[topIdx]

  def is_empty(self):
    return len(self.items) == 0
