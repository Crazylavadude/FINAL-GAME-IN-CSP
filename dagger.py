class Dagger():
    def __init__(self, game, screen, boss,summoner, x,y):
        self.game = game
        self.screen = screen
        self.boss = boss
        self.x = x
        self.y = y
        self.summoner = summoner
        boss.current_attackers.append(self)
        boss.current_attacks.append(self)
        self.lifespan = 60
    
    def spawn(self):
        if(self.lifespan > 0):
            self.game.draw.rect(self.screen, (255,0,0), (self.x,self.y,50,50))
            self.lifespan -= 1
        else:
            self.despawn()
    def despawn(self):
        self.boss.current_attackers.remove(self)
        self.boss.current_attacks.remove(self)
        self.summoner.dagger = None