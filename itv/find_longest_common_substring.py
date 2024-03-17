def find_longest_common_substring(s1, s2):
		row_count = len(s2) + 1
		col_count = len(s1) + 1
		
		m = [ [0] * row_count for _ in range(col_count) ]

		length = 0
		index = -1

		for i in range(1, col_count):
			for j in range(1, row_count):
				if s1[i - 1] == s2[j - 1]:
					m[i][j] = m[i - 1][j - 1] + 1
					if m[i][j] > length:
						length = m[i][j]
						index = i

		if index >= 0:
			print(s1[(index - length):index])

s1 = "ABCDEFGHIJ"
s2 = "fBCDEFGxyzABCDEFGHI"
find_longest_common_substring(s1, s2)