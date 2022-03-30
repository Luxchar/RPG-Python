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
