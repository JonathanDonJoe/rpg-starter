class SuperTonic():
    def __init__(self):
        self.name = 'SuperTonic'
        self.price = 5
    def apply(self, char):
        char.health += 10
        print("%s gained 10 health from the SuperTonic.  Current health is now %d"%(char.name, char.health))

class Armor():
    def __init__(self):
        self.name = 'Armor'
        self.price = 10
    def apply(self, char):
        char.armor += 2
        print("%s gained 2 armor by equipping the Armor.  Current armor is now %d"%(char.name, char.armor))

class Cloak():
    def __init__(self):
        self.name = 'Cloak'
        self.price = 20
    def apply(self, char):
        char.evasion += 2
        print("%s gained 2 evasion by equipping the Cloak.  Current evasion is now %d"%(char.name, char.evasion))

class Sword():
    def __init__(self):
        self.name = 'Sword'
        self.price = 20
    def apply(self, char):
        char.power += 1
        print("%s gained 1 power by equipping the Sword.  Current power is now %d"%(char.name, char.power))
        
class Broadsword():
    def __init__(self):
        self.name = 'Broadsword'
        self.price = 50
    def apply(self, char):
        char.power += 4
        char.evasion -= 1
        print("%s gained 4 power, but lost 1 evasion by equipping the Broadsword.  Current power is now %d.  Current evasion is now %d"%(char.name, char.power, char.evasion))  