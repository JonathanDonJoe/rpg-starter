class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("The %s does %d damage to the %s." % (self.name, self.power, enemy.name))
            
    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power))

    def alive(self):
        return self.health > 0