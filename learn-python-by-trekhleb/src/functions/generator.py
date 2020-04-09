def gensquares(N):
  for i in range(N):
    print("Before yield")
    yield i ** 2
    print("After yield")

for i in gensquares(10):
  print("Result = {}\n".format(i))

x = gensquares(20)
