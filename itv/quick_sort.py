#!/usr/bin/python

class QuickSort(object):
    def sort(self, data):
        if data is None:
            raise TypeError("data cannot be None")
        return self._sort(data)
    
    def _sort(self, data):
        if len(data) < 2:
            return data
        
        left = []
        right = []
        pivot = []
        
        mid = len(data) // 2
        pivot_value = data[mid]
        
        for item in data:
            if item == pivot_value:
                pivot.append(item)
            elif item < pivot_value:
                left.append(item)
            else:
                right.append(item)
        
        print left, pivot, right
        
        left = self._sort(left)
        right = self._sort(right)
        merged = left + pivot + right
        print merged
        return merged

data = [3, 4, 10, 12, 350, 13, 100, 13, 270, 190, 910, 11, 14, 6, 7, 1]
print data, "\n"
sorted_data = QuickSort().sort(data)
print sorted_data
        