from .skills import *
from .attributes import *

class Character:
  def __init__(self):
    self.Strength = Primary("Strength")
    self.Dexterity = Primary("Dexterity")
    self.Constitution = Primary("Constitution")
    self.Intelligence = Primary("Intelligence")
    self.Wisdom = Primary("Wisdom")
    self.Charisma = Primary("Charisma")
    
    self.Skills = Skills()

class PlayerCharacter(Character):
  pass

class NonPlayerCharacter(Character):
  pass
