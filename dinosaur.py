
class Dinosaur:
    def __init__(self):
        self.name = " "
        self.attack_power = 35
        self.health = 100

    def attack(self, Robot):
        self.health -= Robot
        print(self.health)
        
