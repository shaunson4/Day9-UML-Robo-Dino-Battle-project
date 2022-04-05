from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('blow torch', 55)
        self.weapon_one = Weapon('grenade launcher', 25)
        self.weapon_two = Weapon('blow torch', 55)
        self.weapon_three = Weapon('machine gun', 15)

    def attack(self, Dinosaur):
        # lower dino's health by attack power of weapon
        Dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacks {Dinosaur.name} with his {self.active_weapon.name} for {self.active_weapon.attack_power} damage. {Dinosaur.name} current health is: {Dinosaur.health}' )

                        

   
        