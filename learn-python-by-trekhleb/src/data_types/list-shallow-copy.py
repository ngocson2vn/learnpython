import random
import time, sys, colors

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits_copy = fruits.copy()

print(fruits)

fruits[0] = 'Orange'

print(fruits)
print(fruits_copy)


class Salmon(object):

  def __init__(self, name, sex):
    self.name = name
    self.sex = sex
    self.fin_color = 'Black'
    self.father = None
    self.mother = None

  def __str__(self):
    return """{{"name": "{}", "fin_color": "{}"}}""".format(self.name, self.fin_color)

  def breed_with(self, partner):
    child = None
    if self.sex != partner.sex:
      sexes = ['Male', 'Female']
      random.shuffle(sexes)
      child = Salmon(None, sexes[0])
      if self.sex == 'Male':
        child.father = self
        child.mother = partner
      else:
        child.father = partner
        child.mother = self

    return child


salmons = [Salmon('David', 'Male'), Salmon('Peter', 'Male'), Salmon('Mary', 'Female')]
salmons_copy = salmons.copy()
print(salmons[0])
print(salmons_copy[0])
print()

salmons[0].fin_color = 'Red'
print(salmons[0])
print(salmons_copy[0])
print("=" * 100)

i = 0
color = colors.red
while True:
  if i > 0 and i % 10 == 0:
    if color is colors.red:
      color = colors.green
    elif color is colors.green:
      color = colors.blue
    elif color is colors.blue:
      color = colors.yellow
    elif color is colors.yellow:
      color = colors.magenta
    else:
      color = colors.red

    print()
  sys.stdout.write(color("Little Moon, "))
  sys.stdout.flush()
  i += 1
  time.sleep(0.01)
