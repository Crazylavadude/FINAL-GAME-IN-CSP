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
        self.fireball_1 = True

    def spawn(self):
        self.count = self.count + 1
        if(self.count % 5 == 0):
            if(self.fireball_1):
                self.fireball_1 = False
            else:
                self.fireball_1 = True
        if(self.direction == "yl"):
            self.x += 5
            if(self.x > self.screen.get_width()):
                self.despawn()
            self.draw_horizontal_left()
        elif(self.direction == "yr"):
            self.x -= 5
            if(self.x < 0):
                self.despawn()
            self.draw_horizontal_right()
        elif(self.direction == "xt"):
            self.y += 5
            if(self.y > self.screen.get_height()):
                self.despawn()
            self.draw_vertical_down()
        elif(self.direction == "xd"):
            self.y -= 5
            if(self.y < 0):
                self.despawn()
            self.draw_vertical_top()

    def draw_vertical_down(self):
        if(self.fireball_1):
            self.screen.blit(self.image[0],(self.get_x()-15, self.get_y()-25))
        else:
            self.screen.blit(self.image[1],(self.get_x()-15, self.get_y()-25))
    def draw_vertical_top(self):
        if(self.fireball_1):
            rotated_image = self.game.transform.rotate(self.image[0], 180)
            self.screen.blit(rotated_image,(self.get_x()-20, self.get_y()-15))
        else:
            rotated_image = self.game.transform.rotate(self.image[1], 180)
            self.screen.blit(rotated_image,(self.get_x()-20, self.get_y()-15))
    def draw_horizontal_right(self):
        if(self.fireball_1):
            rotated_image = self.game.transform.rotate(self.image[0], 275)
            self.screen.blit(rotated_image,(self.get_x()-20, self.get_y()-15))
        else:
            rotated_image = self.game.transform.rotate(self.image[1], 275)
            self.screen.blit(rotated_image,(self.get_x() - 20, self.get_y()-15))
    def draw_horizontal_left(self):
        if(self.fireball_1):
            rotated_image = self.game.transform.rotate(self.image[0], 90)
            self.screen.blit(rotated_image,(self.get_x()-20, self.get_y()-15))
        else:
            rotated_image = self.game.transform.rotate(self.image[1], 90)
            self.screen.blit(rotated_image,(self.get_x() - 20, self.get_y()-15))
    def despawn(self):
        self.boss.current_attackers.remove(self)
        self.boss.current_attacks.remove(self)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y