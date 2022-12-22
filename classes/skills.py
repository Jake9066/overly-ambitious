class Skill:
  def __init__(self):
    self.Name = None
    self.Attribute = None

class Active(Skill):
  self.Cost = None

class Battle(Active):
  self.Cooldown = None

class Field(Active):
  pass

class Passive(Skill):
  pass
