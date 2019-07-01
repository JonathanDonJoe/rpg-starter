class Hero():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        enemy.health -= self.power
