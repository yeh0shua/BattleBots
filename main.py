
# Create robot class
class Bot:
  def __init__(self, name, level, type):
    self.name = name
    self.level = level
    self.type = type

# Create player class
class Champion:
  def __init__(self, name):
    self.name = name
    self.bots = []
      
