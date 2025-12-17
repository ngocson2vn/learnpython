class Context:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print(f"Enter {self.name}")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exit {self.name}")

with Context("A"), Context("B"), Context("C"):
    print("Inside")
