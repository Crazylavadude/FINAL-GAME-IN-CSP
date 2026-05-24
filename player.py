import math
from Entity import Entity
class Player(Entity):
    def __init__(self, Game, screen):
        super().__init__(Game, screen)
        self.stun_count = 0
        self.current_goal_location = self.pos
        self.sword_list = [self.attribute1.image.load("sword-east.png").convert_alpha(), self.attribute1.image.load("sword-northeast.png").convert_alpha(),self.attribute1.image.load("sword-north.png").convert_alpha(), self.attribute1.image.load("northwest-sword.png").convert_alpha(), self.attribute1.image.load("west-sword.png").convert_alpha(), self.attribute1.image.load("southwest-sword.png").convert_alpha(), self.attribute1.image.load("south-sword.png").convert_alpha(), self.attribute1.image.load("southeast-sword.png").convert_alpha()]
        self.invulnerability = 0

    def player_move(self, dt):
            keys = self.attribute1.key.get_pressed()
            if (keys[self.attribute1.K_w] and self.pos.y > 350):
                self.pos.y -= 300 * dt
            elif (keys[self.attribute1.K_s] and self.pos.y < self.attribute2.get_height()):
                self.pos.y += 300 * dt
            if (keys[self.attribute1.K_a] and self.pos.x > 0):
                self.pos.x -= 300 * dt
            elif (keys[self.attribute1.K_d ] and self.pos.x < self.attribute2.get_width()):
                self.pos.x += 300 * dt
            return self.pos
    
    def set_direction(self):
        mouse_location = self.test_direction()
        y_diff = self.get_y()- mouse_location[1]#if positive then mouse is above
        x_diff = self.get_x() - mouse_location[0]#if positive mouse is to the left
        if(x_diff != 0):
            angle = math.degrees(math.atan(y_diff/x_diff))
        elif(y_diff > 0):
            return 270
        elif(y_diff < 0):
            return 90
        if(x_diff > 0):
            return 180 - angle
        elif(x_diff < 0):
            return -angle
        return angle + 180

        
    
    def test_direction(self):
        return(self.attribute1.mouse.get_pos())

    
    def player_attack(self):
         mouse_location = self.test_direction()
         y_diff = self.get_y()- mouse_location[1]#if positive then mouse is above
         x_diff = self.get_x() - mouse_location[0]#if positive mouse is to the left
         if(self.stun_count == 0):
            self.stun_count = 20
         if(x_diff != 0):
            angle = math.degrees(math.atan(y_diff/x_diff))
            if(x_diff > 0):
                if(angle < -70):#south
                    if(self.stun_count > 13):
                        self.attribute2.blit(self.sword_list[5],(self.get_x() -100,self.get_y()+ 10))
                    elif(self.stun_count > 6):
                        self.attribute2.blit(self.sword_list[6],(self.get_x()-50,self.get_y()+ 30))
                    else:
                        self.attribute2.blit(self.sword_list[7],(self.get_x() + 10,self.get_y()))
                    return [self.get_x() -50, self.get_y(), 100,100]
                elif(angle < -50):#south west
                    if(self.stun_count > 13):
                        self.attribute2.blit(self.sword_list[4],(self.get_x()-120,self.get_y() - 50))
                    elif(self.stun_count > 6):
                        self.attribute2.blit(self.sword_list[5],(self.get_x() -100,self.get_y()+ 10))
                    else:
                        self.attribute2.blit(self.sword_list[6],(self.get_x()-50,self.get_y()+ 30))
                    return [self.get_x() -100, self.get_y(), 100,100]
                elif(angle > -50 and angle < 50):#west
                    if(self.stun_count > 13):
                        self.attribute2.blit(self.sword_list[3],(self.get_x()-90,self.get_y() - 90))
                    elif(self.stun_count > 6):
                        self.attribute2.blit(self.sword_list[4],(self.get_x() -120,self.get_y()-50))
                    else:
                        self.attribute2.blit(self.sword_list[5],(self.get_x()-100,self.get_y()+ 10))
                    return [self.get_x() -100, self.get_y()-50, 100,100]
                elif(angle > 50 and angle < 70):#north west
                    if(self.stun_count > 13):
                        self.attribute2.blit(self.sword_list[2],(self.get_x() - 40,self.get_y() - 110))
                    elif(self.stun_count > 6):
                        self.attribute2.blit(self.sword_list[3],(self.get_x() -90,self.get_y()-90))
                    else:
                        self.attribute2.blit(self.sword_list[4],(self.get_x()-120,self.get_y()-50))
                    return [self.get_x() -100, self.get_y()-100, 100,100]   
                else:#north
                    if(self.stun_count > 13):
                        self.attribute2.blit(self.sword_list[1],(self.get_x() + 10,self.get_y() - 90))
                    elif(self.stun_count > 6):
                        self.attribute2.blit(self.sword_list[2],(self.get_x() -40,self.get_y()-110))
                    else:
                        self.attribute2.blit(self.sword_list[3],(self.get_x()-90,self.get_y()-90))
                    return [self.get_x() -50, self.get_y()-100, 100,100]
            else:
                if (angle < -70):#north
                    if(self.stun_count > 13):
                        self.attribute2.blit(self.sword_list[1],(self.get_x() + 10,self.get_y() - 90))
                    elif(self.stun_count > 6):
                        self.attribute2.blit(self.sword_list[2],(self.get_x() -40,self.get_y()-110))
                    else:
                        self.attribute2.blit(self.sword_list[3],(self.get_x()-90,self.get_y()-90))
                    return [self.get_x() -50, self.get_y()-100, 100,100]
                elif(angle < -50):#north east
                    if(self.stun_count > 13):
                        self.attribute2.blit(self.sword_list[0],(self.get_x() + 30,self.get_y() - 50))
                    elif(self.stun_count > 6):
                        self.attribute2.blit(self.sword_list[1],(self.get_x() +10,self.get_y()-90))
                    else:
                        self.attribute2.blit(self.sword_list[2],(self.get_x()-40,self.get_y()-110))
                    return [self.get_x(), self.get_y()-100, 100,100]
                elif(angle > -50 and angle < 50):#east
                    if(self.stun_count > 13):
                        self.attribute2.blit(self.sword_list[7],(self.get_x() + 10,self.get_y()))
                    elif(self.stun_count > 6):
                        self.attribute2.blit(self.sword_list[0],(self.get_x() +30,self.get_y()-50))
                    else:
                        self.attribute2.blit(self.sword_list[1],(self.get_x()+10,self.get_y()-90))
                    return [self.get_x(), self.get_y()-50, 100,100]
                elif(angle > 50 and angle < 70):#south east
                    if(self.stun_count > 13):
                        self.attribute2.blit(self.sword_list[6],(self.get_x() -50,self.get_y()+30))
                    elif(self.stun_count > 6):
                        self.attribute2.blit(self.sword_list[7],(self.get_x() +10,self.get_y()))
                    else:
                        self.attribute2.blit(self.sword_list[0],(self.get_x()+30,self.get_y()-50)) 
                    return [self.get_x(), self.get_y(), 100,100]
                else:#south
                    if(self.stun_count > 13):
                        self.attribute2.blit(self.sword_list[5],(self.get_x() -100,self.get_y()+ 10))
                    elif(self.stun_count > 6):
                        self.attribute2.blit(self.sword_list[6],(self.get_x()-50,self.get_y()+ 30))
                    else:
                        self.attribute2.blit(self.sword_list[7],(self.get_x() + 10,self.get_y()))
                    return [self.get_x() -50, self.get_y(), 100,100]
                    
         else:
            if(y_diff > 0):
                if(self.stun_count > 13):
                    self.attribute2.blit(self.sword_list[1],(self.get_x() + 10,self.get_y() - 90))
                elif(self.stun_count > 6):
                    self.attribute2.blit(self.sword_list[2],(self.get_x() -40,self.get_y()-110))
                else:
                    self.attribute2.blit(self.sword_list[3],(self.get_x()-90,self.get_y()-90))
                
            else:
                if(self.stun_count > 13):
                    self.attribute2.blit(self.sword_list[5],(self.get_x() -100,self.get_y()+ 10))
                elif(self.stun_count > 6):
                    self.attribute2.blit(self.sword_list[6],(self.get_x()-50,self.get_y()+ 30))
                else:
                    self.attribute2.blit(self.sword_list[7],(self.get_x() + 10,self.get_y()))


    def get_x(self):
        return self.pos.x

    def get_y(self):
        return self.pos.y
    