
# Create robot class
class Bot:
  def __init__(self, name, level):
    self.name = name
    self.level = level
    self.charge = level * 10
    self.active = True 

  def attack(self, target_bot):
    target_bot.charge -= 10
    input(self.name + " attacked " + target_bot.name)
    input(target_bot.name + " sustained 10 damage!")
    

# Create player class
class Champion:
  def __init__(self, name):
    self.name = name
    self.bots = []
    self.pack = {}
  
  def battle(self, opponent):
    input(opponent.name + " has challenged you to a battle!")
    input("Choose your first fighter:")
    fighter = None

    # Player selects fighter
    while fighter is None:
      for bot in self.bots:
        print(bot.name)
      choice = input("Which bot will you send to battle first?\n")
      for bot in self.bots:
        if choice == bot.name:
          fighter = bot
          if fighter.active == True:
            input(fighter.name + " has entered the ring!")
            input(fighter.name + " has a charge of " + fighter.charge)
          else:
            input(fighter.name + " has no power! Make another selection")
        else:
          input("Not a valid selection! Please try again.")
    
    # Opponent selects enemy bot
    

    
# Testing area

player1 = Champion("Joshua")
player2 = Champion("Neon")


bot1 = Bot("Linus", 7)
bot2 = Bot("Ghidra", 5)
bot3 = Bot("Victory", 6)
bot4 = Bot("Picard", 5)
bot5 = Bot("Haephestus", 7)
bot6 = Bot("Xenu", 6)

player1.bots.extend([bot1, bot2, bot3])
player2.bots.extend([bot4, bot5, bot6])

player1.battle(player2)

'''

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

'''
