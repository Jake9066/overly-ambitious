from .skills import *

class Character:
  def __init__(self):
    self.Strength = 0
    self.Dexterity = 0
    self.Constitution = 0
    self.Intelligence = 0
    self.Wisdom = 0
    self.Charisma = 0
    
    self.Skills = Skills()

class PlayerCharacter(Character):
  pass

class NonPlayerCharacter(Character):
  pass
