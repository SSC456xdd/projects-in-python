
class Character:
    def __init__(self,name,hp,attack,max_hp):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.max_hp = max_hp
        self.inventory = {
           "potions": 0,
           "upgrades": 0
             }
    def take_damage(self,amount):
        self.hp = max(self.hp - amount, 0)
    def healing(self,amount):
        self.hp = min(self.hp + amount, self.max_hp)
    def is_alive(self):
     if self.hp > 0:
        return True
     else:
        return False








