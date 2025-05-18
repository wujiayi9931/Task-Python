class Capstr(str):
    def__new__(cls, string)：
      string = string.upper()
      return super().__new__(cls, string)
CS = Capstr("FishC")
