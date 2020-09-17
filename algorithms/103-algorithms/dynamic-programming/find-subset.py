seq = [3, 2, 7, 1]
X = 6

def find_subset(seq, X):
  # Terminating condition
  if X == 0:
    return True
  if len(seq) == 0:
    return False

  # Computational Logic
  if seq[0] > X:
    return find_subset(seq[1:], X)

  return find_subset(seq[1:], X - seq[0]) or find_subset(seq[1:], X)


print(find_subset(seq, X))


def find_subset_db(seq, X):
  cache = [[False] * len(seq)] * (X + 1)
  for i in range(1, X + 1):
    if i == seq[0]:
      cache[i][0] = True

  for j in range(len(seq)):
    if seq[j] == 1:
      cache[1][j] = True

  for i in range(2, X + 1):
    for j in range(1, len(seq)):
      if cache[i][j - 1]:
        cache[i][j] = True
      elif seq[j] == i:
        cache[i][j] = True
      elif i > seq[j]:
        cache[i][j] = cache[i - seq[j]][j - 1]
      else:
        cache[i][j] = False
  return cache[X][len(seq) - 1]

  
