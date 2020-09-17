class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return str(self.data)

class SinglyLinkedList:
  def __init__(self):
    self.tail = None
    self.head = None
    self.size = 0

  def append(self, data):
    node = Node(data)
    if self.head:
      self.head.next = node
      self.head = node
    else:
      self.tail = node
      self.head = node
    self.size += 1

  def __iter__(self):
    current = self.tail
    while current:
      data = current.data
      current = current.next
      yield data

  def __str__(self):
    s = "["
    for val in self.__iter__():
      if len(s) > 1:
        s += ", " + str(val)
      else:
        s += str(val)
    s += "]"
    return s

  def delete(self, data):
    prev = self.tail
    current = self.tail
    while current:
      if current.data == data:
        if current == self.tail:
          self.tail = current.next
        else:
          prev.next = current.next
        self.size -= 1
        return
      prev = current
      current = current.next

  def search(self, data):
    for val in self.__iter__():
      if val == data:
        return True
    return False

  def reverse(self):
    if self.size == 0 or self.size == 1:
      return
    prev = self.tail
    current = prev.next
    self.tail.next = None
    while current:
      nxt = current.next
      current.next = prev
      prev = current
      current = nxt
    self.head = self.tail
    self.tail = prev


def main():
  singlyList = SinglyLinkedList()
  singlyList.append("eggs")
  singlyList.append("ham")
  singlyList.append("spam")
  for item in singlyList:
    print(item)

if __name__ == "__main__":
  main()
