import time
from battle import battleg
from world import user
from world import prison

global game_finished 
game_finished = False

def show_exits(cl):
    exit_options = []

    for direction, destination in prison[cl]["exits"].items():
        exit_options.append(f"{direction}: {destination}")

    print(f"Where would you like to go? ({', '.join(exit_options)})")
    print(f"(Your location: {cl})")
  
#cheezborgor
def story():
 print("You were wrongfully imprisoned after being near a robbery of the richest bug in Hollowroot.")
 time.sleep(3)
 print("They think that you were the one who stole his precious watch and you weren't able to convince them.")
 time.sleep(3)
 print("Your current mission is to leave the prison you are currently at.")
 time.sleep(5)
 return movement(cl)


cl = "Cell" #cl = Current location
def movement(cl):
 while True: 
  print()
  print(prison[cl]["description"])
  if "enemy" in prison[cl]:
    enemy = prison[cl]["enemy"]
    if enemy.is_alive() <= 0:
     print(f"You see the {enemy['name']} you just killed.")
    else:
     battleg(user,enemy,)
     if user.hp <=0:
        print(f"You died in {cl} to {enemy["name"]}...")
        break
     else:
      print("")
  else:
   print("")
  #ending
  if cl == "Citadel":
   print(f"Congratulations! You have finished the game.")
   time.sleep(1)
   game_finished = True
   return 
  
  else:
   print()
  if "item" in prison[cl]:
   del prison[cl]["item"]
   user.inventory["potions"] += 3
   print(f"You found a big potion! it has up to {user.inventory["potions"]} uses.")
  elif "upgrade" in prison[cl]:
   user.attack += 10
   del prison[cl]["upgrade"]
   print(f"Congrats! now your blade does {user.attack} damage.")
  show_exits(cl)
  move = input("").strip().lower()
  if move in prison[cl]["exits"]:
    cl = prison[cl]["exits"][move]
  else:
   print("Please choose a direction.")
   continue

if __name__ == "__main__":
 movement(cl)
