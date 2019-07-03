from random import randint

class Character():
    def __init__(self, name, job, health, power):

        self.name = name
        self.job = job
        self.health = health
        self.power = power
        self.wealth = 10
        self.bounty = 1
        self.evasion = 0
        self.armor = 0
        self.inventory = []

        #set bounty for how much gold your death is worth
        # if self.job.lower() == 'hero':
        #     self.bounty = 10
        # if self.job.lower() == 'medic':
        #     self.bounty = 7
        # if self.job.lower() == 'shadow':
        #     self.bounty = 6
        # if self.job.lower() == 'tank':
        #     self.bounty = 14
        # if self.job.lower() == 'zombie':
        #     self.bounty = 1
        # if self.job.lower() == 'goblin':
        #     self.bounty = 2
        # if self.job.lower() == 'wizard':
        #     self.bounty = 8
        # if self.job.lower() == 'drunkard':
        #     self.bounty = 100

        #Set all shadow's initial health equal to 1
        # if job.lower() == "shadow":
        #     self.health = 1

    #Character attacks and enemy character
    def attack(self, enemy):
        dmg = self.power
        #20% chance for hero to deal double dmg on hit
        if self.job.lower() == "hero":
            roll = randint(1,5)
            if roll == 1:
                dmg = self.power *2 
                print("%s threw a Critical Hit!" % self.name)
        dmg = int(dmg * enemy.is_hit_factor())
        actual_dmg = dmg - enemy.armor
        if actual_dmg < 1:
            if enemy.job.lower() == 'shadow' or enemy.job.lower() == 'drunkard':
                actual_dmg = 0
            else:
                actual_dmg = 1
        enemy.health -= actual_dmg

        print("%s does %d damage to %s." % (self.name, actual_dmg, enemy.name))
        #20% chance for medic to heal 2 health after being attacked
        if enemy.job.lower() == "medic" and enemy.alive() == True:
            roll = randint(1,1)
            if roll == 1:
                enemy.health += 2
                print("%s healed himself %d health." % (enemy.name, 2))
    
    #10% chance for shadow to get hit
    def is_hit_factor(self):
        hit = 1
        roll = 10
        if self.job.lower() == 'shadow':
            roll = randint(1,10)
            if roll >1:
                hit = 0
                print("%s dodged the hit!" % self.name)
        #Tanks take half damage, rounded up
        if self.job.lower() == 'tank':
            hit = 0.5
        #Drunkard has an equal chance to take no damage and double damage
        if self.job.lower() == 'drunkard':
            roll = randint(1,2)
            if roll ==1:
                hit = 2
                print("%s didn't even notice he was getting attacked, so he got hit twice." %self.name)
            else:
                hit = 0
                print("%s tripped on his own feet and accidently dodged the attack." %self.name)
        if self.evasion > 8:
            new_roll = randint(1,2)
            if new_roll == 1:
                hit = 0
        elif self.evasion > 4:
            new_roll = randint(1,100)
            if new_roll <= 15:
                hit = 0
        elif self.evasion > 2:
            new_roll = randint(1,10)
            if new_roll == 1:
                hit = 0
        return hit

    #print status of character        
    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

    #check if character is alive
    def alive(self):
        alive = self.health > 0
        #Zombies never die
        if self.job.lower() == 'zombie':
            alive = True
        return alive

class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, "Hero", health, power)
        self.bounty = 10
class Medic(Character):
    def __init__(self, name, health, power):
        super().__init__(name, "Medic", health, power)
        self.bounty = 7
class Shadow(Character):
    def __init__(self, name, health, power):
        super().__init__(name, "Shadow", 1, power)
        self.bounty = 6
class Tank(Character):
    def __init__(self, name, health, power):
        super().__init__(name, "Tank", health, power)
        self.bounty = 14
class Zombie(Character):
    def __init__(self, name, health, power):
        super().__init__(name, "Zombie", health, power)
        self.bounty = 1
class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, "Goblin", health, power)
        self.bounty = 2
class Wizard(Character):
    def __init__(self, name, health, power):
        super().__init__(name, "Wizard", health, power)
        self.bounty = 8
class Drunkard(Character):
    def __init__(self, name, health, power):
        super().__init__(name, "Drunkard", health, power)
        self.bounty = 100