class EmptyQueueException(Exception):
    pass

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):
    """
        tail --> node <-- node <-- ... <-- node <-- head
    """


    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node
    
    def dequeue(self):
        if self.head is None:
            raise EmptyQueueException("Queue is empty")
        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return node.data
    
    def print_queue(self):
        node = self.head
        result = []
        while node is not None:
            result.append(str(node.data))
            node = node.next
        if len(result) > 0:
            print ['->'.join(result)]
        else: 
            print []


queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(9)
queue.enqueue(0)
queue.enqueue(6)
print "head: %s" % str(queue.head.data)
queue.print_queue()
print "tail: %s" % str(queue.tail.data)

print
print queue.dequeue()
queue.print_queue()

print
print queue.dequeue()
queue.print_queue()

print
print queue.dequeue()
queue.print_queue()

print
print queue.dequeue()
queue.print_queue()

print
print queue.dequeue()
queue.print_queue()

print
print queue.dequeue()
queue.print_queue()

print
print queue.dequeue()
queue.print_queue()

print
print queue.dequeue()
queue.print_queue()