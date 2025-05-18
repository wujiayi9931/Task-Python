class C:
     def __init__(self, data):
          self.data = data
     def __str__(self):
          return f"data = {self.data}"
     def __repr__(self):
          return f"C({self.data})"
     def __add__(self, other):
          self.data += other
