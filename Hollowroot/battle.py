import os
import random
import time
def battleg(user,enemy,):
 print("")
 if "intro" in enemy:
  print(enemy["intro"])
  
  print("")
  time.sleep(2)
 else:
  print("")
  #Check if enemy is alive or not
 print(f"You are fighting {enemy["name"]}!")
 while enemy['hp'] > 0 and user.is_alive():
     print(f"Your health: {user.hp}")
     print(f"{enemy["name"]}'s health: {enemy['hp']}")
     pmoves = ["1. attack",'2. defend','3. heal',]
     if user.inventory["potions"] > 0:
           pmoves.append("4. use potion")
     print(", ".join(pmoves))
     c1 = input("").strip().lower()

     moves = ["attack",'defend','heal','attack','attack','defend']
     pc1 = random.choice(moves)
     #User section choice
     if c1 == "1":
      if pc1 == "defend":
        print("")
      else:       
       enemy['hp'] -= user.attack
     elif c1 == "2":
      if pc1 == "attack":
       print(f"You've blocked {enemy["name"]}'s attack!")
      else:
       print("You did nothing.")
     elif c1 == "3":
      user.healing(7)
      print("You healed 7 HP!")
     elif c1 == "4" and user.inventory["potions"] > 0:
      user.healing(25)
      print("Healed 25HP!")
      user.inventory["potions"] -= 1
      print(f"{user.inventory["potions"]} potions left.")
     else:
      print("Please choose an action.")
      continue
     #Enemys section choice
     if enemy['hp'] > 0:
      if pc1 == "attack": 
       if c1 == "2" :
         print(f'{enemy['name']} decided to {pc1}!')
       else:
         user.take_damage(enemy['attack'])
         print(f'{enemy['name']} decided to {pc1}!')
      elif pc1 == "defend":
       print(f'{enemy['name']} decided to {pc1}!')
       if c1 == "1":
        print("Your attack has been blocked.")
       else:
        print("The enemy did nothing.") 
      elif pc1 == "heal":
       print(f'{enemy['name']} decided to {pc1}!')
       enemy['hp'] = min(enemy['hp'] + 10, enemy ['max_hp'])
 #Win system 
 if enemy['hp']<= 0:
    if "outro" in enemy:
     print (enemy['outro'])
     print ("")
     print("You win!")
     print("Press Enter to continue")
     if input(""):
      os.system("clear")   
    else:
     print("You win!")
    time.sleep(1)
    os.system("clear")
 else:
  print("You lose!")
 time.sleep(1)

