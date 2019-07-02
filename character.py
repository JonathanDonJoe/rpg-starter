from random import randint

class Character():
    def __init__(self, name, job, health, power):

        self.name = name
        self.job = job
        self.health = health
        self.power = power
        self.wealth = 100
        self.bounty = 1
        self.evasion = 0
        self.armor = 0
        self.inventory = []

        #set bounty for how much gold your death is worth
        if self.job.lower() == 'hero':
            self.bounty = 10
        if self.job.lower() == 'medic':
            self.bounty = 7
        if self.job.lower() == 'shadow':
            self.bounty = 6
        if self.job.lower() == 'tank':
            self.bounty = 14
        if self.job.lower() == 'zombie':
            self.bounty = 0
        if self.job.lower() == 'goblin':
            self.bounty = 4
        if self.job.lower() == 'wizard':
            self.bounty = 8
        if self.job.lower() == 'drunkard':
            self.bounty = 100

        #Set all shadow's initial health equal to 1
        if job.lower() == "shadow":
            self.health = 1

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
            actual_dmg = 1
        enemy.health -= actual_dmg

        print("%s does %d damage to the %s." % (self.name, actual_dmg, enemy.name))
        #20% chance for medic to heal 2 health after being attacked
        if enemy.job.lower() == "medic":
            roll = randint(1,5)
            if roll == 1:
                enemy.health += 2
                print("%s has healed %d health!" % (enemy.name, 2))
    
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