costs = [
  [0, 10, 75, 94],
  [-1, 0, 35, 50],
  [-1, -1, 0, 80],
  [-1, -1, -1, 0]
]

def calculate_min_cost(costs):
  min_costs = [None] * len(costs)
  min_costs[0] = costs[0][0]
  min_costs[1] = costs[0][1]
  for i in range(2, len(costs)):
    c = costs[0][i]
    for j in range(1, i):
      m = min_costs[j] + costs[j][i]
      if m < c:
        c = m
    min_costs[i] = c
  return min_costs[len(costs) - 1]

min_cost = calculate_min_cost(costs)
print(min_cost)