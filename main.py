import random

# Create robot class
class Bot:
  def __init__(self, name, level, attack_module, defend_module, base_attack, base_defense):
    self.name = name
    self.level = level
    self.max_charge = level * 10
    self.current_charge = level * 10
    self.active = True

    self.attack_module = attack_module
    self.defend_module = defend_module

    # Battle stats
    self.attack_val = base_attack * level
    self.defense_val = base_defense * level

  def attack(self, target_bot):
    critical = False
    if random.randint(0,5) == 5:
      critical = True

    damage = (self.attack_val - target_bot.defense_val) + 10

    if self.attack_module.has_advantage(target_bot.defend_module):
      damage *= 1.5
    if self.attack_module.is_disadvantaged(target_bot.defend_module):
      damage *= .5

    if damage <= 5:
      damage = 5
    if critical:
      damage *= 2
    target_bot.current_charge -= damage
    input(self.name + " attacked " + target_bot.name)
    if critical:
      input("A critical hit!")
    input(target_bot.name + " sustained " + str(damage) + " damage!")
    if target_bot.current_charge <= 0:
      input(target_bot.name + " powered off!")
      target_bot.active = False

  def defend(self):
    self.defense_val += 5
    input(self.name + " defended itself!")
  
  def is_bot(self):
    return True
  
  def watt_bar(self):
    health = ""
    watt_ratio = int((self.current_charge / self.max_charge) * 10)
    for i in range(0, watt_ratio):
      health += "#"
    num_dashes = 10 - len(health)
    for i in range(0, num_dashes):
      health += "-"
    health_bar = "[" + health + "]"
    return health_bar


class Module:
  def __init__(self, type):
    self.type = type
  
  def has_advantage(self, other_module):
    if self.type == "water" and other_module.type == "fire":
      return True
    if self.type == "fire" and other_module.type == "grass":
      return True
    if self.type == "grass" and other_module.type == "water":
      return True
    else:
      return False
  
  def is_disadvantaged(self, other_module):
    if self.type == "fire" and other_module.type == "water":
      return True
    if self.type == "grass" and other_module.type == "fire":
      return True
    if self.type == "water" and other_module.type == "grass":
      return True
    else:
      return False  

# Create Item class
class Item:
  def __init__(self, name, watts):
    self.name = name
    self.watts = watts
    
# Create Champion class
class Champion:
  def __init__(self, name, is_ai=False):
    self.name = name
    self.bots = []
    self.pack = []
    self.is_ai = is_ai

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
        print("Enter " + str(idx) + " for " + bot.name + " " + bot.watt_bar())
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
  def use_item(self, bot):
    if self.pack:
      for idx, item in enumerate(self.pack):
        print(str(idx) + " for " + item.name)
      while True:
        try:
          choice = int(input(""))
          item = self.pack[choice]
        except ValueError:
          print("Invalid option! Try again.")
          continue
        except IndexError:
          print("Invalid option! Try again")
        else:
          break
      bot.current_charge += item.watts
      self.pack.remove(item)
      input(self.name + " used " + item.name + " on " + bot.name)
      input(bot.name + "'s watt's increased by " + str(item.watts))
    else:
      input("No items in your pack.")

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
      return self.choose_fighter()
    elif choice == 2:
      self.use_item(bot)
    elif choice == 3:
      return "QUIT"
  
  # AI chooses a bot
  def ai_bot_choice(self, target_bot):
    active_bots = []
    smart_picks = []
    for bot in self.bots:
      if bot.active == True:
        active_bots.append(bot)
      if bot.active == False:
        if bot in active_bots:
          active_bots.pop(bot)
    if active_bots:
      for bot in active_bots:
        if bot.defend_module.has_advantage(target_bot.attack_module) or bot.attack_module.has_advantage(target_bot.defend_module):
          smart_picks.append(bot)
          choice = smart_picks[0]
          input(self.name + " sent " + choice.name + " to the battlefield!")
        else:
          choice = active_bots[0]
          input(self.name + " sent " + choice.name + " to the battlefield!")
        return choice
    if not active_bots:
      return None
  
  def ai_choose_battle_action(self, bot, target_bot):
    if bot.current_charge <= bot.max_charge * .5:
      if self.pack:
        item_to_use = self.pack[0]
        bot.current_charge += item_to_use.watts
        self.pack.remove(item_to_use)
        input(self.name + " used a " + item_to_use.name + " on " + bot.name)
        input(bot.name + " has " + str(bot.current_charge) + " watts of charge!")
      else:
        bot.attack(target_bot)
    else:
      if target_bot.attack_module.has_advantage(bot.defend_module):
        thought = random.randint(1,3)
        good_idea = 3
        if thought == good_idea:
          self.ai_bot_choice(target_bot)
        else:
          bot.attack(target_bot)
      else:
        bot.attack(target_bot)

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
      computer_bot = computer.ai_bot_choice(player_bot)

    # While either bot has an active status, players take turns attacking each other.
    while player_bot.active == True and computer_bot.active == True:
      action = player.choose_action(player_bot, computer_bot)
      try:
        if action.is_bot:
          player_bot = action
      except AttributeError:
        pass
      if computer_bot.active == False:
        break
      action = computer.ai_choose_battle_action(computer_bot, player_bot)
      try:
        if action.is_bot:
          computer_bot = action
      except AttributeError:
        pass

# Battle status display
      print('''
+++++++++++++++++++++++++++++++++++++++++++++++
'''
+

player.name + "                     " + computer.name + "\nBOT: " + player_bot.name + " " + player_bot.watt_bar() + "      " + "BOT: " + computer_bot.name + " " + computer_bot.watt_bar() + "\n" +

player_bot.attack_module.type + "/" + player_bot.defend_module.type + "                 " + computer_bot.attack_module.type + "/" + computer_bot.defend_module.type +

'''
+++++++++++++++++++++++++++++++++++++++++++++++
''')

# End battle status display
    
    if player_bot.active == False:
      player_bot = None
    if computer_bot.active == False:
      computer_bot = None
    

    winner = check_winner(player, computer)

  input(winner.name + " has won the battle!")

def game():
  input("Welcome to the world of BattleBots!")
    
# Testing area

player1 = Champion("Joshua")
player2 = Champion("Neon")

water_mod = Module("water")
fire_mod = Module("fire")
grass_mod = Module("grass")


bot1 = Bot("Linus", 10, fire_mod, fire_mod, 10, 10)
bot2 = Bot("Ghidra", 10, grass_mod, grass_mod, 10, 10)
bot3 = Bot("Victory", 10, water_mod, water_mod, 10, 10)
bot4 = Bot("Picard", 10, water_mod, water_mod, 10, 10)
bot5 = Bot("Haephestus", 10, grass_mod, grass_mod, 10, 10)
bot6 = Bot("Xenu", 10, fire_mod, fire_mod, 10, 10)

repair_kit = Item("Repair Kit", 20)
player1.pack.append(repair_kit)
player2.pack.append(repair_kit)

player1.bots.extend([bot1, bot2, bot3])
player2.bots.extend([bot4, bot5, bot6])

battle(player1, player2)

