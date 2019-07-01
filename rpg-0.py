from character import Character
from zombie import Zombie

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    hero1 = Character("Hero",10, 5)
    # goblin1 = Character("Goblin",6,2)
    goblin1 = Zombie()

    while goblin1.alive() and hero1.alive():
        hero1.print_status()
        goblin1.print_status()
        print()
        print("What do you want to do?")
        print("1. fight %s" % goblin1.name)
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero1.attack(goblin1)
            if not goblin1.alive():
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin1.alive():
            # Goblin attacks hero
            goblin1.attack(hero1)
            if not hero1.alive():
                print("You are dead.")

main()
