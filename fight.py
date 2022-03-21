
from main import *

def fight(enemy):
    print(Fore.RED + "YOU FACE A POWERFUL ENEMY TYPE ANY KEY TO CONTINUE..")
    input()
    while player.life > 0 and enemy.life > 0:
        print("You have",player.life," HP. You face the enemy with",enemy.life, "HP")
        print("What do you do ?")
        print("1. Attack")
        print("2. Object")
        action = str(input())
        if action == "1":
            print("Choose an object to attack with:")
            for i in range(len(player.objects)): #fetch user objects
                if player.objects[i][1] == "offensive":
                    print(i,": ",player.objects[i])
            action = int(input())
            print("\n")
            while player.objects[action][1] != "offensive": #valid choice of weapon
                action = int(input())
            enemy.life -= player.objects[action][2] #damage dealt
            player.objects[action][3] -= 1 #durability update
            
            player.life -= enemy.attack #enemy response
        if action == "2":
            print("1. Heal")
            print("2. Defensive")
            action = str(input())
            print("Choose an object to attack with:")
            if action == "1":
                attackmenu()
            if action == "2":
                midstmenu(enemy)

    if player.life > 0:
        print(Fore.WHITE, "You won !")
        result = player.winfight(enemy.level) #update level
        print(str(result))

def attackmenu(): #attack menu in fight
    for i in range(len(player.objects)): #fetch user objects
        if player.objects[i][1] == "heal":
            print(i,": ",player.objects[i])
    action = int(input())
    print("\n")
    while player.objects[action][1] != "heal": #valid choice of object
        action = int(input())

    player.life += player.objects[action][2] #heal
    player.objects[action].remove()

def midstmenu(enemy): #defense and health menu in fight
    for i in range(len(player.objects)): #fetch user objects
        if player.objects[i][1] == "defensive":
            print(i,": ",player.objects[i])
    action = int(input())
    print("\n")
    while player.objects[action][1] != "defensive": #valid choice of object
        action = int(input())

    enemy.attack /= player.objects[action][2]/10 #defense applied to enemy attack
    player.objects[action].remove()

def exit(input): #gets an input and exit the program if the user wants to
    if input == "exit" or input == "Exit":
        main()
