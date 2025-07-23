class Parent:
    def __init__(self, name="unknown"):
        print(f"{__class__} self: {id(self)}")
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        print(f"{__class__} self: {id(self)}")
        # super().__init__(name)  # self is automatically passed
        self.age = age

child = Child("Alice", 10)
print(f"child.name: {child.name}")
print(f"child.age: {child.age}")