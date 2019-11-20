from character import Hero, Medic, Shadow, Tank, Zombie, Goblin, Wizard, Drunkard
from items import *
from random import randint, choice



"""
In this simple RPG game, the Character 1 fights the Character 2. He has the options to:

1. fight Character 2
2. do nothing - in which case the Character 2 will attack him anyway
3. flee

"""

def create_hero():

    print("Time to create your character!")
    name = input("What is your character's name?: ")   
    print() 
    job_selection = input("What is %s's class?\n1. Hero\n2. Medic\n3. Shadow\n4. Wizard\n5. Tank\n6. Drunkard\n: " % name)    
    print()
    health = randint(100,150)
    power = randint(5,10)


    job_selection_dict = {
        "1":Hero(name, health, power),
        "2":Medic(name, health, power),
        "3":Shadow(name, health, power),
        "4":Wizard(name, health, power),
        "5":Tank(name, health, power),
        "6":Drunkard(name, health, power)
    }


    # char = Character(name, job_selection_dict[job_selection], health, power)
    char = job_selection_dict[job_selection]
    print("Your character has been created! %s the %s, with starting stats of %d health and %d power" % (name, char.job, char.health, char.power))
    return char

def battle_random(char1):
    # name = choice(char_list)
    char_list = ['Hero', 'Medic', 'Shadow', 'Wizard', 'Tank', 'Drunkard', 'Zombie', 'Goblin']
    job_index = randint(0,7)
    # char2 = Character(name,name,randint(30,50), randint(5,7))
    job = char_list[job_index]

    random_health = randint(30, 50)
    random_power = randint(5, 7)

    job_selection_dict = {
        "0":Hero(job, random_health, random_power),
        "1":Medic(job, random_health, random_power),
        "2":Shadow(job, 1, random_power),
        "3":Wizard(job, random_health, random_power),
        "4":Tank(job, random_health, random_power),
        "5":Drunkard(job, random_health, random_power),
        "6":Zombie(job, random_health, randint(1,2)),
        "7":Goblin(job, random_health, randint(3,5))
    }


    char2 = job_selection_dict[str(job_index)]

    print("%s encountered a %s!" % (char1.name, char2.name))
    battle(char1, char2)


def battle(char1, char2):

    fighting = True
    while char2.alive() and char1.alive() and fighting:
        char1.print_status()
        char2.print_status()
        print()
        print("What does %s want to do?" % char1.name)
        print("1. Fight %s" % char2.name)
        print("2. Use item")
        print("3. Do nothing")
        print("4. Flee")
        print(": ", end = "")
        user_input = input()
        print("")
        if user_input == "1":
            # Character 1 attacks Character 2
            char1.attack(char2)
            if not char2.alive():
                char1.wealth += char2.wealth
                print("%s has died. %s gains %d gold and now has %d gold\n" % (char2.name, char1.name, char2.wealth, char1.wealth))
        elif user_input == "2":
            use_item(char1)
        elif user_input == "3":
            print("%s decided to do nothing.  Why is this even an option?" %char1.name)
        elif user_input == "4":
            print("%s ran away like a coward." % char1.name)
            fighting = False
        else:
            print("Invalid input %r.  %s loses his turn" % (user_input, char1.name))

        if char2.alive():
            # Character 2 attacks Character 1
            char2.attack(char1)
            if not char1.alive():
                char2.wealth += char1.wealth
                print("%s is dead.  %s gains %d gold and now has %d gold" % (char1.name, char2.name, char1.wealth, char2.wealth))
                print("Game Over.  Try not dying next time.")
                exit(0)

def store(character):
    shopping = True
    while shopping:
        items_dict = {'1':SuperTonic(), '2':Armor(), '3':Cloak(), '4':Sword(), '5': Broadsword()}

        print("%s has %d gold" %(character.name, character.wealth))

        item = input("What do you want to buy?\n1. SuperTonic - 5g\n2. Armor - 10g\n3. Cloak - 20g\n4. Sword - 20g\n5. Broadsword - 50g\n0. Quit\n:")
        print("")
        if item == '0':
            shopping = False
        elif int(item) in [1,2,3,4,5] and character.wealth < items_dict[item].price :
            print("%s can't afford this" % character.name)
            shopping = continue_shopping()
        elif int(item) in [1,2,3,4,5] and character.wealth >= items_dict[item].price:
            character.wealth -= items_dict[item].price
            character.inventory.append(items_dict[item])
            print("%s bought the %s" %(character.name, items_dict[item].name))
            shopping = continue_shopping()     
        else:
            print("Invalid input.  Exiting shop. ")
            shopping = False
        print("")

def continue_shopping():
    shopping = True
    still_shopping = input("Continue shopping?\n1. Yes\n2. No\n: ")
    print("")
    if still_shopping.lower() == "n" or still_shopping.lower() == "no" or still_shopping.lower() == "2":
        shopping = False
    elif still_shopping.lower() == "y" or still_shopping.lower() == "yes" or still_shopping.lower() == "1":
        pass
    else:
        print("Invalid input.  Leaving shop.")
        shopping = False      
    return shopping  


def use_item(char1):
    status = True
    while status:
        print("What do you want to use?: ")
        for i,item in enumerate(char1.inventory):
            print("%d. %s" %(i+1,item.name))
        print("0. Quit")
        #item number they want to use
        request = int(input(":"))
        print("")
        if request == 0:
            status = False
        elif request <= len(char1.inventory) and request > 0 :
            char1.inventory[request-1].apply(char1)          
            del char1.inventory[request-1]
            status = False

        else:
            print("Select a valid item.")

