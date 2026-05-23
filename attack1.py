import random
from enemy_attack_box import attack_boxes
class attack1(attack_boxes):
    def __init__(self, Game, screen, boss):
        super().__init__(Game, screen, boss)
        self.invulnerability = 0


    def spawn(self):
        if(random.randint(0,120) == 1 and self.active_timer == 0):
            self.boss.current_attacks.append(self)
            self.active_timer = 180
            self.determine_location()
        if(self.active_timer > 0):
            self.active_timer = self.active_timer -1
            
            if(self.active_timer > 130):
                    self.Game.draw.rect(self.screen,(255,100,100), (self.x, self.y,100,200))
            elif(self.active_timer > 60):
                    self.Game.draw.rect(self.screen,(255,0,0), (self.x, self.y,100,200))
            elif(self.active_timer > 0):
                    self.Game.draw.rect(self.screen,(0,0,0), (self.x, self.y,100,200))
            else:
                self.boss.current_attacks.remove(self)
        if(self.invulnerability > 0):
            self.invulnerability = self.invulnerability -1
    
    def determine_location(self):
        p = self.boss.player
        keys = self.Game.key.get_pressed()
        self.y = p.pos.y -50
        self.x = p.pos.x - 50
        if (keys[self.Game.K_w]):
                        self.y = p.pos.y - 80
        elif (keys[self.Game.K_s]):
                        self.y = p.pos.y - 20
        if (keys[self.Game.K_a] ):
                        self.x = p.pos.x - 80
        elif (keys[self.Game.K_d ]):
                        self.x = p.pos.x  - 20
                