# Understanding Closures
Python allows a nested function to access the outer scope of the enclosing function. This is a critical concept in decorators, known as a closure.

A closure in Python is a function that remembers the environment in which it was created, even after that environment is no longer active. This means a nested function can "close over" variables from its enclosing scope and continue to use them.

Closures are essential for understanding decorators because decorators rely on the ability of a nested wrapper function to access and modify the state of the enclosing decorator function.

Example of a closure:
```Python
def outer_function(message):
    def inner_function():
        print(f"Message from closure: {message}")
    return inner_function

closure_function = outer_function("Hello, closures!")
closure_function()
# Output: Message from closure: Hello, closures!
```
In this example:

`inner_function` is a closure because it accesses `message`, a variable from its enclosing scope (`outer_function`).
Even though outer_function has finished executing, `inner_function` retains access to `message`.
When you create a decorator, the wrapper function (inside the decorator) is a closure. It retains access to the function being decorated and any additional state or arguments defined in the decorator function. For example:
```Python
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@simple_decorator
def greet():
    print("Hello!")

greet()
# Output:
# Before the function call
# Hello!
# After the function call
```
Here, wrapper is a closure that remembers the function greet and adds behavior before and after its execution.


# functools.wraps
1. Assume we have this: Simple Decorator which takes a function’s output and puts it into a string, followed by three !!!!.
```Python
def mydeco(func):
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)}!!!'
    return wrapper
```

2. Let’s now decorate two different functions with “mydeco”:
```Python
@mydeco
def add(a, b):
    '''Add two objects together, the long way'''
    return a + b

@mydeco
def mysum(*args):
    '''Sum any numbers together, the long way'''
    total = 0
    for one_item in args:
        total += one_item
    return total
```

3. when run add(10,20), mysum(1,2,3,4), it worked!
```Python
>>> add(10,20)
'30!!!'

>>> mysum(1,2,3,4)
'10!!!!'
```

4. However, the name attribute, which gives us the name of a function when we define it,
```Python
>>>add.__name__
'wrapper`

>>>mysum.__name__
'wrapper'
```

5. Worse
```Python
>>> help(add)
Help on function wrapper in module __main__:
wrapper(*args, **kwargs)

>>> help(mysum)
Help on function wrapper in module __main__:
wrapper(*args, **kwargs)
```

6. We can fix partially by:
```Python
def mydeco(func):
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)}!!!'
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper
```

7. Now we run step 5 (2nd time) again:
```Python
>>> help(add)
Help on function add in module __main__:

add(*args, **kwargs)
     Add two objects together, the long way

>>> help(mysum)
Help on function mysum in module __main__:

mysum(*args, **kwargs)
    Sum any numbers together, the long way
```

8. But we can use functools.wraps (decotator tool)
```Python
from functools import wraps

def mydeco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)}!!!'
    return wrapper
```

9. Now run step 5 (3rd time) again
```Python
>>> help(add)
Help on function add in module main:
add(a, b)
     Add two objects together, the long way

>>> help(mysum)
Help on function mysum in module main:
mysum(*args)
     Sum any numbers together, the long way
```

[Reference](https://lerner.co.il/2019/05/05/making-your-python-decorators-even-better-with-functool-wraps/)