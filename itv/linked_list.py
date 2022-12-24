#!/usr/bin/python

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        nextnode = self.head
        while nextnode is not None:
            print nextnode.data
            nextnode = nextnode.next
            
    def insert_at_start(self, node):
        node.next = self.head
        self.head = node
        
    def insert_at_end(self, node):
        if self.head is None:
            self.head = node
            return
        nextnode = self.head
        while nextnode.next is not None:
            nextnode = nextnode.next
        nextnode.next = node
        
    def insert_in_between(self, node, new_node):
        if node is None:
            raise TypeError("node cannot be none")
        new_node.next = node.next
        node.next = new_node
        
    def remove_duplicates(self):
        if self.head is None:
            return
        
        node = self.head
        seen = set({node.data})
        while node.next is not None:
            if node.next.data in seen:
                node.next = node.next.next
            else:
                node = node.next
                seen.add(node.data)
        
"""
[data|next]---->[data|next]---->[data|next]---> None
    node
"""


list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.head.next = e2
e2.next = e3
list1.printlist()

print
list1.insert_at_start(Node("Sun"))
list1.printlist()

print
list1.insert_at_end(Node("Thur"))
list1.printlist()

print 
list1.insert_in_between(e2, Node("Mon"))
list1.printlist()

print
list1.remove_duplicates()
list1.printlist()