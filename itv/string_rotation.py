#!/usr/bin/python

def is_substring(s1, s2):
    return s1 in s2

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return is_substring(s1, s2 + s2)

s1 = "foobarbaz"
s2 = "bazfoobar"
print is_rotation(s1, s2)

s1 = "barbazfoo"
s2 = "foobarbaz"
print is_rotation(s1, s2)