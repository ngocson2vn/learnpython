#!/usr/bin/python

MAX_BITS = 32

def decimal_fraction_to_binary(num):
    if num is None or num >= 1 or num <= 0:
        return 'ERROR'
    result = ['0', '.']
    while True:
        num = num * 2
        if num >= 1:
            result.append('1')
            num = num - 1
        else:
            result.append('0')
        
        if num == 0:
            return ''.join(result)
            
        if len(result) > MAX_BITS:
            return 'ERROR'

print decimal_fraction_to_binary(0.5)
print decimal_fraction_to_binary(0.25)
print decimal_fraction_to_binary(0.125)
print decimal_fraction_to_binary(0.625)
print decimal_fraction_to_binary(0.981)
print decimal_fraction_to_binary(0.987654321)