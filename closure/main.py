def make_x():
  for i in range(10):
    yield i

def make_box():
  def inner():
    print(f"x = {next(x)}")
    print(f"x = {next(x)}")
    print(f"x = {next(x)}")

  x = make_x()
  return inner

box = make_box()
box()
print()

# When `make_box2` returns `inner`, 
# Python creates a closure that “remembers” the environment where `inner` was defined, 
# including the binding of `x` to `10`. 
# This remembered environment is stored in `inner.__closure__`.
def make_box2():
  def inner():
    print(f"x = {x}")
    print(f"x = {x + 1}")
    print(f"x = {x + 2}")

  x = 10
  return inner

box2 = make_box2()
for var in box2.__code__.co_freevars:
  print(var)
