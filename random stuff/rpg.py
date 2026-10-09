import random
import time


LOCATION = "Village square"
LOCATIONS = {
    "north": "Whispering Roots",
    "south": "Sunken Ruins",
    "east": "Moonlit Lake",
    "west": "Abandoned Watchtower",
}

has_clue = False
has_key = False


def win():
    print("The secret locked behind a stone chamber read the traveler you've encountered before")
    print("is secretly a god testing the patience of whoever coded this game.")
    print("Congrats! You completed the game!")


def story_start():
    print("You are a traveler who entered a village.")
    print("You see a paper that says there is a secret in a place called 'Sunken Ruins'.")
    print("You decide to find out what the secret is.")
    print("The directions are north, south, east, and west.")
    print(f"You are at {LOCATION}!")
    move_sys()


def menu():
    global has_clue, has_key

    while True:
        name = input("What is your name? ").strip().capitalize()
        print(f"Welcome {name}, would you like to play? (y/n)")
        game = input("You: ").strip().lower()
        if game in ("yes", "y"):
            has_clue = False
            has_key = False
            print("Loading game...")
            time.sleep(1)
            story_start()
        elif game in ("no", "n"):
            print(f"Until next time, {name}!")
            return
        else:
            print("Please say yes or no.")


def move_sys():
    while True:
        print("Where would you like to go? (north/south/east/west, or quit)")
        direction = input("You: ").strip().lower()
        if direction == "quit":
            print("Until next time!")
            return
        if direction not in LOCATIONS:
            print("Please type a direction or quit.")
            continue

        print(f"You are now at {LOCATIONS[direction]}!\n")
        if direction == "north":
            north()
        elif direction == "south":
            if south():
                return
        elif direction == "east":
            east()
        else:
            west()


def north():
    global has_clue

    print("You hear the creaks of the roots below you.")
    print("You can inspect the tree or exit.")
    choice = input("You: ").strip().lower()
    if choice == "inspect":
        has_clue = True
        print("You found a mysterious paper. You cannot tell what it says.")
    elif choice == "exit":
        print(f"Going back to {LOCATION}...")
    else:
        print("Please type inspect or exit.")


def south():
    print("You see the ruins and wonder what happened here.")
    if not has_key:
        print("You see a locked stone chamber. You do not have its key yet.")
        return False

    print("You see the locked stone chamber. Would you like to open it? (yes/no)")
    choice = input("You: ").strip().lower()
    if choice in ("yes", "y"):
        win()
        return True
    if choice in ("no", "n"):
        print(f"Going back to {LOCATION}...")
        return False
    print("Please choose yes or no.")
    return False


def east():
    print("You see the lake glow from the light of the moon.")
    print("You see a traveler. Go talk to him? (yes/no)")
    choice = input("You: ").strip().lower()
    if choice in ("yes", "y"):
        if has_clue:
            print("The traveler explains that the paper points to a rusty key at the watchtower.")
        else:
            print("The traveler says he may be able to help if you find a clue first.")
    elif choice in ("no", "n"):
        print("Leaving Moonlit Lake...")
    else:
        print("Please choose yes or no.")


def west():
    global has_key

    print("You see everything from the top of the watchtower.")
    if has_key:
        print("The soldier is no longer guarding the rusty key.")
        return

    print("You see a soldier guarding something. Would you like to battle? (y/n)")
    choice = input("You: ").strip().lower()
    if choice in ("no", "n"):
        print("You leave the soldier alone and return to the village square.")
        return
    if choice not in ("yes", "y"):
        print("Please choose yes or no.")
        return

    player_health = 30
    soldier_health = 24
    print("The battle begins! Choose attack, defend, or run.")
    while player_health > 0 and soldier_health > 0:
        print(f"Your health: {player_health} | Soldier health: {soldier_health}")
        action = input("You: ").strip().lower()
        if action == "run":
            print("You retreat from the battle.")
            return
        if action == "attack":
            damage = random.randint(6, 10)
            soldier_health = max(0, soldier_health - damage)
            print(f"You hit the soldier for {damage} damage.")
        elif action == "defend":
            print("You brace yourself and reduce the next hit.")
        else:
            print("Choose attack, defend, or run.")
            continue

        if soldier_health > 0:
            damage = random.randint(4, 8)
            if action == "defend":
                damage = max(1, damage // 2)
            player_health -= damage
            print(f"The soldier hits you for {damage} damage.")

    if player_health > 0:
        has_key = True
        print("You defeated the soldier and found a rusty key!")
    else:
        print("The soldier defeats you. You retreat to the village square and can try again.")


if __name__ == "__main__":
    menu()