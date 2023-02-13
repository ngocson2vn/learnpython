def gen_integer():
  for i in range(10):
    recv = yield i
    print(f"Received: {recv}")

def gen():
  ret = yield from gen_integer()
  print(f"Result: {ret}")
