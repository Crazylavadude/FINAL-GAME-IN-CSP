class Fireball():
    def __init__(self,game,screen,  direction, x, y, boss):
        self.game = game
        self.screen = screen
        self.direction = direction
        self.x = x
        self.y = y
        self.boss = boss
        self.image = [game.image.load("fireball.png").convert_alpha(),game.image.load("fireball2.png").convert_alpha()]
        self.count = 0

    def spawn(self):
        if(self.direction == "yl"):
            self.x += 5
            if(self.x > 1280):
                self.despawn()
        elif(self.direction == "yr"):
            self.x -= 5
            if(self.x < 0):
                self.despawn()
        elif(self.direction == "xt"):
            self.y += 5
            if(self.y > 720):
                self.despawn()
        elif(self.direction == "xd"):
            self.y -= 5
            if(self.y < 0):
                self.despawn()
        if(self.count % 5 == 0):
            self.screen.blit(self.image[0],(self.get_x() -40, self.get_y() -40))
        else:
            self.screen.blit(self.image[1],(self.get_x() -40, self.get_y() -40))
        self.game.draw.rect(self.screen,(255,0,0), (self.x, self.y,50,50))

    def despawn(self):
        self.boss.current_attackers.remove(self)
        self.boss.current_attacks.remove(self)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y