class character:
 def __init__(self,name,hp,attack):
  self.name = name
  self.hp = hp
  self.max_hp = hp
  self.attack = attack

 def showstats(self):
  print(f"{self.name}'s HP: {self.hp}/{self.max_hp}")
  print(f"{self.name}'s attack: {self.attack}")

hero = character("Knight", 50, 10)
guard = character("Prison Guard", 30, 6)

#hero.showstats()
#guard.showstats()

class potions:
 def __init__(self,name,hp,number):
  self.name = name
  self.hp = hp
  self.number = number

 def  use(self):
   if self.number == 0:
       print("You can't use this potion anymore.")
   elif self.number > 0:
    self.number -= 1
    print(f"You used {self.name}!")
    print(f"{self.number} uses left.")

   

 def showinfo(self):
  print(f"{self.name} heals {self.hp}HP.")
  print(f"{self.name} has {self.number} uses.")

big_potion = potions("Big potion", 100, 5)
smolpotion = potions("Small potion", 50, 2)
#big_potion.showinfo()
#smolpotion.showinfo()
while True:
 c1 = input("Would you like to use a potion?(y/n) ").strip().lower()
 if c1 in ["yes","y"]:
  while True:
   c2 = input("Which potion would you like to use? (small or big or leave?) ").strip().lower()
   if c2 == "big":
    big_potion.use()
   elif c2 == "small":
    smolpotion.use() 
   elif c2 in ['quit','leave']:
    break
   else:
    print("Please choose a potion")
    continue
 elif c1 in ['no',"n"]:
  print("Until next time!")
  break
 else:
  print("Please type yes or no.")
  continue


