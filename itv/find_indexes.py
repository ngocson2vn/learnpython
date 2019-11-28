#!/usr/bin/python

def find_indexes(nums, target):
    if nums is None or target is None:
        raise TypeError("nums or target cannot be None")
    if not nums:
        raise ValueError("nums cannot be empty")
    
    cache = dict()
    for index, n in enumerate(nums):
        r = target - n
        if n in cache:
            return (cache[n], index)
        else:
            cache[r] = index
    return None


nums = [1, 3, 2, -7, 5]
target = 5
print find_indexes(nums, target)
