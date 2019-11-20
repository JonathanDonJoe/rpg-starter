from game_elements import create_hero, battle_random, battle, store, continue_shopping, use_item

def main():

    in_game = True
    char1 = create_hero()

    #Overworld
    while in_game:

        action = input("Where do you want to go?\n1. Explore\n2. Shop\n3. Use item\n4. Quit\n: ")
        print("")
        #Battle
        if action == "1":
            battle_random(char1)
        elif action == "2":
            store(char1)
        elif action =="3":
            use_item(char1)
        else:
            in_game = False


#Play
main()
