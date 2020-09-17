def memo_fibonacci(n, cache):
  if cache[n] is None:
    if n <= 2:
      cache[n] = 1
    else:
      cache[n] = memo_fibonacci(n - 2, cache) + memo_fibonacci(n - 1, cache)
  return cache[n]

def tabu_fibonacci(n):
  results = [1, 1]
  for i in range(2, n):
    results.append(results[i - 2] + results[i - 1])
  return results

def dyn_fibonacci(n):
  if n <= 0:
    return None
  
  if n <= 2:
    return 1
  
  p = 1
  q = 1
  f = 0
  for i in range(3, n + 1):
    f = p + q
    p = q
    q = f
  return f



n = 10
cache = [None] * (n + 1)
memo_fibonacci(n, cache)
print(cache[1:])


results = tabu_fibonacci(n)
print(results)

print(dyn_fibonacci(n))
