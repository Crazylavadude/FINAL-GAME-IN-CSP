from Entity import Entity
class Player(Entity):
    def __init__(self, Game, screen):
        super().__init__(Game, screen)
        self.stun_count = 0
        self.direction = "East"
        self.current_goal_location = self.pos

    def player_move(self, dt):
            self.current_goal_location = self.test_move()
            if(self.current_goal_location == self.pos):
                return self.pos
            else:
                y_difference = self.pos.y - self.current_goal_location[1]
                x_difference = self.pos.x - self.current_goal_location[0]
                if(y_difference < 10 and y_difference > -10):
                    self.pos.y = self.pos.y - y_difference
                else:
                    if(y_difference < 0):
                        self.pos.y = self.pos.y +10
                    elif(y_difference > 0):
                        self.pos.y = self.pos.y - 10
                if(x_difference < 10 and x_difference > -10):
                    self.pos.x = self.pos.x - x_difference
                else:
                    if(x_difference < 0):
                        self.pos.x = self.pos.x + 10
                    elif(x_difference > 0):
                        self.pos.x = self.pos.x - 10
            '''
            temporary_direction = ""
            if(self.stun_count == 0):
                keys = self.attribute1.key.get_pressed()
                if(keys[self.attribute1.K_SPACE]):
                    self.player_attack()
                else:
                    if keys[self.attribute1.K_w]:
                        self.pos.y -= 300 * dt
                        temporary_direction = temporary_direction + "North"
                    elif keys[self.attribute1.K_s]:
                        self.pos.y += 300 * dt
                        temporary_direction = temporary_direction + "South"
                    if keys[self.attribute1.K_a]:
                        self.pos.x -= 300 * dt
                        temporary_direction = temporary_direction + "West"
                    elif keys[self.attribute1.K_d]:
                        self.pos.x += 300 * dt
                        temporary_direction = temporary_direction + "East"
            else:
               self.player_attack()
               self.stun_count = self.stun_count -1
            if(temporary_direction == ""):
                return self.pos
            else:
                self.direction = temporary_direction
            '''

            return self.pos
    
    def test_move(self):
        mouse_buttons = self.attribute1.mouse.get_pressed()
        if(mouse_buttons[0]):
            return(self.attribute1.mouse.get_pos())
        return self.current_goal_location

    
    def player_attack(self):
         if(self.direction == "North"):
             self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-50, self.get_y()-100,100,100))
         elif(self.direction == "South"):
             self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-50, self.get_y(),100,100))
         elif(self.direction == "East"):
             self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x(), self.get_y()-50,100,100))
         elif(self.direction == "West"):     
            self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-100, self.get_y()-50,100,100))
         elif(self.direction == "NorthWest"):
             self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-100, self.get_y()-100,100,100))
         elif(self.direction == "NorthEast"):
             self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x(), self.get_y()-100,100,100))
         elif(self.direction == "SouthWest"):
             self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x()-100, self.get_y(),100,100))
         elif(self.direction == "SouthEast"):
             self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x(), self.get_y(),100,100))
         if(self.stun_count == 0):
            self.stun_count = 10

    def get_x(self):
        return self.pos.x

    def get_y(self):
        return self.pos.y
    