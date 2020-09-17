#!/usr/bin/python

def compress(string):
    if string is None or not string:
        return string
    prev_char = string[0]
    count = 0
    result = ""
    for char in string:
        if char == prev_char:
            count += 1
        else:
            result += calc_partial_result(prev_char, count)
            prev_char = char
            count = 1
    result += calc_partial_result(prev_char, count)
    return result if len(result) < len(string) else string
    
def calc_partial_result(char, count):
    return char + (str(count) if count > 1 else "")

string = "AAABBCCCDDDEFG"
print compress(string)