import math
class Dagger():
    def __init__(self, game, screen, boss,summoner, x,y, direction):
        self.game = game
        self.screen = screen
        self.boss = boss
        self.x = x
        self.y = y
        self.y_speed = 0
        self.x_speed = 0
        self.summoner = summoner
        self.direction = direction
        self.set_x_and_y_speed()
        boss.current_attackers.append(self)
        boss.current_attacks.append(self)
        self.image = self.game.image.load("knife.png").convert_alpha()
        self.lifespan = 120
    
    def get_tangent_angle(self):
        x_diff = self.x - self.boss.player.get_x()
        #y_diff = self.y - self.boss.player.get_y()
        if(x_diff != 0):
            if(self.direction < 90):
                return self.direction
            elif(self.direction <180):
                return 180 - self.direction
            elif(self.direction < 270):
                return 180 - self.direction
            elif(self.direction<360):
                return 360 - self.direction
            else:
                return 0
        elif(self.direction == 90):
            return 90
        else:
            return -90
    def set_x_and_y_speed(self):
            angle = self.get_tangent_angle()
            speed = 5
            if(angle == 90):
                self.y_speed = speed
            elif(angle == -90):
                self.y_speed = -speed
            elif(angle == 0):
                if(self.direction == 0):
                    self.x_speed = speed
                else:
                    self.x_speed = -speed
            else:
                if(angle < 0):
                    angle = -angle
                angle = math.radians(angle)
                if(self.direction < 90 ):
                    self.x_speed = speed*math.cos(angle)
                    self.y_speed = -speed*math.sin(angle)
                elif(self.direction < 180 ):
                    self.x_speed -=speed*math.cos(angle)
                    self.y_speed -=speed*math.sin(angle)
                elif(self.direction < 270 ):
                    self.x_speed -=speed*math.cos(angle)
                    self.y_speed +=speed*math.sin(angle)
                elif(self.direction < 360 ):
                    self.x_speed +=speed*math.cos(angle)
                    self.y_speed +=speed*math.sin(angle)


    def spawn(self):
        if(self.lifespan > 0):
            rotated_image = self.game.transform.rotate(self.image, self.direction + 180)
            self.screen.blit(rotated_image,(self.x -25,self.y-25))
            self.lifespan -= 1
            self.x += self.x_speed
            self.y += self.y_speed
        else:
            self.despawn()
    def despawn(self):
        self.boss.current_attackers.remove(self)
        self.boss.current_attacks.remove(self)
        self.summoner.dagger = None
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y