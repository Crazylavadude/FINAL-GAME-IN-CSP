import random
from enemy_attack_box import attack_boxes
class attack1(attack_boxes):
    def __init__(self, Game, screen, boss):
        super().__init__(Game, screen, boss)
        self.images = [self.Game.image.load("puddle-frame-1.png").convert_alpha(),self.Game.image.load("puddle-frame-2.png").convert_alpha(),self.Game.image.load("puddle-frame-3.png").convert_alpha(),self.Game.image.load("puddle-frame-4.png").convert_alpha(),self.Game.image.load("attack-1-frame-1.png").convert_alpha(),self.Game.image.load("attack-1-frame-2.png").convert_alpha(),self.Game.image.load("attack-1-finish.png").convert_alpha()]
        self.invulnerability = 0
        boss.current_attackers.append(self)


    def spawn(self):
        if(random.randint(0,120) == 1 and self.active_timer == 0):
            self.boss.current_attacks.append(self)
            self.active_timer = 280
            self.determine_location()
        if(self.active_timer > 0):
            self.active_timer = self.active_timer -1
            
            if(self.active_timer > 250):
                    self.screen.blit(self.images[0],(self.x- 20, self.y +40))
            elif(self.active_timer > 220):
                    self.screen.blit(self.images[1],(self.x- 20, self.y+40))
            elif(self.active_timer > 190):
                    self.screen.blit(self.images[2],(self.x- 20, self.y+40))
            elif(self.active_timer > 160):
                    self.screen.blit(self.images[3],(self.x- 20, self.y+40))
            elif(self.active_timer > 130 or (self.active_timer <= 30 and self.active_timer > 0)):
                    self.screen.blit(self.images[4],(self.x- 20, self.y+40))
            elif(self.active_timer > 100 or (self.active_timer <= 50 and self.active_timer > 30)):
                    self.screen.blit(self.images[5],(self.x- 20, self.y+40))
            elif(self.active_timer > 50):
                    self.screen.blit(self.images[6],(self.x- 20, self.y+40))
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
                