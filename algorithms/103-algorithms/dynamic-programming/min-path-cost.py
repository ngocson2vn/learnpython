costs = [
  [1, 3, 5, 8],
  [4, 2, 1, 7],
  [4, 3, 2, 3]
]

def min_path_cost(costs, m, n):
  if m == 0 and n == 0:
    return costs[m][n]
  elif m == 0:
    return min_path_cost(costs, m, n - 1) + costs[m][n]
  elif n == 0:
    return min_path_cost(costs, m - 1, n) + costs[m][n]

  x = min_path_cost(costs, m - 1, n)
  y = min_path_cost(costs, m, n - 1)
  return min(x, y) + costs[m][n]

min_costs = [
  [None] * 4,
  [None] * 4,
  [None] * 4
]
def min_path_cost_v2(costs, m, n):
  if min_costs[m][n]:
    return min_costs[m][n]
  if m == 0 and n == 0:
    min_costs[m][n] = costs[m][n]
  elif m == 0:
    min_costs[m][n] = min_path_cost_v2(costs, m, n - 1) + costs[m][n]
  elif n == 0:
    min_costs[m][n] = min_path_cost_v2(costs, m - 1, n) + costs[m][n]
  else:
    x = min_path_cost_v2(costs, m - 1, n)
    y = min_path_cost_v2(costs, m, n - 1)
    min_costs[m, n] = min(x, y) + costs[m][n]
  return min_costs[m][n]

def min_path_cost_v3(costs, m, n):
  min_costs = [
    [None] * 4,
    [None] * 4,
    [None] * 4
  ]

  min_costs[0][0] = costs[0][0]
  for i in range(1, m + 1):
    min_costs[i][0] = min_costs[i - 1][0] + min_costs[i][0]

  for j in range(1, n + 1):
    min_costs[0][j] = min_costs[0][j - 1] + min_costs[0][j]

  for i in range(1, m + 1):
    for j in range(1, n + 1):
        min_costs[i][j] = min(min_costs[i - 1][j], min_costs[i][j - 1]) + costs[m][n]

  return min_costs[m][n]
