#!/usr/bin/python

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def printlist(self):
        nextnode = self.head
        while nextnode is not None:
            print nextnode.data
            nextnode = nextnode.next
            
    def insert_at_start(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head = node
        
    def insert_at_end(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        nextnode = self.head
        while nextnode.next is not None:
            nextnode = nextnode.next
        nextnode.next = node
        self.tail = node
        
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
        self.tail = node

    def append(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def find_kth_to_last(self, k):
        """
        head-->[data|next]-->[data|next]-->[data|next]-->[data|next]-->[data|next]-->None
                   slow                       fast
                   
                   fast - slow = k
        """
        
        if k is None:
            raise TypeError("k cannot be None")

        fast = self.head
        slow = self.head
        for _ in xrange(k):
            fast = fast.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        return slow
    

def split_list(ls, value):
    left = SLinkedList()
    right = SLinkedList()
    
    node = ls.head
    while node is not None:
        if node.data < value:
            left.append(Node(node.data))
        elif node.data == value:
            right.insert_at_start(Node(node.data))
        else:
            right.append(Node(node.data))
        node = node.next
    
    left.tail.next = right.head
    left.tail = right.tail
    return left
    

# list1 = SLinkedList()
# list1.head = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")

# list1.head.next = e2
# e2.next = e3
# list1.printlist()

# print
# list1.insert_at_start(Node("Sun"))
# list1.printlist()

# print
# list1.insert_at_end(Node("Thur"))
# list1.printlist()

# print
# list1.insert_in_between(e2, Node("Mon2"))
# list1.printlist()

ls = SLinkedList()
ls.append(Node(1))
ls.append(Node(10))
ls.append(Node(2))
ls.append(Node(30))
ls.append(Node(5))
ls.append(Node(15))
ls.append(Node(7))
ls.append(Node(3))

ls.printlist()

print
print "tail: {}".format(ls.tail.data)


splitted_ls = split_list(ls, 15)

print
splitted_ls.printlist()

print
print "tail: {}".format(splitted_ls.tail.data)


# print
# print list1.find_kth_to_last(3).data

