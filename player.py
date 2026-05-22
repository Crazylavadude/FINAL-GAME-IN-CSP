import math
from Entity import Entity
class Player(Entity):
    def __init__(self, Game, screen):
        super().__init__(Game, screen)
        self.stun_count = 0
        self.current_goal_location = self.pos

    def player_move(self, dt):
            if(self.stun_count == 0):
                keys = self.attribute1.key.get_pressed()
                if(keys[self.attribute1.K_SPACE]):
                    self.player_attack()
                else:
                    if (keys[self.attribute1.K_w] and self.pos.y > 0):
                        self.pos.y -= 300 * dt
                    elif (keys[self.attribute1.K_s] and self.pos.y < 720):
                        self.pos.y += 300 * dt
                    if (keys[self.attribute1.K_a] and self.pos.x > 0):
                        self.pos.x -= 300 * dt
                    elif (keys[self.attribute1.K_d ] and self.pos.x < 1280):
                        self.pos.x += 300 * dt
            else:
               self.player_attack()
               self.stun_count = self.stun_count -1
            return self.pos
    
    def test_direction(self):
        return(self.attribute1.mouse.get_pos())

    
    def player_attack(self):
         mouse_location = self.test_direction()
         y_diff = self.get_y()- mouse_location[1]#if positive then mouse is above
         x_diff = self.get_x() - mouse_location[0]#if positive mouse is to the left
         if(x_diff != 0):
            angle = math.degrees(math.atan(y_diff/x_diff))
            if(x_diff > 0):
                if(angle < -70):
                    self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-50, self.get_y(),100,100))
                if(angle < -50):
                    self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-100, self.get_y(),100,100))
                elif(angle > -50 and angle < 50):
                    self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-100, self.get_y()-50,100,100))
                elif(angle > 50 and angle < 70):
                    self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-100, self.get_y()-100,100,100))   
                else:
                    self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-50, self.get_y()-100,100,100))
            else:
                if (angle < -70):
                    self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-50, self.get_y()-100,100,100))
                elif(angle < -50):
                    self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x(), self.get_y()-100,100,100))
                elif(angle > -50 and angle < 50):
                    self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x(), self.get_y()-50,100,100))
                elif(angle > 50 and angle < 70):
                    self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x(), self.get_y(),100,100)) 
                else:
                    self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-50, self.get_y(),100,100))
                    
         else:
            if(y_diff > 0):
                self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-50, self.get_y()-100,100,100))
            else:
                self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-50, self.get_y(),100,100))
         if(self.stun_count == 0):
            self.stun_count = 10

    def get_x(self):
        return self.pos.x

    def get_y(self):
        return self.pos.y
    