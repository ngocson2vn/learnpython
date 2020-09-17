import random

def quicksort(seq):
  # Randomize the sequence first
  for i in range(len(seq)):
    j = random.randint(0, len(seq) - 1)
    tmp = seq[i]
    seq[i] = seq[j]
    seq[j] = tmp

  _sort(seq, 0, len(seq))

def _sort(seq, start, stop):
  if start >= stop - 1:
    return

  # pivotIndex ends up in between the two halves
  # where the pivot value is in its final location.
  pivotIndex = partition(seq, start, stop)
  _sort(seq, start, pivotIndex)
  _sort(seq, pivotIndex + 1, stop)

def partition(seq, start, stop):
  # pivotIndex comes from the start location in the list
  pivotIndex = start
  pivot = seq[pivotIndex]
  i = start + 1
  j = stop - 1

  while i <= j:
    while i <= j and seq[i] <= pivot:
      i += 1
    while i <= j and seq[j] > pivot:
      j -= 1

    # If i < j, then seq[i] > pivot and seq[j] < pivot,
    # we need to swap seq[i] for seq[j]
    if i < j:
      tmp = seq[i]
      seq[i] = seq[j]
      seq[j] = tmp
      i += 1
      j -= 1

  # Because i > j, seq[j] must be <= pivot
  seq[pivotIndex] = seq[j]
  seq[j] = pivot
  return j

