from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot('Terminator')
        self.dinosaur = Dinosaur('Barney',50)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to the game of a Robot VERSUS Dinosaur')
         
    def battle_phase(self):
        # robot attacks, print results
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
    
    def display_winner(self):
        if self.robot.health == 0:
            print(f'{self.dinosaur.name} is the WINNER!')
        else:
            print(f'{self.robot} is the WINNER!')    
