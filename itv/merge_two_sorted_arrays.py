#!/usr/bin/python

class RadixSort(object):
    def sort(self, data, base=10):
        if data is None:
            raise TypeError("data cannot be None")
        if len(data) < 2:
            return data
        max_item = max(data)
        max_digits = len(str(abs(max_item)))
        arr = data
        for digit in xrange(max_digits):
            buckets = [[] for _ in xrange(base)]
            for item in arr:
                buckets[(item // base ** digit) % base].append(item)
            del arr[:]
            for b in buckets:
                arr.extend(b)
        return arr

def merge_two_sorted_arrays(a, b):
    h = None
    for l in xrange(len(a)):
        if a[l] is None:
            h = l
            break

    max_a = max(a)
    l = 0
    for r in xrange(len(b)):
        if max_a <= b[r]:
            a[h:] = b[r:]
            return a

        for i in xrange(l, h):
            if a[i] > b[r]:
                a[i + 1:] = a[i:]
                a[i] = b[r]

                l = i + 1
                h = h + 1
                break
    return a

def merge(a, b):
    l = 0
    r = 0
    result = []
    while l < len(a) and r < len(b):
        if a[l] == b[r]:
            result.append(a[l])
            result.append(b[r])
            l += 1
            r += 1
        elif a[l] < b[r]:
            result.append(a[l])
            l += 1
        else:
            result.append(b[r])
            r += 1
    if l < len(a):
        result.extend(a[l:])
    elif r < len(b):
        result.extend(b[r:])
    return result


a = [1, 3, 2, 5, 100, 20, 1, 9]
b = [200, 10, 20, 5, 2, 240, 22]
rs = RadixSort()
a = rs.sort(a)
b = rs.sort(b)

# a.extend([None for _ in xrange(len(b))])
# print a
# print b
# print merge_two_sorted_arrays(a, b)

print a
print b
print merge(a, b)
