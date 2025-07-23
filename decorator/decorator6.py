import pdb
import functools

def forward():
    print("Forward function called")

def optimize(fn):
    @functools.wraps(fn)
    def _fn(*args, **kwargs):
        print("Start function:", fn.__name__)
        fn()
        print("Finish function:", fn.__name__)

    pdb.set_trace()
    return _fn

optimized_func = optimize(forward)
optimized_func()