import json

pet = {"name": "Mochi", "age": 6, "toys": ["ball", "rope"]}

try:
    with open("scores.json", "r") as f:
        scores = json.load(f)
except FileNotFoundError:
    scores = {"best": 0}
    print("No scores yet, starting fresh.")

# SAVE
#with open("pet.json", "w") as f:
#    json.dump(pet, f, indent=2)

# LOAD
with open("pet.json", "r") as f:
    loaded = json.load(f)

try:
    with open("scores.json", "r") as f:
        scores = json.load(f)
except FileNotFoundError:
    scores = {"best": 0}
    print("No scores yet, starting fresh.") 
print(loaded["name"])
print(loaded["toys"])
print(loaded['age'])