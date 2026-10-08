import random
import time
import os
player = {
 "name": "Mochi", "hp": 100, "attack": 10, "max_hp": 100,
 'inventory': {"potions": 0, "blade sharpeners": 0,}
 }
prison = {
 "Cell": {
  "description": "An old, worn out bed and a hole big enough you could go through it.",
  "exits": {"east": "Cell block"} 
 },
 "Cell block": {
  "description": "You see a group of bugs eating something off the wall.",
  "enemy":{"name": "Fungi eater", 'hp': 25, 'attack': 2, 'max_hp': 25},
  "exits":{"west":"Cell", "north": "Storage", "east": "Root tunnel"}
 },
 "Storage": {
  "description": "You see something behind a crate but you can't quite tell what it is.",
  "exits":{"south": "Cell block"},
  "item": "Healing potion"
 },
 "Root tunnel": {
  "description": "While crossing this empty shell of a tree, you see a group of something flying.",
  "enemy": {"name": "Flying mosquito", 'hp': 50, 'attack': 5, 'max_hp': 50},
  "exits": {"west": "Cell block", "east": "Guarder's hall", "north": "Armory"}
 },
 "Armory": {
  "description": "Between lots of rusty weapons, you find one that might upgrade something for you.",
  "exits":{"south": "Root tunnel"},
  "item": 'Blade sharpener'
 },
 "Guarder's hall": {
  "description": "You see a big door.",
  "enemy": {"name": "Guard husk", "hp": 75, "attack": 8, 'max_hp': 75},
  "exits": {"west": "Root tunnel", "east": "Jailer's hall"}
 },
 "Jailer's hall": {
  "description": "The place where the guardian of the entire prison rests.",
  "exits":{"west": "Guarder's hall", "east": "Gate"},
  "enemy": {"name": "Agoner", "hp": 150, "attack": 15, 'max_hp': 200}
 },
 "Gate": {
  "description": "At last, you finally are able to leave and go to the city",
  "exits": {"north": "Citadel"}
 },
 "Citadel": {
  "description": "A beautiful city with lots of crime, you see where you were arrested wrongfully.",
  "exits": {}
 }
}
#cheezborgor
def battleg(player,enemy,):
 print("")
 print(f"You are fighting {enemy["name"]}!")
 while enemy['hp'] > 0 and player['hp'] > 0:
     print(f"Your health: {player['hp']}")
     print(f"{enemy["name"]}'s health: {enemy['hp']}")
     c1 = input("Attack, defend or heal? ").strip().lower()
     moves = ["attack",'defend','heal','attack','attack','defend']
     pc1 = random.choice(moves)
     #User section choice
     if c1 == "attack":
      if pc1 == "defend":
        print("")
      else:       
       enemy['hp'] -= player['attack']
     elif c1 == "defend":
      if pc1 == "attack":
       print(f"You've blocked {enemy["name"]}'s attack!")
      else:
       print("You did nothing.")
     elif c1 == "heal":
      player['hp'] = min(player["hp"] + 7, player['max_hp'])
      print("You healed!")
     else:
      print("Please choose an action.")
      continue
     #Enemys section choice
     if enemy['hp'] > 0:
      if pc1 == "attack": 
       if c1 == "defend" :
         print(f'{enemy['name']} decided to {pc1}!')
       else:
         player["hp"] -= enemy['attack'] 
         print(f'{enemy['name']} decided to {pc1}!')
      elif pc1 == "defend":
       print(f'{enemy['name']} decided to {pc1}!')
       if c1 == "attack":
        print("Your attack has been blocked.")
       else:
        print("The enemy did nothing.") 
      elif pc1 == "heal":
       print(f'{enemy['name']} decided to {pc1}!')
       enemy['hp'] = min(enemy['hp'] + 10, enemy ['max_hp'])
 #Win system 
 if enemy['hp']<= 0:
  print("You win!")
  time.sleep(1)
  os.system("clear")
 else:
  print("You lose!")
 time.sleep(1)
cl = "Cell" #cl = Current location
def moves(cl):
 while True: 
  print()
  print(prison[cl]["description"])
  if "enemy" in prison[cl]:
    enemy = prison[cl]["enemy"]
    if prison[cl]['enemy']['hp'] <= 0:
     print(f"You see the {enemy['name']} you just killed.")
    else:
     battleg(player,enemy,)
     if player['hp'] <=0:
        print(f"You died in {cl} to {enemy["name"]}...")
        break
     else:
      print()
  else:
   print()
  #ending
  if cl == "Citadel":
   print("Congratulations! you have finished the game.")
   time.sleep(1)
   break
  else:
   print()
  print(f"Where would you like to go? ({prison[cl]["exits"]})")
  print(f"(Your location: {cl})")
  move = input("").strip().lower()
  if move in prison[cl]["exits"] or prison[cl]['exits']['south', 'east', 'west', 'north']:
    cl = prison[cl]["exits"][move]
  else:
   print("Please choose a direction.")
   continue

moves(cl)
