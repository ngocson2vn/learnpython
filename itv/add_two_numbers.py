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
        out = []
        nextnode = self.head
        while nextnode is not None:
            out.append(str(nextnode.data))
            nextnode = nextnode.next
        print '->'.join(out)
            
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
    


def add_two_numbers(list1, list2):
    """
    1->8->3
    1->5
    
    1->8->3
    1->5->2
    
    1->8
    1->5->3
    """
    
    result = SLinkedList()
    carry = 0
    node1 = list1.head
    node2 = list2.head

    while node1 is not None and node2 is not None:
        value = node1.data + node2.data + carry
        if value >= 10:
            carry = 1
            result.append(Node(value % 10))
        else:
            result.append(Node(value))
            carry = 0
        node1 = node1.next
        node2 = node2.next
    
    while node1 is not None:
        value = node1.data + carry
        if value >= 10:
            carry = 1
            result.append(Node(value % 10))
        else:
            result.append(Node(value))
            carry = 0
        node1 = node1.next
        
    while node2 is not None:
        value = node2.data + carry
        if value >= 10:
            carry = 1
            result.append(Node(value % 10))
        else:
            result.append(Node(value))
            carry = 0
        node2 = node2.next
        
    if carry:
        result.append(Node(carry))
    
    return result


list1 = SLinkedList()
list1.append(Node(1))
list1.append(Node(8))
list1.append(Node(3))
list1.printlist()


list2 = SLinkedList()
list2.append(Node(1))
list2.append(Node(4))
list2.append(Node(9))
list2.printlist()

result = add_two_numbers(list1, list2)
result.printlist()


print
list1 = SLinkedList()
list1.append(Node(1))
list1.append(Node(8))
list1.append(Node(3))
list1.printlist()


list2 = SLinkedList()
list2.append(Node(4))
list2.append(Node(9))
list2.printlist()

result = add_two_numbers(list1, list2)
result.printlist()

print
list1 = SLinkedList()
list1.append(Node(8))
list1.append(Node(3))
list1.printlist()


list2 = SLinkedList()
list2.append(Node(4))
list2.append(Node(4))
list2.append(Node(9))
list2.printlist()

result = add_two_numbers(list1, list2)
result.printlist()

