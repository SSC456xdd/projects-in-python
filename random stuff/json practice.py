import json

pet = {"name": "Mochi", "age": 6, "toys": ["ball", "rope"]}

# SAVE
with open("pet.json", "w") as f:
    json.dump(pet, f, indent=2)

# LOAD
with open("pet.json", "r") as f:
    loaded = json.load(f)

print(loaded["name"])
print(loaded["toys"])
print(loaded['age'])