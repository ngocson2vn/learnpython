import json
from contextlib import contextmanager

gx = 10

@contextmanager
def ctx():
  gx = 20
  try:
    yield
  finally:
    gx = 10

print(ctx.__name__)
print(type(ctx))
print(ctx.__class__)

# ctx() returns a `ContextDecorator/_GeneratorContextManager` instance (an object that implements `__enter__` and `__exit__`) compatible with the `with` statement.
c = ctx()
print(c.__class__)
print(type(c))
print(json.dumps(dir(c), indent=2))
