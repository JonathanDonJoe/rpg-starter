from character import Character

class Zombie(Character):
    def __init__(self):
        super().__init__("Zombie", 0, 0)

    def alive(self):
        return 999999