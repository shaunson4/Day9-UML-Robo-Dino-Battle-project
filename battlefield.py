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
        while self.robot.health != 0 or self.dinosaur.health != 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
        # dino attacks, print results
        # continue attacks until one combatant is eliminated
        
        # Endgame Section
        # Display winner
    def display_winner(self):
        pass
