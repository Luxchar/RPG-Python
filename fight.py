from colorama import Fore, Back, Style
from main import game, validinput

def fightmenu(enemy, player):
    while player.life > 0 and enemy.life > 0:
        print("You have",player.life," HP. You face the enemy with",enemy.life, "HP")
        print("What do you do ?")
        print("1. Attack")
        print("2. Object")
        action = str(input())
        if action == "1":
            attackmenu(enemy, player)
            
        if action == "2":
            print("1. Heal")
            print("2. Defensive")
            action = str(input())
            print("Choose an object to attack with:")
            if action == "1":
                healmenu(enemy, player)
            if action == "2":
                defensemenu(enemy, player)
        player.life -= enemy.attack #enemy response

    if player.life > 0:
        print(Fore.WHITE, "You won !")
        result = player.winfight(enemy.level) #update level
        print(str(result))
    return game()

def attackmenu(enemy, player):
    print("Choose an object to attack with:")
    for i in range(len(player.objects)): #fetch user objects
        if player.objects[i][1] == "offensive":
            print(i,": ",player.objects[i])
    print(len(player.objects),": Go back")
    action = validinput()
    print("\n")
    while int(action) <0 or int(action) >= len(player.objects)+1: #valid choice of object ???
        print("Choose an object to attack with:")
        for i in range(len(player.objects)): #fetch user objects
            if player.objects[i][1] == "offensive":
                print(i,": ",player.objects[i])
        print(len(player.objects),": Go back")
        action = validinput()

    if action == len(player.objects):
        return fightmenu(enemy, player)
    while player.objects[action][1] != "offensive": #valid choice of weapon
        action = int(input())
    enemy.life -= player.objects[action][2] #damage dealt
    player.objects[action][3] -= 1 #durability update

def healmenu(enemy, player): #attack menu in fight
    for i in range(len(player.objects)): #fetch user objects
        if player.objects[i][1] == "heal":
            print(i,": ",player.objects[i])
    print(len(player.objects),": Go back")
    action = validinput()
    print("\n")
    while action <=0 or action >= len(player.objects)+1: #valid choice of object ???
        print("Choose an object to heal with:")
        for i in range(len(player.objects)): #fetch user objects
            if player.objects[i][1] == "heal":
                print(i,": ",player.objects[i])
        print(len(player.objects),": Go back")
        action = validinput()

    if action == len(player.objects):
        return fightmenu(enemy, player)
    while player.objects[action][1] != "heal": #valid choice of object
        action = int(input())

    player.life += player.objects[action][2] #heal
    player.objects[action].remove()

def defensemenu(enemy, player): #defense and health menu in fight
    for i in range(len(player.objects)): #fetch user objects
        if player.objects[i][1] == "defensive":
            print(i,": ",player.objects[i])
    print(len(player.objects),": Go back")
    action = validinput()
    print("\n")
    while action <=0 or action >= len(player.objects)+1: #valid choice of object ???
        print("Choose an object to defend with:")
        for i in range(len(player.objects)): #fetch user objects
            if player.objects[i][1] == "defensive":
                print(i,": ",player.objects[i])
        print(len(player.objects),": Go back")
        action = validinput()
    
    if action == len(player.objects):
        return fightmenu(enemy, player)
    while player.objects[action][1] != "defensive": #valid choice of object
        action = int(input())

    enemy.attack /= player.objects[action][2]/10 #defense applied to enemy attack
    player.objects[action].remove()
