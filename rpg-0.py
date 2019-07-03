from character import *
from random import randint, choice



"""
In this simple RPG game, the Character 1 fights the Character 2. He has the options to:

1. fight Character 2
2. do nothing - in which case the Character 2 will attack him anyway
3. flee

"""

def create_hero():

    # jobs_dict = {
    #     "1":"Hero",
    #     "2":"Medic",
    #     "3":"Shadow",
    #     "4":"Wizard",
    #     "5":"Tank",
    #     "6":"Drunkard"
    # }


    print("Time to create your character!")
    name = input("What is your character's name?: ")   
    print("") 
    job_selection = input("What is %s's class?\n1. Hero\n2. Medic\n3. Shadow\n4. Wizard\n5. Tank\n6. Drunkard\n: " % name)    
    print("")
    health = randint(100,150)
    power = (randint(5,10))


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

        action = input("Where do you want to go?\n1. Explore\n2. Shop\n3. Use item\n4. Quit\n: ")
        print("")
        #Battle
        if action == "1":
            # name = choice(char_list)
            job_index = randint(0,7)
            # char2 = Character(name,name,randint(30,50), randint(5,7))
            job = char_list[job_index]
            job_selection_dict = {
                "0":Hero(job, randint(30,50), randint(5,7)),
                "1":Medic(job, randint(30,50), randint(5,7)),
                "2":Shadow(job, 1, randint(5,7)),
                "3":Wizard(job, randint(30,50), randint(5,7)),
                "4":Tank(job, randint(30,50), randint(5,7)),
                "5":Drunkard(job, randint(30,50), randint(5,7)),
                "6":Zombie(job, randint(30,50), randint(1,2)),
                "7":Goblin(job, randint(30,50), randint(3,5))
            }
            char2 = job_selection_dict[str(job_index)]

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
            print("%s ran away" % char1.name)
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

def Store(character):
    shopping = True
    while shopping:
        items_dict = {'1':'SuperTonic', '2':'Armor', '3':'Cloak', '4':'Sword', '5': 'Broadsword'}
        items_price_dict = {'1':5, '2':10, '3':20, '4':20, '5':50}

        print("%s has %d gold" %(character.name, character.wealth))

        item = input("What do you want to buy?\n1. SuperTonic - 5g\n2. Armor - 10g\n3. Cloak -2 0g\n4. Sword - 20g\n5. Broadsword - 50g\n0. Quit\n:")
        print("")
        if item == '0':
            shopping = False
        elif int(item) in [1,2,3,4,5] and character.wealth < items_price_dict[item] :
            print("%s can't afford this" % character.name)
            still_shopping = input("Continue shopping?\n1. Yes\n2. No\n: ")
            if still_shopping.lower() == "n" or still_shopping.lower() == "no" or still_shopping.lower() == "2":
                shopping = False
            elif still_shopping.lower() == "y" or still_shopping.lower() == "yes" or still_shopping.lower() == "1":
                pass
            else:
                print("Invalid input.  Leaving shop.")
                shopping = False
        elif int(item) in [1,2,3,4,5] and character.wealth >= items_price_dict[item]:
            character.wealth -= items_price_dict[item]
            character.inventory.append(items_dict[item])
            print("%s bought the %s" %(character.name, items_dict[item]))
            still_shopping = input("Continue shopping?\n1. Yes\n2. No\n: ")
            print("")
            if still_shopping.lower() == "n" or still_shopping.lower() == "no" or still_shopping.lower() == "2":
                shopping = False
            elif still_shopping.lower() == "y" or still_shopping.lower() == "yes" or still_shopping.lower() == "1":
                pass
            else:
                print("Invalid input.  Leaving shop.")
                shopping = False            
        else:
            print("Invalid input.  Exiting shop. ")
            shopping = False
        print("")

# class SuperTonic():
#     def use(self, char):
#         heal = 10
#         char.health += 10
#         print("%s has healed %d by using a SuperTonic" % (char.name, heal))

# class Armor():
#     def use(self, char):
#         #takes 2 less dmg
#         print("%s equipped Armor to gain 2 armor." % char.name)

# class Cloak():
#     def use(self, char):
#         #+2 evade
#         print("%s equipped Cloak to gain 2 evasion." % char.name)
    


def use_item(char1):
    # print(char1.inventory)
    status = True
    while status:
        print("What do you want to use?: ")
        for i,item in enumerate(char1.inventory):
            print("%d. %s" %(i+1,item))
        print("0. Quit")
        #item number they want to use
        request = int(input(":"))
        print("")
        if request == 0:
            status = False
        elif request <= len(char1.inventory) and request > 0 :
            if char1.inventory[request-1] == "SuperTonic":
                char1.health += 10
                print("%s gained 10 health from the SuperTonic.  Current health is now %d"%(char1.name, char1.health))
            if char1.inventory[request-1] == "Armor":
                char1.armor += 2
                print("%s gained 2 armor by equipping the Armor.  Current armor is now %d"%(char1.name, char1.armor))
            if char1.inventory[request-1] == "Cloak":
                char1.evasion += 2
                print("%s gained 2 evasion by equipping the Cloak.  Current evasion is now %d"%(char1.name, char1.evasion))
            if char1.inventory[request-1] == "Sword":
                char1.power += 1
                print("%s gained 1 power by equipping the Sword.  Current power is now %d"%(char1.name, char1.power))
            if char1.inventory[request-1] == "Broadsword":
                char1.power += 2
                char1.evasion -= 1
                print("%s gained 2 power, but lost 1 evasion by equipping the Broadsword.  Current power is now %d.  Current evasion is now %d"%(char1.name, char1.power, char1.evasion))                
            del char1.inventory[request-1]
            status = False

        else:
            print("Select a valid item.")


#Play
protagonist = create_hero()
main(protagonist)
