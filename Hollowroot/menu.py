import time


usrname = input("What is your hero's name? ").strip().capitalize()
print(f"Hello, {usrname}!")
def mainmenu(usrname):
  while True:
   print("Would you like to play?",end="\n")
   opt1 = input("(y/n)? ").strip().lower()
   if opt1 in ['yes', 'y']:
    if __name__ == "__main__":
     from movement import story
     print("Loading Hollowroot...")
     time.sleep(3)
     print("game loaded!")
     print(" ")
     story()
     from movement import game_finished
     if game_finished == story():
      break
   elif opt1 in ['no','n']:
    print("Until next time!")
    time.sleep(1)
    break
   else:
    print("Please choose yes or no.")

mainmenu(usrname)