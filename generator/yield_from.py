"""
The yield from expression in Python (introduced in Python 3.3 via PEP 380) is used within a generator function to delegate iteration to another iterable or generator (often called a subgenerator). It effectively yields each value from the sub-iterable one by one, as if they were yielded directly from the current generator. This allows for cleaner composition of generators without manual looping (e.g., no need for for item in subgen: yield item).Additionally, yield from handles two-way communication: it propagates exceptions raised in the subgenerator back to the caller and captures any return value from the subgenerator (accessible via a variable, like result = yield from subgen()).

The key benefit of yield from x (assuming x is an iterable or generator) is that it yields each individual item from x sequentially into the current generator's output stream, allowing the generator to continue after delegation. In contrast, return x immediately terminates the generator and returns the entire x object as the generator's return value (accessible via the StopIteration exception's value attribute when exhausted), without yielding any of its contents.This makes yield from ideal for flattening or chaining generators, promoting modular and memory-efficient code, while return x is better for ending the generator early and passing back a single value or object.
"""

def gen_integer():
  for i in range(10):
    recv = yield i
  return "DONE"

def main_gen():
  ret = yield from gen_integer()
  print(f"Result: {ret}")

gen = main_gen()
for i in gen:
  print(i)
