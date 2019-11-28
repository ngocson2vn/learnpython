#!/usr/bin/python

def group_anagrams(data):
    if data is None:
        raise TypeError("data cannot be None")
    if len(data) < 2:
        return data
    
    ag = dict()
    for item in data:
        key = "".join(sorted(item))
        if key in ag:
            ag[key].append(item)
        else:
            ag[key] = [item]
    print ag
    result = []
    for a in ag.values():
        result.extend(a)
    return result

data = ['cat', 'tab', 'act', 'ram', 'bat', 'arm']
print data
print group_anagrams(data)