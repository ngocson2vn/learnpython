#!/usr/bin/python

def find_diff_xor(s1, s2):
    result = 0
    for c in s1:
        result = result ^ ord(c)
    for c in s2:
        result = result ^ ord(c)
    
    diff = chr(result)
    return diff if diff in s1 or diff in s2 else None

s1 = "Son Nguyen"
s2 = "Son Ngxuyen"

print find_diff_xor(s1, s2)