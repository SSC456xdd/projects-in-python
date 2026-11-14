
import random # movement for animatronics

class Animatronic:
    def __init__(self,name,location,aggression,route):
        self.name = name
        self.location = location
        self.aggression = aggression
        self.route = route
        self.active = False
    def move(self):
        current_location = self.route.index(self.location) # looks for the location in the list and then assigns 
        #the value to the variable "current_location".
        probability = random.randint(1,100)
        if probability <= self.aggression:
            rooms = len(self.route)
            rooms -= 1
            if current_location == rooms: #when animatronic reaches the office
                pass #
            else: #else: animatronic NOT in office
                current_location += 1
                a = self.route[current_location]
                self.location = a
        else:
            pass

    def check_location(self) -> bool:
        if self.location == "office":
            return True
        else:
            return False
