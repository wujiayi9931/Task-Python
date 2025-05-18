class C:
  count = 0
  @classmethod
  def add(cls):
    cls.count += 1
  def __init__(self):
    self.add()
  @classmethod
  def get_count(cls):
    print(f"该类一共实例化了 {cls.count}个对象。”)
