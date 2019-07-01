class Hero():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        return self.health > 0
    
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))