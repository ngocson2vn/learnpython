# 1. Memorization (cache)
# 2. Tabulation   (Bottom up)

def find_longest_common_subsequence(s1, s2):
		row_count = len(s2) + 1
		col_count = len(s1) + 1
		m = [ [0] * row_count for _ in xrange(col_count) ]
		for i in xrange(1, col_count):
			for j in xrange(1, row_count):
				if s1[i - 1] == s2[j - 1]:
					m[i][j] = m[i - 1][j - 1] + 1
				else:
					m[i][j] = max(m[i - 1][j], m[i][j - 1])

		i = col_count - 1
		j = row_count - 1
		lcs = []
		while m[i][j]:
			if m[i][j] == m[i - 1][j]:
				i -= 1
			elif m[i][j] == m[i][j - 1]:
				j -= 1
			elif m[i][j] == m[i - 1][j - 1] + 1:
				lcs.append(s1[i - 1])
				i -= 1
				j -= 1

		print m[col_count - 1][row_count - 1], lcs[::-1]


s1 = "ABCDEFGHIJ"
s2 = "fECxFAGzDE"
find_longest_common_subsequence(s1, s2)