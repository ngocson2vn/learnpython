from functools import wraps

def display(*args, **kwargs):
    for a in args:
        print(a)
    for k, v in kwargs:
        print(f"{k}={v}")

def wrapper_raw_ops(op_name):
    print(f"wrapper_raw_ops is called with argument op_name={op_name}")
    def wrapper(func):
        print(f"wrapper is called with argument func={func}")

        @wraps(func)
        def wrapper_api(*args, **kwargs):
            print(f"Before calling {func.__name__}")
            op = display
            ret = func(*args, op=op, **kwargs)
            print(f"After calling {func.__name__}")
            return ret

        print(f"wrapper returns wrapper_api")
        return wrapper_api

    print(f"wrapper_raw_ops returns wrapper")
    return wrapper

@wrapper_raw_ops("eng_flash_attn_fwd_v2")
def eng_flash_attn_fwd_v2(q, k, v, tao, **kwargs):
    op = kwargs.pop("op")
    return op(q, k, v, tao, **kwargs)

