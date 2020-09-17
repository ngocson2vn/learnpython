def nest(n):
  for i in range(n):
    for j in range(n):
      i + j

from timeit import timeit
def profile(n):
  ls = []
  for n in range(n):
    t = timeit("nest({})".format(n), setup="from __main__ import nest", number=1)
    ls.append(t)
  return ls

import matplotlib.pyplot as plt
n = 1000
plt.plot(profile(n))
plt.plot([x*x/10000000 for x in range(n)])
plt.show()