play = True
action = input("Welcome to the escape room dungeon. Try anything (I suggest you look around)")
#store items in an 'inventory' array
inventory = []
score = 0
glass = True
knife = False
key = False
trapdoor = False
while play == True:
#look around
    if action.lower() == "look around":
            action = input("There is a bed to your left, a glass of water on the floor in front of you, a locked metal door to your right and a boarded up window behind you. (The room stays orientated this way regardless of what moves you make.) \nLeft, right, forward or back?")
            continue
#go forward
    elif action.lower() == "go forward" or action.lower() == "forward":
        while glass == True:
            action = input("There's a glass of water on the floor in front of you. Don't knock it over.")
            if action.lower() == "pick up glass" or action.lower() == "take glass" or action.lower() =="drink water" or action.lower() =="drink glass of water" or action.lower() == "drink":
                print("*drinks water*")
                score = score + 5
                print("Score:", score)
                inventory.append("empty glass")
                glass = False
                print("Inventory:", inventory)
                action = input("No longer thirsty. You'll need that for survival.\nLeft, forward, right or back?")
                continue
            elif action.lower() == "knock over glass" or action.lower() == "knock it over":
                glass = False
                score = score - 5
                print("Score:", score)
                inventory.append("broken glass")
                print("Inventory:", inventory)
                action = input("You're terrible at survival.")
                continue
            else:
                break
#after water has been drank, it can't be drank again (or knocked over)
        while glass == False:
            if action.lower() == "pick up glass" or action.lower() == "drink" or action.lower() == "take glass" or action.lower() =="drink water" or action.lower() =="drink glass of water" or action.lower() == "knock over glass" or action.lower() == "knock glass over":
                action = input("Glass is empty!")
                break
            elif action.lower() == "forward" or action.lower() == "go forward":
                action = input("Nothing there. You already took the glass.")
                break
            elif action.lower() == "drop glass" or action.lower() == "drop broken glass" or action.lower() == "drop empty glass":
                inventory.remove("empty glass" or "broken glass")
                print("Inventory:", inventory)
                action = input("Dropped. Now what?")
                break
            else:
                break
        continue
#turn left
    elif action.lower() == "go left" or action.lower() =="look left" or action.lower() == "left" or action.lower() == "turn left":
        action = input("There is a bed in front of you. Lie down or look around?")
        if action.lower() == "look around":
            action = input("There is a bed to your left, a glass of water on the floor in front of you, a locked metal door to your right and a boarded up window behind you. (The room stays orientated this way regardless of what moves you make.) \nLeft, right, forward or back?")
            continue
        elif action.lower() == "move bed" or action.lower() == "move the bed":
            action = input("Moved. There's a trap door with a lock on it and a pen knife.")
            while knife == False:
                if action.lower() == "take knife" or action.lower() == "pick up knife" or action.lower() == "take pen knife" or action.lower() == "pick up pen knife":
                    inventory.append("pen knife")
                    print("Inventory:", inventory)
                    score = score+10
                    print("Score:", score)
                    knife = True
                    action = input("Be careful with that.")
                    continue
            if action.lower() == "unlock trapdoor" or action.lower() == "unlock trap door" or action.lower() == "open trap door" or action.lower() == "open trapdoor":
                while key == False:
                    action = input("Can't do that without a key.")
                    break
            #once knife is taken (knife = True), it can't be taken again
            elif action.lower() == "take knife" or action.lower() == "pick up knife" or action.lower() == "take pen knife" or action.lower() == "pick up pen knife":
                action = input("You're holding it!")
            else:
                continue
        elif action.lower() == "lie down" or action.lower() == "lie" or action.lower() == "rest" or action.lower() == "sleep":
            print("Giving up already? \nYou lose.")
            score = score-100
            print("Score:", score)
            action = input("Just kidding, you get another chance. But your score doesn't.")
            continue
#anything to do with the knife
    while knife == True:
        if action.lower() == "drop knife":
            inventory.remove("pen knife")
            print("Inventory:", inventory)
            knife = False
            score = score - 10
            print("Score:", score)
            action = input("Knife dropped (back in its inital place)")
        elif action.lower() == "take knife" or action.lower() == "pick up knife" or action.lower() == "take pen knife" or action.lower() == "pick up pen knife":
            action = input("You're holding it!")
        elif action.lower() == "cut door" or action.lower() == "cut the main door" or action.lower() == "cut main door":
            action = input("It's metal...")
        elif action.lower() == "use knife on boards" or action.lower() == "cut boarded window" or action.lower() == "cut boards on window" or action.lower() == "use knife on boards on window" or action.lower() == "cut boards":
            action = input("Interesting move... and it worked! \nThere's a key on the window sill. *picks up key* \nUse on door or trapdoor?")
            inventory.append("key")
            print("Inventory:", inventory)
            score = score+10
            print("Score:", score)
            key = True
            continue
        elif action.lower() == "use knife":
            action = input("On what?")
            while trapdoor == False:
                if action.lower() == "trap door" or action.lower() == "trapdoor":
                    action = input("Interesting move... but it didn't work.")
                    continue
                elif action.lower() == "door" or action.lower() == "the door":
                    action = input("It's metal...")
                elif action.lower() == "the boards on the window" or action.lower() == "boards on window":
                    action = input("Interesting move... and it worked! \nThere's a key on the window sill. *picks up key* \nUse on door or trapdoor?")
                    inventory.append("key")
                    print("Inventory:", inventory)
                    score = score+10
                    print("Score:", score)
                    key = True
                    continue
                elif action.lower() == "cut trapdoor" or action.lower == "cut trap door" or action.lower() == "use knife on trap door":
                    action = input("Interesting move... but it didn't work.")
                    continue
                else:
                    pass
            while trapdoor == True:
                if action.lower() == "trap door" or action.lower() == "trapdoor":
                    action = input("Can't do that - it's already open.")
                    continue
                else:
                    pass
#while knife is in the inventory but player doesn't want to use it, ignore this while loop
        else:
            break
#random actions with consequences
    if action.lower() == "die":
        print("You died, loser")
        score = score-1000
        print("Score:", score)
        print("No second chance for you.")
        break
    elif action.lower() == "inventory" or action.lower() == "show inventory" or action.lower() == "view inventory":
        print("Inventory:", inventory)
        action = input("Now what?")
#turn right
    if action.lower() == "go right" or action.lower() == "look right" or action.lower() == "right":
        action = input("There's a door... but it's locked.")
        continue
#turn around
    elif action.lower() == "turn around" or action.lower() =="turn back" or action.lower() =="turn" or action.lower() =="back" or action.lower() == "behind":
        action = input("There's a boarded up window. It's boarded from the inside...")
        while knife == True:
            if action.lower() == "cut boards" or action.lower() == "cut through boards":
                print("Interesting move... and it worked!")
                score = score + 10
                print("Score:", score)
                print("There's a key on the window sill. *picks up key* \nUse on door or trapdoor?")
                inventory.append("key")
                print("Inventory:", inventory)
                key = True
                action = input("")
                break
        else:
            continue
    elif action.lower() == "pick up glass" or action.lower() =="take glass" or action.lower() =="drink glass of water" or action.lower() =="drink water":
        action = input("You'll have to go forward first")
        continue
#while player has the key (which is only compatible with the trapdoor)
    while key == True:
        if action.lower() == "use on door" or action.lower() == "door" or action.lower() == "unlock door" or action.lower() == "open door" or action.lower() == "unlock door with key":
            action = input("Key is not compatible with this door.")
        elif action.lower() == "drop key":
            if key == True:
                print("Dropping key...")
                inventory.remove("key")
                key = False
                print("Inventory:", inventory)
                score = score - 10
                action = input("Dropped key.")
        elif action.lower() == "use on trapdoor" or action.lower() == "use on trap door" or action.lower() == "trapdoor" or action.lower() == "trap door" or action.lower() == "open trapdoor" or action.lower() == "unlock trapdoor" or action.lower() == "unlock trap door":
            trapdoor = True
            score = score + 10
            print("Score:", score)
            action = input("Opened. Go down or look around?")
            if action.lower() == "down" or action.lower() == "go down" or action.lower() == "do downstairs":
                print("You earn points for bravery.")
                score = score + 10
                print("Score:", score)
                action = input("Escape or stay?")
                if action.lower() == "escape":
                    play = False
                    break
                elif action.lower() == "stay":
                    print("You lose.")
                    score = score - 100
                    print("Final score:", score)
                    break
            elif action.lower() == "look around":
                action = input("There is a bed to your left, a glass of water on the floor in front of you, a locked metal door to your right and a boarded up window behind you. (The room stays orientated this way regardless of what moves you make.) \nLeft, right, forward or back?")
                continue
#as I can't cover everything the player might say, here's this:
    else:
        action = input("Instructions unclear. Try again.")
#when play is false, you've won
if play == False:
    score = score+100
    print("You win!")
    print("Final score:", score)