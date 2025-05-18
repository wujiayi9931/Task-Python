class E:
    def__init__(self, name, func)：
          self.name = name
          self.func = func
    def__del__(self):
          self.func(self)
def outter():
   x =0
   def inner(y=None)：
        nonlocal x
        if y:
          x =y
        else:
          return x
   return inner

