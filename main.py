
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
      target_bot.active = False

# Create Item class
class Item:
  def __init__(self, name, watts):
    self.name = name
    self.watts = watts
    
# Create Champion class
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
  
  # Allows player to use item object from their pack.
  def use_item(self, item):
    pass

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
      except ValueError:
        print(self.name + "! That's not an option here.")
      except TypeError:
        print(self.name + "! That's not an option here.")
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
  
  # AI chooses first bot in index of active bots
  def ai_bot_choice(self):
    active_bots = []
    for bot in self.bots:
      if bot.active == True:
        active_bots.append(bot)
      if bot.active == False:
        if bot in active_bots:
          active_bots.pop(bot)
    if active_bots:
      input(self.name + " sent " + active_bots[0].name + " to the battlefield!")
      return active_bots[0]
    if not active_bots:
      return None

# Returns list of player's active bots
def check_active_bots(player):
  active_bots = []
  for bot in player.bots:
    if bot.active == True:
      active_bots.append(bot)
  return active_bots

# Check for winner
def check_winner(player1, player2):
  if not check_active_bots(player1):
    return player2
  elif not check_active_bots(player2):
    return player1
  else:
    return None

# Battle function

def battle(player, computer):
  winner = None
  player_bot = None
  computer_bot = None

  print(computer.name + " has challenged you to a battle!")

  while winner == None:

    player_team = player.bots
    computer_team = computer.bots

    if player_bot == None:
      player_bot = player.choose_fighter()
    if computer_bot == None:
      computer_bot = computer.ai_bot_choice()

    # While either bot has an active status, players take turns attacking each other.
    while player_bot.active == True and computer_bot.active == True:
      player.choose_action(player_bot, computer_bot)
      if computer_bot.active == False:
        break
      computer_bot.attack(player_bot)
    
    if player_bot.active == False:
      player_bot = None
    if computer_bot.active == False:
      computer_bot = None
    

    winner = check_winner(player, computer)

  input(winner.name + " has won the battle!")

    
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

