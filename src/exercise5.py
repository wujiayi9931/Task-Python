class C:
    def __init_(self, data):
        self.data = data
    def __iter__(self):
        print("Iter", end=' ->')
        self.i = 0
        return self
   def __next__(self):
       print("Next", end='->')
       if self.i == len(self.data):
            raise StopIteration
       item = self.data[self.il
       self.i += 1
       return item
