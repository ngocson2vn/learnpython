def doSomething():
  x = 10
  print("Start doSomething")
  x = x ** 2
  print(f"x = {x}")
  print("End doSomething")


fn = lambda: doSomething()
print(type(fn))
fn()