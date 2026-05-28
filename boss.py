from Entity import Entity
from attack1 import attack1
from attack2 import attack2
from fireball import Fireball
from attack3 import Attack3
from summon_dagger import Summon_dagger
from summon_wizard import Summon_wizard
from mage_fireball import Mage_fireball
from dagger import Dagger
class Boss(Entity):
    def __init__(self, game, screen, player):
        super().__init__(game, screen)
        self.player = player
        self.current_attacks = []
        self.player_attack = None
        self.current_attackers = []
        self.player_health = 5
        self.boss_health = 0
        self.player_image = self.attribute1.image.load("sludgetop.png").convert_alpha()
        self.heart_images = [self.attribute1.image.load("slime-heart.png").convert_alpha(), self.attribute1.image.load("slime-heart-broken.png").convert_alpha()]
        self.bar_image = [self.attribute1.image.load("healthbar.png").convert_alpha(),self.attribute1.image.load("healthbar-1.png").convert_alpha() ]
        self.wall_image = [self.attribute1.image.load("wall-bottom-frame1.png").convert_alpha(),self.attribute1.image.load("wall-bottom-frame2.png").convert_alpha(),self.attribute1.image.load("wall-bottom-frame3.png").convert_alpha(),self.attribute1.image.load("wall-frame-4.png").convert_alpha(),self.attribute1.image.load("wall-frame-5.png").convert_alpha(),self.attribute1.image.load("wall-frame-6.png").convert_alpha()]
        self.phase = 0
        self.setup_count = 299
        self.death_count = 280
        self.boss= [game.image.load("bass-frame1.png").convert_alpha(),game.image.load("bass-frame2.png").convert_alpha(),game.image.load("bass-frame3.png").convert_alpha(),game.image.load("boss.png").convert_alpha(),game.image.load("puddle-frame-4.png").convert_alpha()]
        self.sword = game.image.load("sword-east.png").convert_alpha()

    def phase1(self):
        self.phase = 1
        self.player_health = 5
        self.current_attackers.clear()
        self.current_attacks.clear()
        self.boss_health = 5
        Attack3(self.attribute1,self.attribute2,self)
        attack1(self.attribute1, self.attribute2,self)


    def phase2(self):
        self.boss_health = 10
        attack1(self.attribute1, self.attribute2,self)
        attack2(self.attribute1, self.attribute2,self)
        harder_attackers = []
        for attacks in self.current_attackers:
            if(isinstance(attacks, attack1)):
                harder_attackers.append(attacks)
        for attack in harder_attackers:
            self.current_attackers.append(attack)
        self.phase = 2

    def death(self):
        if(self.death_count <10):
            return
        if(self.death_count < 80):
           self.attribute2.blit(self.boss[4],(self.attribute2.get_width() / 2 -100,200))
           self.attribute2.blit(self.boss[0],(self.attribute2.get_width() / 2 -150,0))
           self.death_count -= 1
        elif(self.death_count < 160):
            self.attribute2.blit(self.boss[4],(self.attribute2.get_width() / 2 -100,200))
            self.attribute2.blit(self.boss[1],(self.attribute2.get_width() / 2 -150,0))
            self.death_count -= 1
        elif(self.death_count < 230):
            self.attribute2.blit(self.boss[4],(self.attribute2.get_width() / 2 -100,200))
            self.attribute2.blit(self.boss[2],(self.attribute2.get_width() / 2 -150,0))

            self.death_count -= 1
        elif(self.death_count < 300):
           self.attribute2.blit(self.boss[3],(self.attribute2.get_width() / 2 -150,0))

           self.death_count -= 1

    def setup(self,):
        if(self.phase == 2):
            if(self.boss_health == 0):
                self.death()
                self.current_attackers.clear()
                self.current_attacks.clear()
                return
        self.boss_animation()
        self.wall_animation()
        if(self.setup_count < 0 and self.phase ==0):
            self.phase1()

    def boss_animation(self):
        
        if(self.setup_count < 80):
            self.attribute2.blit(self.boss[3],(self.attribute2.get_width() / 2 -150,0))
        elif(self.setup_count < 160):
            self.attribute2.blit(self.boss[4],(self.attribute2.get_width() / 2 -100,200))
            self.attribute2.blit(self.boss[2],(self.attribute2.get_width() / 2 -150,0))
            self.setup_count -= 1
        elif(self.setup_count < 230):
            self.attribute2.blit(self.boss[4],(self.attribute2.get_width() / 2 -100,200))
            self.attribute2.blit(self.boss[1],(self.attribute2.get_width() / 2 -150,0))
            self.setup_count -= 1
        elif(self.setup_count < 300):
           self.attribute2.blit(self.boss[4],(self.attribute2.get_width() / 2 -100,200))
           self.attribute2.blit(self.boss[0],(self.attribute2.get_width() / 2 -150,0))
           self.setup_count -= 1
        
    def wall_animation(self):
        if(self.setup_count < 0):
            self.attribute2.blit(self.wall_image[5],(0,200))
        elif(self.setup_count < 40):
            self.attribute2.blit(self.wall_image[4],(0,200))
            self.setup_count -= 1
        elif(self.setup_count < 80):
            self.attribute2.blit(self.wall_image[3],(0,200))
            self.setup_count -= 1
        elif(self.setup_count < 120):
            self.attribute2.blit(self.wall_image[2],(0,200))
            self.setup_count -= 1
        elif(self.setup_count < 160):
            self.attribute2.blit(self.wall_image[1],(0,200))
            self.setup_count -= 1
        elif(self.setup_count < 230):
            self.attribute2.blit(self.wall_image[0],(0,200))
            self.setup_count -= 1

    def phase_ongoing(self, dt):
        for object in self.current_attackers:
            object.spawn()
        keys = self.attribute1.key.get_pressed()
        direction = self.player.set_direction()
        rotated_image = self.attribute1.transform.rotate(self.player_image, direction)
        rotated_sword = self.attribute1.transform.rotate(self.sword, direction)
        if(keys[self.attribute1.K_SPACE]):
            self.player_attack = self.player.player_attack()
            self.attribute2.blit(rotated_image,(self.player.get_x() -40,self.player.get_y() - 40))
        elif(self.player.stun_count == 0):
            pos = self.player.player_move(dt)
            self.player_attack = None
            if(direction< 0):
                direction = 360 + direction
            if(direction > 360):
                direction = direction - 360
            if(direction <= 90):
                self.attribute2.blit(rotated_sword,(pos.x +30-(40 * direction/90), pos.y - (120*direction/90)))
            elif(direction<= 180):
                self.attribute2.blit(rotated_sword,(pos.x, pos.y - 20))
            elif(direction<= 270):
                self.attribute2.blit(rotated_sword,(pos.x, pos.y - 20))
            elif(direction<= 360):
                self.attribute2.blit(rotated_sword,(pos.x, pos.y - 20))
            self.attribute2.blit(rotated_image,(pos.x -40, pos.y -40))
        else:
            self.player_attack = self.player.player_attack()
            self.attribute2.blit(rotated_image,(self.player.get_x() -40,self.player.get_y() - 40))
            self.player.stun_count = self.player.stun_count -1
        if(self.player.invulnerability > 0):
            self.player.invulnerability = self.player.invulnerability -1
        self.check_player_status()
        for num in range(5):
            if(num < self.player_health):
                self.attribute2.blit(self.heart_images[0], (0 + 50 * num,0))
            else:
                self.attribute2.blit(self.heart_images[1], (0 + 50 * num,0))
        if(self.phase == 1):
            if(self.boss_health <= 0):
                self.phase2()
            self.attribute1.draw.rect(self.attribute2,(0,0,0),(self.attribute2.get_width()/2 - 550,self.attribute2.get_height() - 150, 1175, 80))
            self.attribute1.draw.rect(self.attribute2,(255,0,0),(self.attribute2.get_width()/2 - 550,self.attribute2.get_height() - 150, 235*self.boss_health, 80))
            self.attribute2.blit(self.bar_image[1],(self.attribute2.get_width()/2 - 600,self.attribute2.get_height() - 200))
        elif(self.phase == 2):
            if(self.boss_health == 0):
                return
            self.attribute1.draw.rect(self.attribute2,(0,0,0),(self.attribute2.get_width()/2 - 550,self.attribute2.get_height() - 150, 1175, 80))
            self.attribute1.draw.rect(self.attribute2,(255,0,0),(self.attribute2.get_width()/2 - 550,self.attribute2.get_height() - 150, (1175/10)*self.boss_health, 80))
            self.attribute2.blit(self.bar_image[0],(self.attribute2.get_width()/2 - 600,self.attribute2.get_height() - 200))


    def check_player_status(self):
        for object in self.current_attacks:
            if(isinstance(object, attack1)):
                    if(self.player.get_x()+20 > object.get_x() and self.player.get_x() - 20 < object.get_x()+100 and self.player.get_y() +20 > object.get_y() + 40 and self.player.get_y()-20 < object.get_y()+200 and object.active_timer < 100 and object.active_timer > 50 and self.player.invulnerability == 0):
                        self.player_health = self.player_health - 1
                        self.player.invulnerability = 60
                    elif(self.player.get_x()+20 > object.get_x() and self.player.get_x() -20 < object.get_x()+100 and self.player.get_y()+20 > object.get_y() + 100 and self.player.get_y()-20 < object.get_y()+200 and ((object.active_timer < 130 and object.active_timer > 100)or(object.active_timer < 50 and object.active_timer > 30)) and self.player.invulnerability == 0):
                        self.player_health = self.player_health - 1
                        self.player.invulnerability = 60
                    elif(self.player.get_x()+20 > object.get_x() and self.player.get_x()-20 < object.get_x()+100 and self.player.get_y()+20 > object.get_y() + 160 and self.player.get_y()-20 < object.get_y()+200 and ((object.active_timer < 160 and object.active_timer > 130)or(object.active_timer < 30 and object.active_timer > 0)) and self.player.invulnerability == 0):
                        self.player_health = self.player_health - 1
                        self.player.invulnerability = 60
                    if(self.player_attack != None and self.player_attack[0] < object.get_x() + 100 and self.player_attack[0] + self.player_attack[2] > object.get_x() and self.player_attack[1] - self.player_attack[3] < object.get_y() + 40 and self.player_attack[1] > object.get_y() - 100 and object.active_timer < 100 and object.active_timer > 50  and object.invulnerability == 0):
                        object.invulnerability = 60
                        self.boss_health = self.boss_health - 1
                        self.player_attack = None
                        print(self.boss_health)
                    elif(self.player_attack != None and self.player_attack[0] < object.get_x() + 100 and self.player_attack[0] + self.player_attack[2] > object.get_x() and self.player_attack[1] - self.player_attack[3] < object.get_y() + 100 and self.player_attack[1] > object.get_y() - 100 and ((object.active_timer < 130 and object.active_timer > 100)or(object.active_timer < 50 and object.active_timer > 30))  and object.invulnerability == 0):
                        object.invulnerability = 60
                        self.boss_health = self.boss_health - 1
                        self.player_attack = None
                    elif(self.player_attack != None and self.player_attack[0] < object.get_x() + 100 and self.player_attack[0] + self.player_attack[2] > object.get_x() and self.player_attack[1] - self.player_attack[3] < object.get_y() + 160 and self.player_attack[1] > object.get_y() - 100 and ((object.active_timer < 160 and object.active_timer > 130)or(object.active_timer < 30 and object.active_timer > 0))  and object.invulnerability == 0):
                        object.invulnerability = 60
                        self.boss_health = self.boss_health - 1
                        self.player_attack = None
            elif(isinstance(object, Fireball)):
                    if(self.player.get_x() +20 > object.get_x() and self.player.get_x()-20 < object.get_x()+50 and self.player.get_y()+20 > object.get_y() and self.player.get_y()-20 < object.get_y()+50):
                        if(self.player.invulnerability == 0):
                            self.player_health -= 1
                            self.player.invulnerability = 20
                        object.despawn()
                        print(self.player_health)
                    elif(self.player_attack != None and self.player_attack[0] < object.get_x() + 50 and self.player_attack[0] + self.player_attack[2] > object.get_x() and self.player_attack[1] - self.player_attack[3] < object.get_y() + 40 and self.player_attack[1] > object.get_y() - 50):
                        object.despawn()
            elif(isinstance(object, Mage_fireball)):
                if(self.player.get_x()+20 > object.get_x() and self.player.get_x()-20 < object.get_x()+50 and self.player.get_y()+20 > object.get_y() and self.player.get_y()-20 < object.get_y()+50 and self.player.invulnerability == 0):
                    self.player_health -= 1
                    self.player.invulnerability = 20
            elif(isinstance(object, Summon_wizard)):
                if(self.player_attack != None and self.player_attack[0] < object.get_x() + 50 and self.player_attack[0] + self.player_attack[2] > object.get_x() and self.player_attack[1] - self.player_attack[3] < object.get_y() + 40 and self.player_attack[1] > object.get_y() - 75):
                    object.despawn()
            elif(isinstance(object, Summon_dagger)):
                if(self.player_attack != None and self.player_attack[0] < object.get_x() + 50 and self.player_attack[0] + self.player_attack[2] > object.get_x() and self.player_attack[1] - self.player_attack[3] < object.get_y() + 40 and self.player_attack[1] > object.get_y() - 75):
                    object.despawn()
            elif(isinstance(object, Dagger)):
                if(self.player.get_x()+20 > object.get_x() and self.player.get_x()-20 < object.get_x()+20 and self.player.get_y()+20 > object.get_y() and self.player.get_y()-20 < object.get_y()+20 and self.player.invulnerability == 0):
                    self.player_health -= 1
                    self.player.invulnerability = 20

                

        
    
