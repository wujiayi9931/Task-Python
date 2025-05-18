class Power:
     def __init__(self, exp)：
          self.exp = exp
     def __call__(self, base):
          return base ** self.exp
