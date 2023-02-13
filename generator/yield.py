def gen_AB():
  print("start")
  yield "A"
  print("continue")
  yield "B"
  print("end")

def gen_integer():
  print("Start")
  i = 1
  while True:
    print(f"Round {i}")
    yield i
    print("Increase i")
    i += 1
    if i == 10:
      break
  print("End")

def gen_x():
  print("Start")
  i = 1
  while True:
    x = yield i
    print(f"x = {x}")
    i += 1

def gensquares(N):
  for i in range(N):
    yield i**2

def gen():
  for i in range(10):
    X = yield i
    print(f"X = {X}")
