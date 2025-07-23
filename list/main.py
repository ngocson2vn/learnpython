class Student:
  def __init__(self, id: int, name: str):
    self.id = id
    self.name = name
  
  def __repr__(self):
    return f"{{id: {self.id}, name: {self.name}}}"

students = []
for i in range(10):
  students.append(Student(i, f"Student{i}"))

for s in students:
  s.name += "_modified"
  print()

print("\n".join([repr(s) for s in students]))