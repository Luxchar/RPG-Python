from random import randrange, uniform

import settings

def createmap(): #handles the creation of the map
    for subplace in range(len(settings.map)):
        for place in range(len(settings.map)):
            settings.map[subplace][place] = dice()
    settings.map[settings.player.posy][settings.player.posx] = "P"
    settings.map[settings.bosss.posy][settings.bosss.posx] = "B"

def dice(): #roll the dice to create the map
    dice = int(randrange(1,10))
    if dice >0 and dice <=4:
        return "S"
    if dice >5 and dice <=7:
        return "O"
    return "X"

def createsbire(Sbire): #creates a sbire
    health = int(randrange(10,20))
    attack = int(randrange(2,4))
    defense = uniform(0.1,0.5)
    sbire = Sbire(health, attack, defense,1)
    return sbire

def createobject(): #creates an object
    object = []
    type = int(randrange(0,3))
    rand = int(randrange(0,3))
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

def savegame():
    save = open("save.txt","w")
    save.write(str(settings.player.life)+"\n")
    save.write(str(settings.player.attack)+"\n")
    save.write(str(settings.player.defense)+"\n")
    save.write(str(settings.player.objects)+"\n")
    save.write(str(settings.player.level)+"\n")
    save.write(str(settings.player.xp)+"\n")
    save.write(str(settings.player.posy)+"\n")
    save.write(str(settings.player.posx)+"\n")
    save.write(str(settings.bosss.life)+"\n")
    save.write(str(settings.bosss.attack)+"\n")
    save.write(str(settings.bosss.defense)+"\n")
    save.write(str(settings.bosss.posy)+"\n")
    save.write(str(settings.bosss.posx)+"\n")
    save.write(str(settings.map)+"\n")
    save.close()

def loadgame():
    save = open("save.txt","r")
    settings.player.life = int(save.readline())
    settings.player.attack = int(save.readline())
    settings.player.defense = float(save.readline())
    settings.player.objects = eval(save.readline())
    settings.player.level = int(save.readline())
    settings.player.xp = int(save.readline())
    settings.player.posy = int(save.readline())
    settings.player.posx = int(save.readline())
    settings.bosss.life = int(save.readline())
    settings.bosss.attack = int(save.readline())
    settings.bosss.defense = float(save.readline())
    settings.bosss.posy = int(save.readline())
    settings.bosss.posx = int(save.readline())
    settings.map = eval(save.readline())
    save.close()
    
