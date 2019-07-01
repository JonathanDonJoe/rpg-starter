from character import Character

class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health,power)    
    
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))