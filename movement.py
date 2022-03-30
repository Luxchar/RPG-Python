from create import createobject, createsbire
from fight import fightmenu
from colorama import Fore, Back, Style
import settings

def eventhandler(event,player,bosss,Sbire): #handles the event depending on the position he is on
    print(event)
    if event == "X":
        return
    if event == "O":
        player.objects.append(createobject()) 
        print("You got a",player.objects[len(player.objects)-1][0])
        print(player.objects)
    if event == "S":
        print(Fore.RED + "YOU ARE ATTACKED PRESS ANY KEY TO CONTINUE..")
        input()
        return fightmenu(createsbire(Sbire), player)
    if event == "B":
        print(Fore.RED + "YOU FACE A POWERFUL ENEMY PRESS ANY KEY TO CONTINUE..")
        input()
        return fightmenu(bosss, player)
        #return game()

def confirmboss(event):
    if event == "B":
        answer = input("You are about to fight a powerful enemy, there is no going back. Proceed ? (y or n)\n")
        if answer == "" or answer == "y" or answer == "Y" or answer == "yes":
            return ""
        else:
            print("Alright, going back to last movement\n")
            return "err"
    return ""

def move(direction):
    if direction == "W" or direction == "w" :
        if settings.player.posx > 0:
            event = settings.map[settings.player.posy][settings.player.posx-1]
            if confirmboss(event) != "":
                return "","",""
            settings.map[settings.player.posy][settings.player.posx] = "X" #update old pos
            settings.player.posx -=1
            settings.map[settings.player.posy][settings.player.posx] = "P" #update new pos
            return "",event,direction
    if direction == "N" or direction == "n" :
        if settings.player.posy > 0:
            event = settings.map[settings.player.posy-1][settings.player.posx]
            if confirmboss(event) != "":
                return "","",""
            settings.map[settings.player.posy][settings.player.posx] = "X"
            settings.player.posy -=1
            settings.map[settings.player.posy][settings.player.posx] = "P"
            return "",event,direction
    if direction == "E" or direction == "e" :
        if settings.player.posx < 7:
            event = settings.map[settings.player.posy][settings.player.posx+1]
            if confirmboss(event) != "":
                return "","",""
            settings.map[settings.player.posy][settings.player.posx] = "X"
            settings.player.posx +=1
            settings.map[settings.player.posy][settings.player.posx] = "P"
            return "",event,direction
    if direction == "S" or direction == "s" :
        if settings.player.posy < 7:
            event = settings.map[settings.player.posy+1][settings.player.posx]
            if confirmboss(event) != "":
                return "","",""
            settings.map[settings.player.posy][settings.player.posx] = "X"
            settings.player.posy +=1
            settings.map[settings.player.posy][settings.player.posx] = "P"
            return "",event,direction
    return "error wrong key or cant access the direction","",""
        