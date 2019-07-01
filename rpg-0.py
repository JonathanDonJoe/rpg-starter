from character import Character

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    char1 = Character("Hero",'hero', 10, 11)
    # char2 = Character("Goblin",6,2)
    char2 = Character('Bob','drunkard',100,1)

    while char2.alive() and char1.alive():
        char1.print_status()
        char2.print_status()
        print()
        print("What do you want to do?")
        print("1. fight %s" % char2.name)
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            char1.attack(char2)
            if not char2.alive():
                char1.wealth += char2.bounty
                print("%s is dead. %s gains %d gold and now has %d gold" % (char2.name, char1.name, char2.bounty, char1.wealth))
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r.  %s loses his turn" % (user_input, char1.name))

        if char2.alive():
            # Goblin attacks hero
            char2.attack(char1)
            if not char1.alive():
                char2.wealth += char1.bounty
                print("%s is dead.  %s gains %d gold and now has %d gold" % (char1.name, char2.name, char1.bounty, char2.wealth))

main()
