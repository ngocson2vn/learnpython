def f(debug=False, **kwargs):
  if debug:
    for k, v in kwargs.items():
      print(f"{k}: {v}")
  else:
    print(f"debug = {debug}")
  
f(debug=True, x=10, y=20, z=30)