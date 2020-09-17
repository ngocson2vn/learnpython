#!/usr/bin/python

class RadixSort(object):
    def sort(self, data, base=10):
        if data is None:
            raise TypeError("data cannot be None")
        max_item = max(data)
        max_digits = len(str(abs(max_item)))
        arr = data
        for digit in xrange(max_digits):
            buckets = [[] for _ in xrange(base)]
            for item in arr:
                buckets[(item // base ** digit) % base].append(item)
            
            print "digit = {}".format(digit)
            print buckets
            del arr[:]
            for b in buckets:
                arr.extend(b)
            print arr, "\n"
        return arr

data = data = [3, 4, 10, 12, 350, 13, 100, 13, 270, 190, 910, 11, 14, 6, 7, 1]
print data, "\n"
sorted_data = RadixSort().sort(data)
print sorted_data