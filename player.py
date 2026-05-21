from Entity import Entity
class Player(Entity):
    def __init__(self, Game, screen):
        super().__init__(Game, screen)
        self.stun_count = 0

    def player_move(self, dt):
            if(self.stun_count == 0):
                keys = self.attribute1.key.get_pressed()
                if(keys[self.attribute1.K_f]):
                    self.player_attack()
                else:
                    if keys[self.attribute1.K_w]:
                        self.pos.y -= 300 * dt
                    if keys[self.attribute1.K_s]:
                        self.pos.y += 300 * dt
                    if keys[self.attribute1.K_a]:
                        self.pos.x -= 300 * dt
                    if keys[self.attribute1.K_d]:
                        self.pos.x += 300 * dt
            else:
               self.stun_count = self.stun_count -1
               self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x() + 20, self.get_y()-50,100,100))
            return self.pos

    
    def player_attack(self):
         self.attribute1.draw.rect(self.attribute2, "blue", (self.get_x() + 20, self.get_y()-50,100,100))
         self.stun_count = 10

    def get_x(self):
        return self.pos.x

    def get_y(self):
        return self.pos.y
    
