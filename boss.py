from Entity import Entity
from attack1 import attack1
from attack2 import attack2
from fireball import Fireball
class Boss(Entity):
    def __init__(self, game, screen, player):
        super().__init__(game, screen)
        self.player = player
        self.current_attacks = []
        self.player_attack = None
        self.current_attackers = []
        self.player_health = 10
        self.boss_health = 0
        self.player_image = self.attribute1.image.load("sludgetop.png").convert_alpha()
        self.heart_images = [self.attribute1.image.load("slime-heart.png").convert_alpha(), self.attribute1.image.load("slime-heart-broken.png").convert_alpha()]

    def phase1(self):
        self.boss_health = 100
        a1 = attack1(self.attribute1, self.attribute2,self)
        a2 = attack2(self.attribute1, self.attribute2,self)
        self.current_attackers.append(a2)
        self.current_attackers.append(a1)
        a1.spawn()

    def phase2(self):
        self.boss_health = 200
        a2 = attack1(self.attribute1, self.attribute2,self)
        self.current_attackers.append(a2)
        a2.spawn()

    def phase_ongoing(self, dt):

        for object in self.current_attackers:
            object.spawn()
        keys = self.attribute1.key.get_pressed()
        if(keys[self.attribute1.K_SPACE]):
            self.player_attack = self.player.player_attack()
            self.attribute2.blit(self.player_image,(self.player.get_x() -40,self.player.get_y() - 40))
        elif(self.player.stun_count == 0):
            pos = self.player.player_move(dt)
            self.attribute2.blit(self.player_image,(pos.x -40, pos.y -40))
        else:
            self.player_attack = self.player.player_attack()
            self.attribute2.blit(self.player_image,(self.player.get_x() -40,self.player.get_y() - 40))
            self.player.stun_count = self.player.stun_count -1
        if(self.player.invulnerability > 0):
            self.player.invulnerability = self.player.invulnerability -1
        for num in range(10):
            if(num <= self.player_health):
                self.attribute2.blit(self.heart_images[0], (0 + 50 * num,0))
            else:
                self.attribute2.blit(self.heart_images[1], (0 + 50 * num,0))
        self.check_player_status()


    def check_player_status(self):
        for object in self.current_attacks:
            if( isinstance(object,attack1) ):
                if(self.player.get_x() > object.get_x() and self.player.get_x() < object.get_x()+100 and self.player.get_y() > object.get_y() and self.player.get_y() < object.get_y()+200 and object.active_timer < 60 and self.player.invulnerability == 0):
                    self.player_health = self.player_health - 1
                    self.player.invulnerability = 20
                    print(self.player_health)
                if(self.player_attack != None and self.player_attack[0] < object.get_x() + 100 and self.player_attack[0] + self.player_attack[2] > object.get_x() and self.player_attack[1] - self.player_attack[3] < object.get_y() and self.player_attack[1] > object.get_y() - 100 and object.active_timer < 60 and object.invulnerability == 0):
                    object.invulnerability = 60
                    self.boss_health = self.boss_health - 1
                    self.player_attack = None
                    print(self.boss_health)
            elif(isinstance(object, Fireball)):
                if(self.player.get_x() > object.get_x() and self.player.get_x() < object.get_x()+50 and self.player.get_y() > object.get_y() and self.player.get_y() < object.get_y()+50 and self.player.invulnerability == 0):
                    self.player_health -= 1
                    self.player.invulnerability = 20
                    print(self.player_health)
                

        
    
