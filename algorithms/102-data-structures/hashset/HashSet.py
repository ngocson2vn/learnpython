import json

class HashSet():
  print("Welcome to HashSet")

  def __init__(self, contents=[]):
    self.items = [None] * 10
    self.numItems = 0
    for item in contents:
      self.add(item)

  def __contains__(self, item):
    idx = hash(item) % len(self.items)
    while self.items[idx] != None:
      if self.items[idx] == item:
        return True
      idx = (idx + 1) % len(self.items)
    return False

  def __iter__(self):
    for i in range(len(self.items)):
      if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
        yield self.items[i]

  def add(self, item):
    if HashSet.__add(item, self.items):
      self.numItems += 1
      load = max(self.numItems, 10) / len(self.items)
      if load >= 0.75:
        self.items = HashSet.__rehash(self.items, [None] * 2 * len(self.items))

  def remove(self, item):
    if HashSet.__remove(item, self.items):
      self.numItems -= 1
      load = max(self.numItems, 10) / len(self.items)
      if load <= 0.25:
        self.items = HashSet.__rehash(self.items, [None] * (len(self.items) // 2))
    else:
      raise KeyError("Item not in HashSet")

  class __Placeholder:
    def __init__(self):
      pass

    def __eq__(self, other):
      return False

  def __add(item, items):
    idx = hash(item) % len(items)
    loc = -1

    # Linear probing
    while items[idx] != None:
      if items[idx] == item:
        return False
      if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
        loc = idx
      idx = (idx + 1) % len(items)

    if loc < 0:
      loc = idx
    items[loc] = item
    return True

  def __rehash(oldList, newList):
    for x in oldList:
      if x != None and type(x) != HashSet.__Placeholder:
        HashSet.__add(x, newList)
    return newList

  def __remove(item, items):
    idx = hash(item) % len(items)

    while items[idx] != None:
      if items[idx] == item:
        nextIdx = (idx + 1) % len(items)
        if items[nextIdx] == None:
          items[idx] = None
        else:
          items[idx] = HashSet.__Placeholder()
        return True
      idx = (idx + 1) % len(items)
    return False
