
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
    if target_bot.charge <= 10:
      input(target_bot.name + " powered off!")
      target_bot.active == False
    

# Create player class
class Champion:
  def __init__(self, name):
    self.name = name
    self.bots = []
    self.pack = {}

  # Enables player to choose a live bot from their team
  def choose_fighter(self):
    fighter = None
    active_bots = []
    for bot in self.bots:
      if bot.active == True:
        active_bots.append(bot)
    if active_bots:
      input("Choose your fighter!")
      for idx, bot in enumerate(active_bots):
        print("Enter " + str(idx) + " for " + bot.name + " with a charge of " + str(bot.charge))
      while True:
        try:
          choice = int(input(""))
          fighter = active_bots[choice]
        except ValueError:
          print("You have to choose a valid number! Try again.")
          continue
        except IndexError:
          print("You have to choose a valid number! Try again.")
        else:
          break
      input(self.name + " sent " + fighter.name + " to the battlefield!")
      return fighter 
    else:
      print("You have no active bots!")
      return None
  
  def choose_action(self, bot, enemy):
    # Take user input
    input("Your turn...")
    print('''
Enter 0 to Attack
Enter 1 to Change BattleBot
Enter 2 to Use Item
Enter 3 to Forfeit Match
          ''')
    while True:
      valid = [0, 1, 2, 3]
      try:
        choice = int(input(""))
      except TypeError:
        print(self.name + "! That's not an option here.")
        continue
      else:
        if choice in valid:
          break
        else:
          print(self.name + "! That's not an option here.")
          continue
    
    # Perform action based on input
    if choice == 0:
      bot.attack(enemy)
    elif choice == 1:
      self.choose_fighter()
    elif choice == 2:
      pass
    elif choice == 3:
      return "QUIT"

   

# Battle system

def battle(player, computer):
  winner = None

  print(computer.name + " has challenged you to a battle!")
  player_bot = player.choose_fighter()
  computer_bot = computer.bots[0]
  
  # Battle continues until a winner is declared
  while winner == None:
    players_active_bots = []
    computers_active_bots = []

  # Checks both teams for active bots and adds them to lists
    for bot in player.bots:
      if bot.active == True:
        players_active_bots.append(bot)
    for bot in computer.bots:
      if bot.active == True:
        computers_active_bots.append(bot)
  
    action = player.choose_action(player_bot, computer_bot)
    if action == "QUIT":
      winner = computer

  # Checks both teams for inactive bots and removes them from lists
    for bot in player.bots:
      if bot.active == False:
        players_active_bots.pop(bot)
    for bot in computer.bots:
      if bot.active == False:
        computers_active_bots.pop(bot)

    if not players_active_bots:
      winner = computer
  
    if not computers_active_bots:
      winner = player

  print(winner.name + " has won the match!")    

    
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

battle(player1, player2)

