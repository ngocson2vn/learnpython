#!/usr/bin/python

def validate_index(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if arg < 0:
                raise IndexError("index cannot be negative")
        return func(self, *args, **kwargs)
    return wrapper

class Bit(object):
    
    def __init__(self, number):
        self.number = number
    
    @validate_index
    def get_bit(self, index):
        mask = 1 << index
        return (self.number & mask) != 0
    
    @validate_index
    def set_bit(self, index):
        mask = 1 << index
        self.number = self.number | mask
        return self.number
    
    @validate_index
    def clear_bit(self, index):
        mask = ~(1 << index)
        self.number = self.number & mask
        return self.number
    
    @validate_index
    def clear_bits_msb_to_index(self, index):
        mask = (1 << index) - 1
        self.number = self.number & mask
        return self.number
    
    @validate_index
    def clear_bits_index_to_lsb(self, index):
        mask = ~((1 << index + 1) - 1)
        self.number = self.number & mask
        return self.number

number = 42
print "{0:08b}".format(number)

bit = Bit(42)
print bit.get_bit(3)

bit = Bit(42)
print "{0:08b}".format(bit.set_bit(3))

bit = Bit(42)
print "{0:08b}".format(bit.clear_bit(3))

bit = Bit(42)
print "{0:08b}".format(bit.clear_bits_index_to_lsb(3))

bit = Bit(42)
print "{0:08b}".format(bit.clear_bits_msb_to_index(3))