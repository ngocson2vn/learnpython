split_count = 0

def mergeSort(seq):
  print("INIT")
  print(seq)
  print("=" * 100)
  mergeSortRecursively(seq, 0, len(seq))
  print("start = {}, stop = {}".format(0, len(seq)))
  print(seq)

def mergeSortRecursively(seq, start, stop):
  global split_count

  # if start == stop, then seq is empty and therefore start > stop - 1
  # Normally start == stop - 1
  if start >= stop - 1:
    return

  mid = (start + stop) // 2
  split_count += 1
  n = split_count

  mergeSortRecursively(seq, start, mid)
  print("SPLIT_NUMBER = {}, start = {}, stop = {}".format(n, start, mid))
  print(seq)
  print("=" * 100) if mid - start >= 2 else print()

  mergeSortRecursively(seq, mid, stop)
  print("SPLIT_NUMBER = {}, start = {}, stop = {}".format(n, mid, stop))
  print(seq)
  print("=" * 100) if stop - mid >= 2 else print()

  merge(seq, start, mid, stop)

def merge(seq, start, mid, stop):
  tempList = []
  i = start
  j = mid
  while i < mid and j < stop:
    if seq[i] < seq[j]:
      tempList.append(seq[i])
      i += 1
    else:
      tempList.append(seq[j])
      j += 1

  while i < mid:
    tempList.append(seq[i])
    i += 1

  N = start + len(tempList)
  seq[start:N] = tempList

seq = [1, 7, 20, 10, 5, 8, 2, 6, 30, 2, 80, 23, 90, 19, 0, 17]
mergeSort(seq)

#######################################
# Calculating Time Complexity
#######################################
"""
(1) Forward phase:
Start from the original sequence, we perform the following steps:
Step 1: we divide the original sequence into 2 sub sequences:
Step 2: we repeat the Step 1 for 2 sub sequences
Step 3: we repeat the Step 1 for 4 sub sequences
...
Step x: we repeat the Step 1 for m sub sequences

We need at most x = log(n) + 1 steps to divide the original sequence 
into y sub sequences so that each sub sequence contains only one element.

(2) Backward phase
We go from Step x backward to Step 1:
At each step, we merge pairs of sub sequences into ordered sub sequences.

So time complexity is O(n * log(n))
"""
