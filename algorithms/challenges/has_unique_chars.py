#!/usr/bin/python

def has_unique_chars_v1(string):
    if string is None:
        return False
    return len(set(string)) == len(string)

def has_unique_chars_v2(string):
    if string is None:
        return False
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True
            
def has_unique_chars_v3(string):
    if string is None:
        return False
    for char in string:
        if string.count(char) > 1:
            return False
    return True

string = "Hoa Nguyen"

print has_unique_chars_v1(string)
print has_unique_chars_v2(string)
print has_unique_chars_v3(string)