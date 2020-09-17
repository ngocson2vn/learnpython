import numpy as np
import matplotlib.pyplot as plt
import util

G = np.array(
      [[0, 9, 75, 2, 0],
      [9, 0, 95, 19, 42],
      [75, 95, 0, 51, 66],
      [2, 19, 51, 0, 31],
      [0, 42, 66, 31, 0]]
    )

X = np.zeros(G.shape[0])
Y = np.zeros(G.shape[0])
X[0] = 10
Y[0] = 10

fig, axes = plt.subplots(figsize=(16, 8))
axes.set_aspect(1)
axes.margins(x=2, y=1)

i = 0
j = 1
circle0 = plt.Circle((X[i], Y[i]), G[i, j], color='b', fill=False)
axes.add_artist(circle0)
X[j], Y[j] = util.generate_random_point_on_circle(X[i], Y[i], G[i, j])
circlej = plt.Circle((X[j], Y[j]), G[i, j], color='b', fill=False)



# for i in range(G.shape[0]):
#   for j in range(i + 1, G.shape[0]):
#     if G[i, j] > 0:
#       print("(i = {}, j = {})".format(i, j))
#       X[j], Y[j] = util.generate_random_point_on_circle(X[i], Y[i], G[i, j])

plt.scatter(X, Y, s=20, c='r')
plt.plot(X, Y)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
