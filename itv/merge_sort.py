#!/usr/bin/python

class MergeSort(object):
    """
    Merge sort can be a good choice for data sets that are too large to fit in memory, 
    as large chunks of data can be read and written to disk.
    """
    def sort(self, data):
        if data is None:
            raise TypeError("data cannot be None")
        return self._sort(data)
    
    def _sort(self, data):
        if len(data) < 2:
            return data
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        
        left = self._sort(left)
        right = self._sort(right)
        return self._merge(left, right)
    
    def _merge(self, left, right):
        l = 0
        r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        if l < len(left):
            result.extend(left[l:])
        if r < len(right):
            result.extend(right[r:])
        return result

data = [3, 4, 10, 12, 5, 6, 7, 100, 13, 14, 6, 7, 1]
print data, "\n"
ms = MergeSort()
print ms.sort(data)
