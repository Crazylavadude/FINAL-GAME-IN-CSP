
from dagger import Dagger
class Summon_dagger():
    def __init__(self, Game, screen, boss,attack3, x, y):
        self.Game = Game
        self.screen =screen
        self.boss = boss
        self.attack3 = attack3
        self.x = x
        self.y = y
        self.image = self.Game.image.load("Summon-dagger.png").convert_alpha()
        boss.current_attackers.append(self)
        boss.current_attacks.append(self)
        self.stun = 0
        self.dagger = None

    def spawn(self):
        if(abs(self.x - self.boss.player.get_x()) > 30 and self.stun == 0):
            if(self.x < self.boss.player.get_x()):
                self.x += 2
            elif(self.x > self.boss.player.get_x()):
                self.x -= 2
        if(abs(self.y - self.boss.player.get_y())> 30 and self.stun == 0):
            if(self.y < self.boss.player.get_y()):
                self.y += 2
            elif(self.y > self.boss.player.get_y()):
                self.y -= 2
        if(abs(self.y - self.boss.player.get_y()) < 30 and abs(self.x - self.boss.player.get_x()) < 30 and self.stun == 0):
            self.attack()
            self.stun = 5*60
        if(self.stun > 0):
            self.stun -= 1
        self.screen.blit(self.image,(self.x-12.5,self.y-25))
    def attack(self):
        self.dagger = Dagger(self.Game, self.screen, self.boss,self, self.x, self.y)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def despawn(self):
        self.boss.current_attackers.remove(self)
        self.boss.current_attacks.remove(self)
        if(self.dagger != None):
            self.dagger.despawn()
        self.attack3.summon_count -= 1