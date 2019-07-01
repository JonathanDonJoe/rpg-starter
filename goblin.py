from character import Character

class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health,power) 

    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))