from character import Character

user = Character("Mochi",100,10,100)

prison = {
 "Cell": {
  "description": "An old, worn out bed and a hole big enough you could go through it.",
  "exits": {"east": "Cell block"} 
 },
 "Cell block": {
  "description": "You see a group of bugs eating something off the wall.",
  "enemy": Character("Fungi eater", 25, 2, 25),
  "exits":{"west":"Cell", "north": "Storage", "east": "Root tunnel"}
 },
 "Storage": {
  "description": "You see a potion behind a crate and decide to grab it.",
  "exits":{"south": "Cell block"},
  "item": "Healing potion"
 },
 "Root tunnel": {
  "description": "While crossing this empty shell of a tree, you see a group of something flying.",
  "enemy": {"name": "Flying mosquito", 'hp': 50, 'attack': 5, 'max_hp': 50},
  "exits": {"west": "Cell block", "east": "Guarder's hall", "north": "Armory"}
 },
 "Armory": {
  "description": "Between lots of rusty weapons, you find one that might upgrade something for you.",
  "exits":{"south": "Root tunnel"},
  "upgrade": 'Blade sharpener'
 },
 "Guarder's hall": {
  "description": "You see a big door.",
  "enemy": {"name": "Guard husk", "hp": 75, "attack": 8, 'max_hp': 75},
  "exits": {"west": "Root tunnel", "east": "Jailer's hall"}
 },
 "Jailer's hall": {
  "description": "The place where the guardian of the entire prison rests.",
  "exits":{"west": "Guarder's hall", "east": "Gate"},
  "enemy": {"name": "Agoner", "hp": 150, "attack": 15, 'max_hp': 200,
  "intro": "Agoner: Who's there? Why would you leave your cell, prisoner? You will get punished for this!",
  "outro": "Agoner: Sorry it had to be this way... I know you're innocent but I can't do anything about it..."
  }

 },
 "Gate": {
  "description": "At last, you finally are able to leave and go to the city",
  "exits": {"north": "Citadel"}
 },
 "Citadel": {
  "description": "A beautiful city with lots of crime, you see where you were arrested wrongfully.",
  "exits": {}
 }
}

placeholder = {


    "cheeseburger"

}