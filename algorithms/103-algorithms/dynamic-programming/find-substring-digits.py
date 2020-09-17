def find_max_substring(s):
  # i is the starting index
  max_len = 0
  start = 0
  end = 0
  for i in range(len(s)):
    for j in range(i + 1, len(s), 2):
      len_sub = j - i + 1

      if max_len > len_sub:
        continue

      lsum = 0
      rsum = 0
      for k in range(len_sub // 2):
        lsum += int(s[i + k])
        rsum += int(s[i + k + len_sub // 2])

      if lsum == rsum:
        max_len = len_sub
        start = i
        end = j

  return max_len, start, end


s = "9430723"
max_len, start, end = find_max_substring(s)
print(max_len, start, end)
print(s[start:end + 1])