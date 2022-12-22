class Attribute:
  def __init__(self):
    self.Name = None
    self.Value = None
    self.Bonus = None

class Secondary(Attribute):
  def __init__(self, **kwargs):
    super().__init__()
