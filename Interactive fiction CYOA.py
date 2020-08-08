# global variables to keep track of what's happened in our game so far
money = 0
money_found = False
mace_bought = False

# the dorm room--where we start the journey
def dorm():
    # define all variables that we might need to change as global
    global money
    global money_found
    
    while True:
        print ()
        print ("You are currently in your dorm.")
        print ("There is a huge pile of laundry beside your bed.")
        print ("Both the subway and the library are a five minute walk away.")
        choice = input("What would you like to do? ")
        if choice == "laundry":
            return laundry
        # they want to go south
        elif choice == "subway":
            # send a reference to the 'store' function back
            return subway

        # they want to go east
        elif choice == "library":
            # send a reference to the 'cave' function back
            return library

        # command not understood
        else:
            print ("I don't understand that")


# the laundry
def laundry():
    global money
    global money_found
    
    while True:
        print ()
        print ("You trudge downstairs with your laundry.")
        print ("It has to be done at some point right?")
        print("Usually you check your laundry, but you're debating on just tossing it in there for time's sake.")
        print("Do you end up checking your laundry? Or do you dump it inside and head to one of the following places:")
        if money_found==False:
            print("Library or Subway")
        else:
            print("Library, Subway, or Store")
        # did they already buy the sword?
        choice = input("What would you like to do? ")


        if choice == "check":
             # is this the first time they've looked here?
            if money_found == False:
                print ("There is $15 here! Maybe you can spend it on something cool?")

                # give them the money and make sure they can't get it again!
                money_found = True
                money += 15
            # otherwise there is nothing here
            else:
                print ("Nothing here")

        elif choice =="store":
            return store
        elif choice=="subway":
            return subway
        elif choice=="library":
            return library
                    
        # command not understood
        else:
            print ("I don't understand that")


# the subway station
def subway():
    global money
    global money_found
    while True:
        print()
        #if they found the money and bought nothing
        if money_found==True and money==15:
            print("On the way to the subway station you get mugged! You have now lost your $15.")
            print("You only have a subway card with enough money for a single subway trip and 15% battery on your phone")
            print("However, you've always wanted to visit Central Park...")
            choice=input("Should you go to Central Park? or stay back and go to the library instead?")
            money-=15
            if choice == "central park" or choice == "park":
                return park
            elif choice == "library":
                return library
            else:
                print ("I don't understand that")
        #if they have mace
        elif mace_bought==True:
            print("You almost got mugged! But luckily you had your mace with you.")
            print("You have enough money to go to Central Park and back!")
            print("Or you can go to the library and study")
            choice=input("Should you go to Central Park? or stay back and go to the library instead?")
            if choice == "central park" or choice == "park":
                return park
            elif choice == "library":
                return library
            else:
                print ("I don't understand that")
        #if they have nothing
        else:
            print("On the way to the subway station you realize you have a subway card with enough money for a single subway")
            print("Your phone also only has 15% battery")
            print("However, you've always wanted to visit Central Park...")
            choice=input("Should you go to Central Park, do your laundry, or go to the library instead?")
            if choice == "central park" or choice == "park":
                return park
            elif choice == "laundry":
                return laundry
            elif choice == "library":
                return library
            else:
                print ("I don't understand that")
#the store
def store():
    global money
    global mace_bought
    while True:
        print()
        print("At the store there's a bunch of cool things!")
        print("They have mace or candy to buy.")
        print("You can also choose to save money and buy nothing.")
        print("You can leave the store and go to the library or subway station as well.")
        choice=input("What do you want to do? ")
        if money == 15:
            if choice == "mace":
                mace_bought=True
                money-=10
                print("A good choice. Safety is always important.")
            # if they fight they can win, but only if they have the sword
            elif choice == "candy":
                print("You spent $15 on candy and ate it! It was worth it.")
                money-=15
            elif choice == "nothing" or choice=="save":
                print("You have bought nothing")
            elif choice=="library":
                return library
            elif choice=="subway":
                return subway
            else:
                print ("I don't understand that")
        else:
            if choice == "mace":
                print("You don't have enough money")
            # if they fight they can win, but only if they have the sword
            elif choice == "candy":
                print("You don't have enough money")
            elif choice == "nothing" or choice=="save":
                print("You have bought nothing")
            elif choice=="library":
                return library
            elif choice=="subway":
                return subway


#park
def park():
    global money
    while True:
        print()
        if money == 5:
            print("You're at Central Park! Safely equipped with your mace you're ready to take on the world.")
            print("You go exploring for a bit until you take a subway back. It's already 9 PM...")
            print("Should you go to the library or get some rest?")
            choice=input("What do you want to do? ")
            if choice =="rest":
                print("You get a good night's rest! Going to Central Park was worth it.")
                print("Especially compared to what you heard happen at the library last night.")
                return "The end"
            elif choice =="library":
                return library
            else:
                print ("I don't understand that")
        else:
            print("You're at Central Park and it's absolutely beautiful.")
            print("You go exploring for a bit.")
            print("Eventually you take your phone out to take a picture until you realize it's completely dead.")
            print("Instead of calling an Uber or a Lyft back, you now have to walk 80 blocks back to Washington Square.")
            print("Have fun!")
            return "The end"
    
#the library           
def library():
    global mace_bought
    while True:
        print()
        print("You enter the library and it's... oddly silent?")
        print("The lights are flickering but the security guard says it's fine, only construction.")
        print("You make your way towards your usual study spot in LL2 until you hear a noise.")
        choice=input("Do you investigate or call security? ")
        if choice =="investigate":
            if mace_bought==True:
                print("Armed with your mace, you slowly make your way forward.")
                print("Suddenly, some one grabs you")
                print("But you spray them with the mace and run upstairs to bring a security guard.")
                print("You're alive! And you took down a security threat. Good job.")
                return "The end"
            else:
                print("A person suddenly grabs you by the wrist and now you're dead.")
                print("Maybe you should have left after the flickering lights...")
                return "The end"
        elif choice=="call" or choice =="security" or choice=="call security guard":
            print("You inform the security guard and she calls for backup")
            print("The library is evacuated and the noise is investigated.")
            print("You go back home and get some well deserved rest after the long day.")
            return "The end"
        else:
            print ("I don't understand that")
            
# start off the game by defining the 'dorm' function as the first room
current_room = dorm

# enter into an infinte loop
while True:

    # execute the 'current_room' function (which is initially set to 'dorm')
    # capture the return value
    next_action_to_take = current_room()

    # if the function returns the string 'end' we should end the program
    if next_action_to_take == 'The end':
        print("The end")
        break

    # the function didn't return the string 'end', so we must be moving into
    # a different room
    else:
        # set the current_room based on the next_action_to_take
        current_room = next_action_to_take
