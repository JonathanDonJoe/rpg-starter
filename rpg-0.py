from character import Character
from random import randint, choice
from store import *



"""
In this simple RPG game, the Character 1 fights the Character 2. He has the options to:

1. fight Character 2
2. do nothing - in which case the Character 2 will attack him anyway
3. flee

"""

def create_hero():

    jobs_dict = {
        "1":"Hero",
        "2":"Medic",
        "3":"Shadow",
        "4":"Wizard",
        "5":"Tank",
        "6":"Drunkard"
    }

    print("Time to create your character!")
    name = input("What is your character's name?")    
    job_selection = input("What is your %s's class?\n1. Hero\n2. Medic\n3. Shadow\n4. Wizard\n5. Tank\n6. Drunkard\n:" % name)    
    health = randint(100,150)
    power = (randint(5,10))
    char = Character(name, jobs_dict[job_selection], health, power)
    print("Your character has been created! %s the %s, with starting stats of %d health and %d power" % (name, char.job, char.health, char.power))
    return char


def main(char1):

    in_game = True
    #Overworld
    while in_game:

        # action_dict = {
        #     '1':'Explore',
        #     '2':'Shop',
        #     '4':'Quit'
        # }
        char_list = ['Hero', 'Medic', 'Shadow', 'Wizard', 'Tank', 'Drunkard', 'Zombie', 'Goblin']

        action = input("Where do you want to go?\n1. Explore\n2. Shop\n3. Use item\n4. Quit\n")
        #Battle
        if action == "1":
            name = choice(char_list)
            char2 = Character(name,name,randint(30,50), randint(5,7))
            print("%s encountered a %s!" % (char1.name, char2.name))
            battle(char1, char2)
        elif action == "2":
            Store(char1)
        elif action =="3":
            use_item(char1)
        else:
            in_game = False



def battle(char1, char2):

    fighting = True
    while char2.alive() and char1.alive() and fighting:
        char1.print_status()
        char2.print_status()
        print()
        print("What does %s want to do?" % char1.name)
        print("1. fight %s" % char2.name)
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Character 1 attacks Character 2
            char1.attack(char2)
            if not char2.alive():
                char1.wealth += char2.bounty
                print("%s is dead. %s gains %d gold and now has %d gold" % (char2.name, char1.name, char2.bounty, char1.wealth))
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            fighting = False
        else:
            print("Invalid input %r.  %s loses his turn" % (user_input, char1.name))

        if char2.alive():
            # Character 2 attacks Character 1
            char2.attack(char1)
            if not char1.alive():
                char2.wealth += char1.bounty
                print("%s is dead.  %s gains %d gold and now has %d gold" % (char1.name, char2.name, char1.bounty, char2.wealth))
                print("Game Over")
                exit(0)


def use_item(char1):
    # print(char1.inventory)
    print("What do you want to use?: ")
    for i,item in enumerate(char1.inventory):
        print("%d. %s\n" %(i+1,item))
    print("0. Quit")
    #item number they want to use
    request = int(input(":"))
    if request == 0:
        pass
    elif request < len(char1.inventory) and request > 0 :
        if char1.inventory[request-1] == "SuperTonic":
            char1.health += 10
            print("%s gained 10 health.  Current health is now %d"%(char1.name, char1.health))
        elif char1.inventory[request-1] == "Armor":
            char1.armor += 2
            print("%s gained 2 armor.  Current armor is now %d"%(char1.name, char1.armor))
        if char1.inventory[request-1] == "Cloak":
            char1.evasion += 2
            print("%s gained 2 evasion.  Current evasion is now %d"%(char1.name, char1.evasion))
        del char1.inventory[request-1]
        
    else:
        print("Select a valid item.")


#Play
protagonist = create_hero()
main(protagonist)
