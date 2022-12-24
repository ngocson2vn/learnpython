#!/usr/bin/python

def insertion_sort(data):
    """
    Insertion sort works well for very small datasets where most of the input is already sorted.
    """
    
    if data is None:
        raise TypeError("data cannot be None")
    if len(data) < 2:
        return data
    for r in xrange(len(data)):
        print ("r = {}, data[r] = {}".format(r, data[r]))
        print data
        for l in xrange(r):
            if data[r] < data[l]:
                temp = data[r]
                data[l+1:r+1] = data[l:r]
                data[l] = temp
                print "l = {}, swap".format(l)
                break
            else:
                print "l = {}".format(l)
        print data, "\n"
    return data


data = [3, 4, 10, 12, 100, 13, 14, 6, 7, 1]
print data, "\n"
insertion_sort(data)
print data