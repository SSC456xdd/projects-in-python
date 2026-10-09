import time
import random
coins = 20
potions = 0
def potion_market(coins,potions):
 print("You have entered the potion stand!")
 while True:
    print("Would you like to check status, buy, or quit?") 
    c1 = input("").strip().lower()
    if c1 == "buy":
         print("Would you like to buy? (y/n) ")
         buying = input("").strip().lower()
         if buying in ["yes", "y"]:
          if coins >= 5:
           coins -= 5
           potions += 1
           print(f'You now have ${coins} and {potions} potion(s).')
           print("")
          else:
           print("Not enough coins.")
         elif buying in ["no", "n"]:
          print("")
         else:
          print("Please choose an option.")
    elif c1 == "status":
      print(f"You currently have ${coins}, and {potions} potion(s).")
      print("")
    elif c1 == "quit":
      print("Until next time!")
      return coins, potions 
    else:
      print("Please choose an option.")
print(f"You had {coins} coin(s) and {potions} potion(s)")



