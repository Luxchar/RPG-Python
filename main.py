from random import randrange

#difficulty menu ?
#multiple ends with dialogue
#place of power

#you are about to fight a powerful enemy, there is no going back. Proceed ?

class Player:
    def __init__(self, life, attack, defense, objects, level, posy,posx):
        self.life = life #health
        self.attack = attack # *0.5 on all the player attacks 
        self.defense = defense # /0.5 all enemy attacks
        self.objects = objects #user objects
        self.level = level
        self.posy = posy
        self.posx = posx
        
class Sbire:
    def __init__(self, life, attack, defense, level):
        self.life = life
        self.attack = attack
        self.defense = defense
    
class Boss:
    def __init__(self, life, attack, defense):
        self.life = life
        self.attack = attack
        self.defense = defense

class Object:
    def __init__(self, name, attribute, number):
        self.name = name
        self.attribute = attribute #offensive, defensive, heal
        self.number = number

#useful game data 
map = [["X"]*8 for i in range(8)]
playerposy = int(randrange(0,7))
player = Player(20,4,2,[["Epee en bois","offensive",4]],1,int(randrange(0,7)),int(randrange(0,7)))
boss = Boss(50,8,4)
enemies = [] #store all the enemies
objectbank = [] #all the valuable objects in the game 

def main(): #menu handler
    print("NEW GAME")
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

def creategame(): #game loop
    username = str(input("Enter your username:\n"))
    print("Good luck" ,username,"! Remember you can type 'exit' to quit the game :)\n")
    createmap()

    game()

def game():
    while player.life > 0 or boss.life > 0:   
        print(map)
        direction = str(input("type the direction you want to go(N, S, E, W):\n"))
        exit(input) 
        err = move(direction)
        if err != "":
            break

def exit(input): #gets an input and exit the program if the user wants to
    if input == "exit" or input == "Exit":
        main()

def move(direction):
    if direction == "N" or direction == "n" :
        if map[player.posy+1][player.posx]:
            player.posy +=1
            return ""
    if direction == "S" or direction == "s" :
        if map[player.posy-1][player.posx]:
            player.posy -=1
            return ""
    if direction == "E" or direction == "e" :
        if map[player.posy][player.posx+1]:
            player.posx +=1
            return ""
    if direction == "S" or direction == "s" :
        if map[player.posy-1][player.posx]:
            player.posy -=1
            return ""
    return "You cannot go there !"
        

def createmap(): #handles the creation of the map
    for subplace in range(len(map)):
        for place in range(subplace):
            map[subplace][place] = dice()

def dice(): #roll the dice to create the map
    dice = int(randrange(1,10))
    if dice >0 and dice <=4:
        createsbire()
        return "S"
    if dice >5 and dice <=7:
        createobject()
        return "O"
    return "X"

def createsbire(): #creates a sbire
    health = int(randrange(10,20))
    attack = randrange(0.1,0.5)
    defense = randrange(0.1,0.5)
    sbire = Sbire(health, attack, defense)
    enemies.append(sbire)

def createobject(): #creates an object
    name = ""
    type = int(randrange(0,2))
    if type ==0:
        attribute="offensive"
    if type ==1:
        attribute="defensive"
    if type ==2:
        attribute="heal"
    number = int(randrange(2,8))
    object = Object(name, attribute, number)
    objectbank.append(object)

if __name__ == "__main__":
    main()