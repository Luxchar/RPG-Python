from random import randrange, uniform

class Player:
    def __init__(self, life, attack, defense, objects, level, xp, posy, posx):
        self.life = life #health
        self.lifecap = life #max health
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
            self.lifecap+=5
            self.attack+=1
            self.defense+=1
            self.life = self.lifecap
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

map = [["X"]*8 for i in range(8)]
playerposy = int(randrange(0,7))
player = Player(20,4,2,[["Punch","offensive",4,999],["Wooden Sword","offensive",5,20]],1,1,int(randrange(0,7)),int(randrange(0,7)))
bosss = Boss(50,8,4,int(randrange(0,7)),int(randrange(0,7)))

def gameinit():
    map = [["X"]*8 for i in range(8)]
    playerposy = int(randrange(0,7))
    player = Player(20,4,2,[["Punch","offensive",4,999],["Wooden Sword","offensive",5,20]],1,1,int(randrange(0,7)),int(randrange(0,7)))
    bosss = Boss(50,8,4,int(randrange(0,7)),int(randrange(0,7)))