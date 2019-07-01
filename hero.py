class Hero():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        self.health -= enemy.power
        enemy.health -= self.power
