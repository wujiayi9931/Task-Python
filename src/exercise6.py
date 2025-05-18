class S(str):
   def __lt__(self, other):
         return len(self) < len(other)
   def __gt__(self, other):
         return len(self) > len(other)
   def __eq__(self, other):
         return len(self) == len(other)
   __le__=None
   __ge__=None
   __ne__=None
