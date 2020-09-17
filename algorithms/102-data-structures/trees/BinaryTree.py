class Node:
  def __init__(self, data):
    self.data = data
    self.left_child = None
    self.right_child = None

class Tree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    node = Node(data)
    if self.root is None:
      self.root = node
      return
    current = self.root
    parent = None
    while True:
      parent = current
      if node.data <= current.data:
        current = current.left_child
        if current is None:
          parent.left_child = node
          return
      else:
        current = current.right_child
        if current is None:
          parent.right_child = node
          return

  def get_node_with_parent(self, data):
    parent = None
    current = self.root
    while current:
      if data == current.data:
        return (parent, current)
      parent = current
      if data < current.data:
        current = current.left_child
      else:
        current = current.right_child
        
    return (None, None)

  def remove(self, data):
    parent, node = self.get_node_with_parent(data)
    if parent is None and node is None:
      return False
    
    # Get children count
    children_count = 0
    if node.left_child and node.right_child:
      children_count = 2
    elif node.left_child or node.right_child:
      children_count = 1

    if children_count == 0:
      if parent:
        if parent.left_child is node:
          parent.left_child = None
        else:
          parent.right_child = None
      # node is the root tree
      else:
        self.root = None
    elif children_count == 1:
      next_node = None
      if node.left_child:
        next_node = node.left_child
      else:
        next_node = node.right_child
      if parent:
        if parent.left_child is node:
          parent.left_child = next_node
        else:
          parent.right_child = next_node
      # node is the root tree
      else:
        self.root = next_node
    else:
      prev_node = node
      leftmost_node = node.right_child

      # Find the leftmost node
      while leftmost_node.left_child:
        prev_node = leftmost_node
        leftmost_node = leftmost_node.left_child

      # Replace node's data with the leftmost node's data
      node.data = current.data

      if prev_node.left_child is leftmost_node:
        prev_node.left_child = leftmost_node.right_child
      else:
        prev_node.right_child = leftmost_node.right_child

  def search(self, data):
    current = self.root
    while current:
      if data == current.data:
        return current
      elif data < current.data:
        current = current.left_child
      else:
        current = current.right_child
    return None
