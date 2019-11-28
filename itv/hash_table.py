#!/usr/bin/python

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return str((str(self.key), str(self.value)))

    def __repr__(self):
        return str((str(self.key), str(self.value)))

    
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in xrange(size)]
        
    def __str__(self):
        return str(self.table)
    
    def _hash_function(self, key):
        return key % self.size
    
    def set(self, key, value):
        slot = self._hash_function(key)
        for item in self.table[slot]:
            if item.key == key:
                item.value = value
                return
        self.table[slot].append(Item(key, value))
        
    def get(self, key):
        slot = self._hash_function(key)
        for item in self.table[slot]:
            if item.key == key:
                return item.value
        raise KeyError("The given key was not present in the hash table.")
        
    def remove(self, key):
        slot = self._hash_function(key)
        for index, item in enumerate(self.table[slot]):
            if item.key == key:
                del self.table[slot][index]
                return
        raise KeyError("The given key was not present in the hash table.")


h = HashTable(10)
h.set(10, 20)
h.set(11, 21)
h.set(12, 22)
h.set(13, 23)
h.set(20, 30)
h.set(22, 31)

print h, "\n"
print h.get(13), "\n"

h.remove(22)
print h, "\n"