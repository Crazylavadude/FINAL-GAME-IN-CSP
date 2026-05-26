from mage_fireball import Mage_fireball
import random
class Summon_wizard():
    def __init__(self, Game, screen, boss,x,y):
        self.Game = Game
        self.screen =screen
        self.boss = boss
        self.x = x
        self.y = y
        boss.current_attackers.append(self)
        boss.current_attacks.append(self)
        self.cooldown = 5 * 60
        self.image = self.Game.image.load("Summon-staff.png").convert_alpha()
        self.my_fireballs = []
        self.dontmove = 0
        self.goal = None

    def spawn(self):
        self.screen.blit(self.image,(self.x-12.5,self.y-25))
        if(self.cooldown == 0):
            self.dontmove = 360
            self.my_fireballs.append(Mage_fireball(self.Game,self.screen,self.boss,self.x,self.y))
            self.cooldown = 15*60
        elif(self.cooldown > 0):
            self.cooldown -= 1
        if(self.dontmove == 0):
            if(self.goal == None):
                random_x = random.randint(50,1570)
                random_y = random.randint(400,800)
                self.goal = (random_x, random_y)
            elif(self.x == self.goal[0] and self.y == self.goal[1]):
                self.goal = None
                random_x = random.randint(50,1570)
                random_y = random.randint(400,800)
                self.goal = (random_x, random_y)
            else:
                self.x = self.goal[0]
                self.y = self.goal[1]
                self.dontmove = 360
        else:
            self.dontmove -= 1

    def despawn(self):
        self.boss.current_attackers.remove(self)
        self.boss.current_attacks.remove(self)
        for object in self.my_fireballs:
            object.despawn()

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y