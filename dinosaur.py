
class Dinosaur:
    def __init__(self, dino_name, attack_power):
        self.name = dino_name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, Robot):
        Robot.health -= self.attack_power
        print(f'{self.name} attacks {Robot.name} for 50 damage. {Robot.name} current health is: {Robot.health} ')
        # lower robot's health by attack_power's value
        
