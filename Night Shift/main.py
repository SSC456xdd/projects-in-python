from player import Player
from config import DIFFICULTY_SETTINGS
from config import routes
from animatronic import Animatronic

def start_game() -> dict:
    while True:
        print("Welcome to Night Shift!")
        print("difficulties:")
        print("Easy")
        print("Medium")
        print("Nightmare (Really hard💀)")

        difficulty = input("What difficulty would you like? ").strip().lower()

        if difficulty in DIFFICULTY_SETTINGS:
            settings = DIFFICULTY_SETTINGS[difficulty]
            print(f"Difficulty chosen: {difficulty}.")
            return settings
        else:
            print("Please choose a difficulty!")
            continue

if __name__ == "__main__":
    settings = start_game() #the returning value of start_game is the difficulty settings
    
    freddy = Animatronic("Freddy","stage",settings["freddy"],routes["freddy"])
    chica = Animatronic("Chica","stage",settings["chica"],routes["chica"])
    bonnie = Animatronic("Bonnie","stage",settings["bonnie"],routes["bonnie"])   
    foxy = Animatronic("Foxy","pirate cove 1",settings["foxy"],routes["foxy"])





def game_loop():
    ...

def display_menu():
    ...
def check_game_over():
    ...
def pass_time():
    ...
