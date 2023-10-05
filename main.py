
# Create robot class
class Bot:
  def __init__(self, name, level):
    self.name = name
    self.level = level
    self.charge = level * 10

  def attack(self, target_bot):
    target_bot.charge -= 10
    input(self.name + " attacked " + target_bot.name)
    input(target_bot.name + " sustained 10 damage!")
    

# Create player class
class Champion:
  def __init__(self, name):
    self.name = name
    self.bots = []


    
# Testing area
bot1 = Bot("Linus", 7)
bot2 = Bot("Ghidra", 5)

while bot1.charge > 0 and bot2.charge > 0:
  choice = input("Press A to attack!")
  if choice == 'A':
    bot1.attack(bot2)
    input("Your opponent is preparing an attack.")
    bot2.attack(bot1)
  else:
    print(bot1.name + " did not understand your command.")

if bot1.charge > 0:
  winner = bot1
elif bot2.charge > 0:
  winner = bot2

print(winner.name + " won!")
