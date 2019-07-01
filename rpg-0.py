from hero import Hero
from goblin import Goblin

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    hero1 = Hero(10, 5)
    goblin1 = Goblin(6,2)

    while goblin1.health > 0 and hero1.health > 0:
        print("You have %d health and %d power." % (hero1.health, hero1.power))
        print("The goblin has %d health and %d power." % (goblin1.health, goblin1.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            goblin1.health -= hero1.power
            print("You do %d damage to the goblin." % hero1.power)
            if goblin1.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin1.health > 0:
            # Goblin attacks hero
            hero1.health -= goblin1.power
            print("The goblin does %d damage to you." % goblin1.power)
            if hero1.health <= 0:
                print("You are dead.")

main()
