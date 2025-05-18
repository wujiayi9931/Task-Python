class D:
    def __init__(self):
      self._x = 250
    def __getattr__(self, name):
      if name == 'x':
            return self._x
      else:
            super().__getattr__(name)
    def __setattr__(self, name, value):
      if name == 'x':
           super().__setattr__('_x',value)
      else:
           super().__setattr__(name, value)
    def __delattr__(self, name)：
      if name == 'x':
           super().__delattr__('_x')
      else:
           super().__delattr__(name)
