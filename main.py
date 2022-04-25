from random import randrange, uniform
from colorama import Fore, Back, Style

from create import createmap, loadgame, savegame
import movement
import settings 

def main(): #menu handler
    print("MAIN MENU")
    print("1. Start Game !")
    print("2. Load Game")
    print("3. About")
    print("4. Exit")
    choice = input("Choose an option:\n")
    if choice == "1" or choice =="Start Game" or choice =="start":
        creategame()
    if choice == "2":
        loadgame()
        game()
    if choice == "3" or choice == "About":
        print("\n")
        print(f"Hope you enjoyed playing, you can head over to my github to see other projects i made {Fore.BLUE}https://github.com/Luxchar{Fore.WHITE}\n")
        main()
    if choice == "4":
        quit()
    main()

def creategame():
    print(f"Good luck ! Remember you can type {Fore.GREEN}'save'{Fore.WHITE} to save the game and {Fore.RED}'exit'{Fore.WHITE} to quit the game :)\n")
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
        printmap()
        print("\n")
        direction = str(input(f"Type the direction you want to go to ({Fore.GREEN}N{Fore.WHITE}(orth), {Fore.RED}S{Fore.WHITE}(outh), {Fore.YELLOW}E{Fore.WHITE}(ast), {Fore.BLUE}W{Fore.WHITE}(est)):\n"))
        exit(direction)
        print(direction)
        if direction == "save":
            savegame()
            break
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
        print(Fore.WHITE+"")

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