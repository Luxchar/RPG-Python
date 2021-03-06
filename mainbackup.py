from random import randrange, uniform
from colorama import Fore, Back, Style
#difficulty menu ?
#multiple ends with dialogue
#place of power
#handle keypad
#save
#key for door to the boss

#handle the defense and attack parameters
class Player:
    def __init__(self, life, attack, defense, objects, level, xp, posy, posx):
        self.life = life #health
        self.attack = attack # *0.5 on all the player attacks 
        self.defense = defense # /0.5 all enemy attacks
        self.objects = objects #user objects
        self.level = level
        self.xp = xp
        self.posy = posy
        self.posx = posx

    def winfight(self, coefficient):
        self.xp += coefficient*10
        if self.level*10 <= self.xp: #raise level
            self.level +=1
            self.xp = 1
            self.life+=5
            self.attack+=1
            self.defense+=1
            return "Level up ! You are now level",self.level

        return int(self.level*10-self.xp),"XP left before next level up"
class Sbire:
    def __init__(self, life, attack, defense, level):
        self.life = life
        self.attack = attack
        self.defense = defense
        self.level = level
    
class Boss:
    def __init__(self, life, attack, defense, posy, posx):
        self.life = life
        self.attack = attack
        self.defense = defense
        self.posy = posy
        self.posx = posx

#useful game data 
map = [["X"]*8 for i in range(8)]
playerposy = int(randrange(0,7))
player = Player(20,4,2,[["Punch","offensive",4,999],["Wooden Sword","offensive",10,20]],1,1,int(randrange(0,7)),int(randrange(0,7)))
bosss = Boss(50,8,4,int(randrange(0,7)),int(randrange(0,7)))

def gameinit():
    map = [["X"]*8 for i in range(8)]
    playerposy = int(randrange(0,7))
    player = Player(20,4,2,[["Punch","offensive",4,999],["Wooden Sword","offensive",10,20]],1,1,int(randrange(0,7)),int(randrange(0,7)))
    bosss = Boss(50,8,4,int(randrange(0,7)),int(randrange(0,7)))

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
        print("Hope you enjoyed playing, you can head to my github to see other projects i made https://github.com/Luxchar\n")
        main()
    if choice == "4":
        quit()
    main()

def creategame():
    print("Good luck ! Remember you can type 'exit' to quit the game :)\n")
    gameinit()
    createmap()
    game()

def game():
    while player.life > 0 or bosss.life > 0: 
        if endgame():
            if bosss.life == 0:
                print(Fore.GREEN, "Nice game, You won !")
            else:
                print(Fore.WHITE, "You lost, Try again ?\n")
            return main()
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in map])) # print the map clearly
        print("\n")
        direction = str(input("Type the direction you want to go to (N, S, E, W):\n"))
        exit(direction) 
        err, event,direction = move(direction)
        if err != "":
            continue
        eventhandler(event)

def endgame():
    if player.life <=0 or bosss.life <=0:
        return True
    return False

def eventhandler(event): #handles the event depending on the position he is on
    print(event)
    if event == "_":
        return
    if event == "O":
        player.objects.append(createobject()) 
        print("You got a",player.objects[len(player.objects)-1][0])
        print(player.objects)
    if event == "S":
        print(Fore.RED + "YOU ARE ATTACKED PRESS ANY KEY TO CONTINUE..")
        input()
        return fight(createsbire())
    if event == "B":
        print(Fore.RED + "YOU FACE A POWERFUL ENEMY PRESS ANY KEY TO CONTINUE..")
        input()
        return fight(bosss)
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
        if player.posx > 0:
            event = map[player.posy][player.posx-1]
            if confirmboss(event) != "":
                return "","",""
            map[player.posy][player.posx] = "_" #update old pos
            player.posx -=1
            map[player.posy][player.posx] = "P" #update new pos
            return "",event,direction
    if direction == "N" or direction == "n" :
        if player.posy > 0:
            event = map[player.posy-1][player.posx]
            if confirmboss(event) != "":
                return "","",""
            map[player.posy][player.posx] = "_"
            player.posy -=1
            map[player.posy][player.posx] = "P"
            return "",event,direction
    if direction == "E" or direction == "e" :
        if player.posx < 7:
            event = map[player.posy][player.posx+1]
            if confirmboss(event) != "":
                return "","",""
            map[player.posy][player.posx] = "_"
            player.posx +=1
            map[player.posy][player.posx] = "P"
            return "",event,direction
    if direction == "S" or direction == "s" :
        if player.posy < 7:
            event = map[player.posy+1][player.posx]
            if confirmboss(event) != "":
                return "","",""
            map[player.posy][player.posx] = "_"
            player.posy +=1
            map[player.posy][player.posx] = "P"
            return "",event,direction
    return "error wrong key or cant access the direction","",""
        

def createmap(): #handles the creation of the map
    for subplace in range(len(map)):
        for place in range(len(map)):
            map[subplace][place] = dice()
    map[player.posy][player.posx] = "P"
    map[bosss.posy][bosss.posx] = "B"

def dice(): #roll the dice to create the map
    dice = int(randrange(1,10))
    if dice >0 and dice <=4:
        return "S"
    if dice >5 and dice <=7:
        return "O"
    return "_"

def createsbire(): #creates a sbire
    health = int(randrange(10,20))
    attack = int(randrange(2,4))
    defense = uniform(0.1,0.5)
    sbire = Sbire(health, attack, defense,1)
    return sbire

def createobject(): #creates an object
    object = []
    type = int(randrange(0,2))
    rand = int(randrange(0,2))
    if type == 0:
        itemsname = ["Silver Sword", "Ray Gun", "Katana"]
        object.append(itemsname[rand]) #name
        itemsname.pop(rand)
        object.append("offensive")
    if type == 1:
        itemsname = ["Shield", "Wall", "Bodyguard"]
        object.append(itemsname[rand]) #name
        object.append("defensive")
    if type == 2:
        itemsname = ["Health kit", "Bandage", "Water"]
        object.append(itemsname[rand]) #name
        object.append("heal")
    object.append(int(randrange(2,8)))
    object.append(10)
    return object

def fight(enemy):
    while player.life > 0 and enemy.life > 0:
        print("You have",player.life," HP. You face the enemy with",enemy.life, "HP")
        print("What do you do ?")
        print("1. Attack")
        print("2. Object")
        action = str(input())
        if action == "1":
            attackmenu(enemy)
            
        if action == "2":
            print("1. Heal")
            print("2. Defensive")
            action = str(input())
            print("Choose an object to attack with:")
            if action == "1":
                healmenu(enemy)
            if action == "2":
                defensemenu(enemy)
        player.life -= enemy.attack #enemy response

    if player.life > 0:
        print(Fore.WHITE, "You won !")
        result = player.winfight(enemy.level) #update level
        print(str(result))
    return game()

def attackmenu(enemy):
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
        return fight(enemy)
    while player.objects[action][1] != "offensive": #valid choice of weapon
        action = int(input())
    enemy.life -= player.objects[action][2] #damage dealt
    player.objects[action][3] -= 1 #durability update

def healmenu(enemy): #attack menu in fight
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
        return fight(enemy)
    while player.objects[action][1] != "heal": #valid choice of object
        action = int(input())

    player.life += player.objects[action][2] #heal
    player.objects[action].remove()

def defensemenu(enemy): #defense and health menu in fight
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
        return fight(enemy)
    while player.objects[action][1] != "defensive": #valid choice of object
        action = int(input())

    enemy.attack /= player.objects[action][2]/10 #defense applied to enemy attack
    player.objects[action].remove()

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