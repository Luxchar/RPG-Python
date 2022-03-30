from random import randrange, uniform
from colorama import Fore, Back, Style

from create import createmap
import movement
import settings 

#difficulty menu ?
#multiple ends with dialogue
#place of power
#handle keypad
#save
#key for door to the boss

def main(): #menu handler
    print("MAIN MENU")
    print("1. Start Game !")
    print("2. Load Game")
    print("3. About")
    print("4. Exit")
    choice = input("Choose an option:\n")
    if choice == "1" or choice =="Start Game" or choice =="start":
        creategame()
    if choice == "3" or choice == "About":
        print("\n")
        print("Hope you enjoyed playing, you can head over to my github to see other projects i made https://github.com/Luxchar\n")
        main()
    if choice == "4":
        quit()
    main()

def creategame():
    print("Good luck ! Remember you can type 'exit' to quit the game :)\n")
    settings.gameinit()
    createmap()
    game()

def game():
    while settings.player.life > 0 or settings.bosss.life > 0: 
        if endgame():
            if settings.bosss.life == 0:
                print(Fore.GREEN, "Nice game, You won !")
            else:
                print(Fore.WHITE, "You lost, Try again ?\n")
            return main()
        #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in settings.map])) # print the map clearly
        printmap()
        print("\n")
        direction = str(input("Type the direction you want to go to (N, S, E, W):\n"))
        exit(direction) 
        err, event,direction = movement.move(direction)
        if err != "":
            continue
        movement.eventhandler(event,settings.player,settings.bosss,settings.Sbire)

def printmap():
    for row in settings.map:
        for item in row:
            if item == "P":
                print(Fore.GREEN, item, end=" ")
            elif item == "B":
                print(Fore.RED, item, end=" ")
            elif item == "S":
                print(Fore.YELLOW, item, end=" ")
            elif item == "E":
                print(Fore.BLUE, item, end=" ")
            elif item == "O":
                print(Fore.CYAN, item, end=" ")
            elif item == "D":
                print(Fore.WHITE, item, end=" ")
            elif item == "X":
                print(Fore.WHITE, item, end=" ")
            else:
                print(Fore.WHITE, item, end=" ")
        print("")

def endgame():
    if settings.player.life <=0 or settings.bosss.life <=0:
        return True
    return False

def exit(input): #gets an input and exit the program if the user wants to
    if input == "exit" or input == "Exit":
        main()

def validinput():
    try:
        action = int(input())
    except ValueError:
        print("Need a number !")
        return validinput()
    return action


if __name__ == "__main__":
    main()