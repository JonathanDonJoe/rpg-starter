from character import Character

def Store(character):
    shopping = True
    while shopping:
        items_dict = {'1':'SuperTonic', '2':'Armor', '3':'Cloak'}
        items_price_dict = {'1':5, '2':10, '3':20}

        print("%s has %d gold" %(character.name, character.wealth))

        item = input("What do you want to buy?\n1. SuperTonic - 5g\n2. Armor - 10g\n3. Cloak -20g\n4. Quit\n:")
        
        if item == '4':
            shopping = False
        elif int(item) in [1,2,3] and character.wealth < items_price_dict[item] :
            print("%s can't afford this" % character.name)
            still_shopping = input("Continue shopping?\n1. Yes\n2. No\n: ")
            if still_shopping.lower() == "n" or still_shopping.lower() == "no" or still_shopping.lower() == "1":
                shopping = False
            elif still_shopping.lower() == "y" or still_shopping.lower() == "yes" or still_shopping.lower() == "2":
                pass
            else:
                print("Invalid input.  Leaving shop.")
                shopping = False
        elif int(item) in [1,2,3] and character.wealth >= items_price_dict[item]:
            character.wealth -= items_price_dict[item]
            character.inventory.append(items_dict[item])
            print("%s bought %s" %(character.name, items_dict[item]))
            still_shopping = input("Continue shopping?\n1. Yes\n2. No\n: ")
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
    
