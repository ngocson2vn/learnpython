str1 = "ABCDEF"
str2 = "APQBRF"

def find_lcs(str1, str2):
  # Terminating condition
  if len(str1) == 0 or len(str2) == 0:
    return 0

  # Main logic
  if str1[-1] == str2[-1]:
    return 1 + find_lcs(str1[:-1], str2[:-1])
  return max(find_lcs(str1, str2[:-1]), find_lcs(str1[:-1], str2))

print(find_lcs(str1, str2))

lcs = [
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
]

def find_lcs_dp(str1, str2):
  m = len(str1)
  n = len(str2)
  lcs = [[0] * m] * n
  
  if str1[0] == str2[0]:
    lcs[0][0] = 1

  for i in range(1, m):
    lcs[i][0] = lcs[i - 1][0]
    if str1[i] == str2[0]:
      lcs[i][0] = 1

  for j in range(1, n):
    lcs[0][j] = lcs[0][j - 1]
    if str1[0] == str2[j]:
      lcs[0][j] = 1

  for i in range(1, m):
    for j in range(1, n):
      if str1[i] == str2[j]:
        lcs[i][j] = lcs[i - 1][j - 1] + 1
      else:
        lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

  lcs_len = lcs[m - 1][n - 1]

  # Walk backwards to collect characters belonging to lcs
  lcs_str = []
  i = m - 1
  j = n - 1
  while i > 0 and j > 0:
    print("i = {}, j = {}".format(i, j))
    if str1[i] == str2[j]:
      lcs_str.append(str1[i])
      i -= 1
      j -= 1
    elif i > 0 and j > 0:
      if lcs[i - 1][j] > lcs[i][j - 1]:
        i -= 1
      else:
        j -= 1
      
  print("i = {}, j = {}".format(i, j))
  if i == 0 and j == 0:
    if lcs[0][0] > 0:
      lcs_str.append(str1[0])
  elif i == 0 and lcs[i][j] > 0:
    lcs_str.append(str1[i])
  elif lcs[i][j] > 0:
    lcs_str.append(str2[j])

  lcs_str.reverse()
  return lcs_str

print(find_lcs_dp(str1, str2))
