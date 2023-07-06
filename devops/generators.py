def count():
  n = 0
  while True:
    n += 1
    yield n

def Fibonacci():
  prev = 0
  next = 1
  yield prev
  yield next
  while True:
    prev, next = next, prev + next
    yield next

# Generator Comprehension
gen = (x for x in range(1000))