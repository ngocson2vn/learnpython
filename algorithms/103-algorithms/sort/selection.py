def select(start, seq):
  minIndex = start
  for i in range(start + 1, len(seq)):
    if seq[i] < seq[minIndex]:
      minIndex = i
  return minIndex

def selection_sort(seq):
  for i in range(len(seq) - 1):
    minIndex = select(i, seq)
    tmp = seq[i]
    seq[i] = seq[minIndex]
    seq[minIndex] = tmp

def main():
  seq = [5, 8, 2, 6, 9, 1, 0, 7]
  print(seq)
  selection_sort(seq)
  print(seq)

if __name__ == '__main__':
  main()