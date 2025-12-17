import json

code = '''
def greet():
    print("Hello, World!")
greet()
'''
ctx = {}
exec(code, ctx)

# ctx.pop("__builtins__")
print(json.dumps(ctx, indent=2, default=str))
