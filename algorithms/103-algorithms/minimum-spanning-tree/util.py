import math
import random
import numpy as np

def circle(x_c, y_c, r):
  """
  The equation of a circle
    (x - x_c)**2 + (y - y_c)**2 = r**2
    y = y_c - math.sqrt(r**2 - (x - x_c)**2)
    y = y_c + math.sqrt(r**2 - (x - x_c)**2)
  """
  X = []
  Y = []
  for x in np.arange(x_c - r, x_c + r + 0.1, 0.1):
    x = round(x, 1)
    # print(x)
    d = math.sqrt(r**2 - (x - x_c)**2)
    y1 = y_c - d
    y2 = y_c + d
    X.extend([x, x])
    Y.extend([y1, y2])
  return X, Y

def generate_random_point_on_circle(x_c, y_c, r):
  x = random.uniform(x_c - r, x_c + r)
  y = y_c + math.sqrt(r**2 - (x - x_c)**2)
  return x, y