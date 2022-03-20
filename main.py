from random import randrange, uniform
from colorama import Fore, Back, Style
from numpy import diff

#difficulty menu ?
#multiple ends with dialogue
#place of power
#handle keypad

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
        if self.level*10 <= self.xp: #raise level
            difference = self.level*10-self.xp
            self.level +=1
            self.xp = 0
            self.life+=5
            self.attack+=1
            self.defense+=1

        self.xp *= coefficient/10
        if difference:
            self.xp += difference
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

class Object:
    def __init__(self, name, attribute, number, durability):
        self.name = name
        self.attribute = attribute #offensive, defensive, heal
        self.number = number
        self.durability = durability

#useful game data 
map = [["X"]*8 for i in range(8)]
playerposy = int(randrange(0,7))
player = Player(20,4,2,[["Punch","offensive",4,999],["Epee en bois","offensive",6,20]],1,0,int(randrange(0,7)),int(randrange(0,7)))
boss = Boss(50,8,4,int(randrange(0,7)),int(randrange(0,7)))

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
        print("Hope you enjoyed playing, you can head to my github to see other projects i made https://github.com/Luxchar")
        main()
    if choice == "4":
        exit()
    main()

def creategame():
    username = str(input("Enter your username:\n"))
    print("Good luck" ,username,"! Remember you can type 'exit' to quit the game :)\n")
    createmap()
    game()

def game():
    while player.life > 0 or boss.life > 0:   
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in map])) # print the map clearly
        print("\n")
        direction = str(input("Type the direction you want to go to (N, S, E, W):\n"))
        exit(input) 
        err, event,direction = move(direction)
        if err != "":
            continue
        eventhandler(event,direction)
    print("You lost, Try again ?\n")

def eventhandler(event,direction): #handles the event depending on the position he is on
    print(event)
    if event == "X":
        return
    if event == "S":
        return fightsbire()
    if event == "B":
        return game()

def confirmboss(event):
    if event == "B":
        answer = input("You are about to fight a powerful enemy, there is no going back. Proceed ? (y or n)\n")
        if answer == "" or answer == "y" or answer == "Y" or answer == "yes":
            return ""
        else:
            print("Alright, going back to last movement\n")
            return "err"
    return ""

def fightboss():
    print("t")

def fightsbire():
    print(Fore.RED + "YOU ARE ATTACKED PRESS ANY KEY TO START THE FIGHT..")
    sbire = createsbire()
    _ = input()
    while player.life > 0 or sbire.life > 0:
        print("You have",player.life," health. You face a sbire with",sbire.life, "HP")
        print("What do you do ?")
        print("1. Attack")
        print("2. Heal")
        action = str(input())
        if action == "1" or action == "Attack":
            print("Choose an object to attack with:")
            count = 0
            for i in range(len(player.objects)): #fetch user objects
                if player.objects[i][1] == "offensive":
                    count+=1
                    print(i,": ",player.objects[i],"\n")
            action = int(input())
            while player.objects[action][1] != "offensive": #valid choice of weapon
                action = int(input())
            sbire.life -= player.objects[action][2] #damage dealt
            player.objects[action][3] -= 1 #durability update
            
            player.life -= sbire.attack #sbire response

    print(Fore.WHITE + "You won ! you earned x amount of experience")

def exit(input): #gets an input and exit the program if the user wants to
    if input == "exit" or input == "Exit":
        main()

def move(direction):
    if direction == "W" or direction == "w" :
        if player.posx > 0:
            event = map[player.posy][player.posx-1]
            if confirmboss(event) != "":
                return 
            map[player.posy][player.posx] = "X" #update old pos
            player.posx -=1
            map[player.posy][player.posx] = "P" #update new pos
            return "",event,direction
    if direction == "N" or direction == "n" :
        if player.posy > 0:
            event = map[player.posy-1][player.posx]
            if confirmboss(event) != "":
                return
            map[player.posy][player.posx] = "X"
            player.posy -=1
            map[player.posy][player.posx] = "P"
            return "",event,direction
    if direction == "E" or direction == "e" :
        if player.posx < 7:
            event = map[player.posy][player.posx+1]
            if confirmboss(event) != "":
                return
            map[player.posy][player.posx] = "X"
            player.posx +=1
            map[player.posy][player.posx] = "P"
            return "",event,direction
    if direction == "S" or direction == "s" :
        if player.posy < 7:
            event = map[player.posy+1][player.posx]
            if confirmboss(event) != "":
                return
            map[player.posy][player.posx] = "X"
            player.posy +=1
            map[player.posy][player.posx] = "P"
            return "",event,direction
    return "error wrong key or cant access the direction","",""
        

def createmap(): #handles the creation of the map
    for subplace in range(len(map)):
        for place in range(len(map)):
            map[subplace][place] = dice()
    map[player.posy][player.posx] = "P"
    map[boss.posy][boss.posx] = "B"

def dice(): #roll the dice to create the map
    dice = int(randrange(1,10))
    if dice >0 and dice <=4:
        return "S"
    if dice >5 and dice <=7:
        return "O"
    return "X"

def createsbire(): #creates a sbire
    health = int(randrange(10,20))
    attack = uniform(2,4)
    defense = uniform(0.1,0.5)
    sbire = Sbire(health, attack, defense,1)
    return sbire

def createobject(): #creates an object
    type = int(randrange(0,2))
    if type ==0:
        rand = int(randrange(1,10))
        itemsname = ["Silver Sword", "Ray Gun", "Katana", ""]
        name = itemsname[rand]
        itemsname.pop(rand)
        attribute="offensive"
    if type ==1:
        attribute="defensive"
    if type ==2:
        attribute="heal"
    number = int(randrange(2,8))
    object = Object(name, attribute, number, 10)
    return object

if __name__ == "__main__":
    main()