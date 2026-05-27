import math
class Mage_fireball():
    def __init__(self, game, screen, boss, x ,y):
        self.Game = game
        self.screen =screen
        self.boss = boss
        self.x = x
        self.y = y
        self.current_angle = 0
        self.desired_angle = 0
        boss.current_attackers.append(self)
        boss.current_attacks.append(self)
        self.count = 0
        self.image = [self.Game.image.load("mage-fireball-1.png").convert_alpha(),self.Game.image.load("mage-fireball-2.png").convert_alpha()]

    def spawn(self):
            desired_angle = self.get_desired_angle()
            if(self.current_angle > 360):
                self.current_angle = self.current_angle - 360
            if(desired_angle == self.current_angle):
                counter_clockwise = 0
            else:
                counter_clockwise = desired_angle -self.current_angle
                if(counter_clockwise < 0):
                    counter_clockwise = 360 + counter_clockwise
            clockwise = 360 - counter_clockwise

            if(counter_clockwise <= clockwise):
                self.current_angle = counter_clockwise/50 + self.current_angle 
            elif(clockwise < counter_clockwise):
                self.current_angle = -clockwise/50 + self.current_angle 
            else:
                self.current_angle = self.desired_angle
            speed = 3
            if(self.current_angle < 0):
                self.current_angle = 360 + self.current_angle
            angle = self.get_tangent_angle(self.current_angle)
            if(angle == 90):
                self.y -= speed
            elif(angle == -90):
                self.y += speed
            elif(angle == 0):
                if(self.current_angle == 0):
                    self.x += speed
                else:
                    self.x -= speed
            else:
                if(angle < 0):
                    angle = -angle
                angle = math.radians(angle)
                if(self.current_angle < 90 ):
                    self.x += speed*math.cos(angle)
                    self.y -=speed*math.sin(angle)
                elif(self.current_angle < 180 ):
                    self.x -=speed*math.cos(angle)
                    self.y -=speed*math.sin(angle)
                elif(self.current_angle < 270 ):
                    self.x -=speed*math.cos(angle)
                    self.y +=speed*math.sin(angle)
                elif(self.current_angle < 360 ):
                    self.x +=speed*math.cos(angle)
                    self.y +=speed*math.sin(angle)
            

            rotated_image = self.Game.transform.rotate(self.select_image(), self.current_angle + 90)
            self.screen.blit(rotated_image,(self.x -25,self.y-25))
    
    def get_tangent_angle(self, current_angle):
        x_diff = self.x - self.boss.player.get_x()
        y_diff = self.y - self.boss.player.get_y()
        if(x_diff != 0):
            if(current_angle < 90):
                return current_angle
            elif(current_angle <180):
                return 180 - current_angle
            elif(current_angle < 270):
                return 180 - current_angle
            elif(current_angle<360):
                return 360 - current_angle
            else:
                return 0
        elif(current_angle == 90):
            return 90
        else:
            return -90
        


    def get_desired_angle(self):
        x_diff = self.x - self.boss.player.get_x()
        y_diff = self.y - self.boss.player.get_y()
        if(x_diff != 0):
            angle = math.degrees(math.atan(y_diff/x_diff))
            if(y_diff > 0 and x_diff < 0):
                return -angle
            elif(y_diff > 0 and x_diff > 0):
                return 180 -angle
            elif(y_diff < 0 and x_diff > 0):
                return 180 -angle
            elif(y_diff < 0 and x_diff < 0):
                return 360 - angle
            else:
                return angle
            
        elif(y_diff > 0):
            return 90
        else:
            return 270
    def select_image(self):
        self.count += 1
        if(self.count > 10):
            if(self.count > 20):
                self.count = 0
            return self.image[0]
        else:
            return self.image[1]

    def despawn(self):
        self.boss.current_attackers.remove(self)
        self.boss.current_attacks.remove(self)

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y