from contextlib import contextmanager
from threading import local

class Kernel:
  def __init__(self, name):
    self._name = name

threadlocal = local()

class _V:
  def __init__(self, name):
    self._vname = name
    self._key = f"__key_{self._vname}"
    setattr(threadlocal, self._key, None)

  def set_kernel_handler(self, kernel: Kernel):
    prior = getattr(threadlocal, self._key)
    setattr(threadlocal, self._key, kernel)

    @contextmanager
    def ctx():
      try:
        yield
      finally:
        setattr(threadlocal, self._key, prior)
    
    return ctx()

  def get_kernel_handler(self):
    return getattr(threadlocal, self._key)


V = _V("kernel")

if __name__ == "__main__":
  print(V.get_kernel_handler())
  kernel = Kernel("kernel1")
  with V.set_kernel_handler(kernel) as ctx:
    print(f"ctx: {ctx}")
    print(V.get_kernel_handler())
  print(V.get_kernel_handler())