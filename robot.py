from weapon import Weapon

weapon_one = Weapon('grenade launcher', 25)
weapon_two = Weapon('blow torch', 50)
weapon_three = Weapon('machine gun', 15)


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('grenade launcher', 25)

    def attack(self, Dinosaur):
        # lower dino's health by attack power of weapon
        Dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacks {Dinosaur.name} with his {self.active_weapon.name} for {self.active_weapon.attack_power} damage. {Dinosaur.name} current health is: {Dinosaur.health}' )

                        

   
        