# True == door is closed
#False == door is open

import random

class Player:
    def __init__(self):
        self.power = 100.0
        self.left_door = False
        self.right_door = False
        
    def show_status(self):
        print(f"You have {self.power} power left!")

    def close_door(self,side):
        if side == "left":    
            if self.left_door == False:
                self.left_door = True
                print("Door closed!")
            else:
                print("Door is already closed!")
        elif side == "right": # ik i can use "else" but this makes code more readable.
            if self.right_door == False:
                self.right_door = True
                print("Door closed!")
            else:
                print("Door is already closed!")


    def open_door(self,side):
        if side == "left":
            if self.left_door == True:
                self.left_door = False
                print("Door opened!")
            else:
                print("Door already opened!")
        elif side == "right": # ik i can use "else" but this makes code more readable.
            if self.right_door == True:
                self.right_door = False
                print("Door opened!")
            else:
                print("Door already opened!")


    def use_power(self,power_being_used):
            self.power -= power_being_used

    def add_power(self):
        extra_power = random.randint(15,30)
        self.power += extra_power

