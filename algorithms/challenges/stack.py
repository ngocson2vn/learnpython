#!/usr/bin/python

class StackFullException(Exception):
    pass

class Node(object):
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

class Stack(object):
    def __init__(self, size):
        self.size = size
        self.top = None
        
    def push(self, data):
        if len(self.stack) == self.size:
            raise StackFullException("Stack was full")
        node = Node(data, self.top)
        self.top = node
        return True
    
    def pop(self):
        if self.is_empty():
            return None
        node = self.top

        self.top = self.top.next
        node.next = None
        return node.data
    
    def peek(self):
        return self.top.data if self.top is not None else None
    
    def is_empty(self):
        return self.top is None
    
    def print_stack(self):
        node = self.top
        result = []
        while node is not None:
            result.append(str(node.data))
            node = node.next
        print '->'.join(result)
        

stack = Stack(10)
stack.push(1)
stack.push(19)
stack.push(3)
stack.push(5)
stack.push(8)
stack.push(5)
stack.push(8)
stack.push(8)
stack.push(7)
stack.push(9)
stack.print_stack()