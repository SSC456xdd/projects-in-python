import time
from battle import battleg
from world import player
from world import prison
#cheezborgor

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
  if "item" in prison[cl]:
   del prison[cl]["item"]
   player["inventory"]["potions"] += 3
   print(f"You found a big potion! it has up to {player['inventory']['potions']} uses.")
  elif "upgrade" in prison[cl]:
   player["attack"] += 10
   del prison[cl]["upgrade"]
   print(f"Congrats! now your blade does {player['attack']} damage.")

  print(f"Where would you like to go? ({prison[cl]["exits"]})")
  print(f"(Your location: {cl})")
  move = input("").strip().lower()
  if move in prison[cl]["exits"]:
    cl = prison[cl]["exits"][move]
  else:
   print("Please choose a direction.")
   continue

moves(cl)
