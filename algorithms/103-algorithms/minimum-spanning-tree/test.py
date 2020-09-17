import util
import matplotlib.pyplot as plt

X, Y = util.circle(10, 10, 9)
plt.scatter(X, Y, s=3)
for i in range(10):
  a, b = util.generate_random_point_on_circle(10, 10, 9)
  plt.plot([a], [b], marker='o', markersize=5, color="red")
plt.show()