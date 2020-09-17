#!/usr/bin/python

def reverse(string):
    print id(string)
    l = len(string)
    for i in xrange(0, l / 2):
        string[i], string[(l - 1) - i] = string[(l - 1) - i], string[i]

string = list("ABCDEFG")
print id(string)
print string, "\n"

reverse(string)
print string