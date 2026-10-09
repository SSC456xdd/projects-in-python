import random
import time
while True:
 gs = input("Would you like to play ? (y/n)").strip().lower()
 if gs in ['yes','y']:
  pcs = 0
  uss = 0
  while pcs < 3 and uss < 3 :
   print("Rolling your dice...")
   time.sleep(1)
   usr = random.randint(1,6)
   print(f"You rolled {usr}!")
   time.sleep(2)
   print("Rolling computers dice...")
   time.sleep(1)
   pcr = random.randint(1,6)
   print(f"Computer rolled {pcr}!")
   if pcr > usr:
     pcs += 1
     print(f"Computer has {pcs} point(s). You have {uss} point(s). ")
   elif pcr < usr:
     uss += 1
     print(f"Computer has {pcs} point(s). You have {uss} point(s). ")
   else:
     print("Its a tie!")
  if pcs == 3:
    print("Computer wins!")
  elif uss == 3:
    print("You win!")
 elif gs  in ["no","n"]:
  print("Until next time!")
  break
 else :
  print("Please choose yes or no")
