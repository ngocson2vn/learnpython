#!/usr/bin/python

class Node(object):
    def __init__(self, data):
        if data is None:
            raise TypeError("data cannot be None")
        self.data = data
        self.left = None
        self.right = None
        
    def _insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left._insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right._insert(data)
        else:
            return
    
    def _traverse(self, indent):
        print " " * indent, self.data
        rindent = indent
        if self.left is not None:
            # print "Left to {0}".format(self.data)
            if indent - 4 >= 0:
                indent -= 4
            self.left._traverse(indent)
        if self.right is not None:
            # print "Right to {0}".format(self.data)
            rindent += 8
            self.right._traverse(rindent)

class BinaryTree(object):
    def __init__(self, root_data):
        if root_data is None:
            raise TypeError("Root data cannot be None")
        self.root = Node(root_data)
    
    def insert(self, data):
        self.root._insert(data)
    
    def traverse(self, indent=0):
        print " " * indent, self.data
        self.root._traverse(indent)

bt = BinaryTree(1000)
bt.insert(3)
bt.insert(30)
bt.insert(63)
bt.insert(124)
bt.insert(1243)
bt.insert(5243)
bt.insert(90)
bt.insert(999)
bt.insert(9912)
bt.insert(1)

bt.traverse(indent=100)