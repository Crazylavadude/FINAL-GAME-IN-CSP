
from dagger import Dagger
import math
import random
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
        self.stun = 3*60
        self.goal_x = None
        self.goal_y = None
        self.speed_y = 0
        self.speed_x = 0


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

    def spawn(self):
        speed = 5
        if(self.goal_x == None and self.goal_y == None):
            self.goal_x = random.randint(50,1550)
            self.goal_y = random.randint(400,800)
        elif(self.speed_x == 0 and self.speed_y == 0):
            x_diff = self.goal_x - self.x
            y_diff = self.goal_y - self.y
            time = math.sqrt(math.pow(x_diff,2) + math.pow(y_diff,2))/speed
            
            self.speed_x = x_diff/time
            self.speed_y = y_diff/time
        elif(10 > abs(self.goal_x - self.x) and 10 > abs(self.goal_y - self.y)):
            self.goal_x = None
            self.goal_y = None
            self.speed_x = 0
            self.speed_y = 0
        else:
            self.x += self.speed_x
            self.y += self.speed_y
        if(self.stun == 0):
            self.attack()
            self.stun = 5*60
        if(self.stun > 0):
            self.stun -= 1
        self.screen.blit(self.image,(self.x-12.5,self.y-25))
    def attack(self):
        direction = self.get_desired_angle()
        direction1 = direction + 45
        direction2 = direction - 45
        if(direction1 > 360):
            direction1 = direction1 - 360
        if(direction2 < 0):
            direction2 = 360 + direction2
        Dagger(self.Game, self.screen, self.boss,self, self.x, self.y, direction1)
        Dagger(self.Game, self.screen, self.boss,self, self.x, self.y, direction)
        Dagger(self.Game, self.screen, self.boss,self, self.x, self.y, direction2)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def despawn(self):
        self.boss.current_attackers.remove(self)
        self.boss.current_attacks.remove(self)
        self.attack3.summon_count -= 1