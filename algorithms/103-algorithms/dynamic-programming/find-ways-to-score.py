"""
Consider a game where a player can score 3, 5 or 10 points in one move.
Given a total score of 13, find the total number of unique ways to reach a score of 13.
"""

def find_ways(N):
  if N < 0:
    return 0
  if N == 0:
    return 1

  # First move, score = 3
  x = find_ways(N - 3)

  # First move, score = 5
  y = find_ways(N - 5)

  # First move, score = 10
  z = find_ways(N - 10)

  return x + y + z

print(find_ways(13))
print(find_ways(15))


def find_ways_dp(N):
  if N < 3:
    return 0

  ways = [0] * (N + 1)
  ways[0] = 1
  ways[1] = 0
  ways[2] = 0

  for n in range(3, N + 1):
    if n - 3 >= 0:
      ways[n] += ways[n - 3]
    if n - 5 >= 0:
      ways[n] += ways[n - 5]
    if n - 10 >= 0:
      ways[n] += ways[n - 10]

  return ways[N]

print(find_ways_dp(13))
print(find_ways(15))