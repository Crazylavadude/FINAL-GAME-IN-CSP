from enemy_attack_box import attack_boxes
from fireball import Fireball
import random
class attack2():
    def __init__(self, Game, screen, boss):
        self.Game = Game
        self.screen = screen
        self.boss = boss
        self.active_timer = 0
        self.x= 0
        self.y=0
        boss.current_attackers.append(self)

    def spawn(self):
        spawn_chance = random.randint(0, 200)
        direction = ""
        if(spawn_chance < 5):
            half_chance = random.randint(1,2)
            if(half_chance == 1):
                direction = direction + "y"
                random_y = random.randint(50, 670)
                half_chance2 = random.randint(1,2)
                if(half_chance2 == 1):
                    direction = direction + "l"
                    f1 = Fireball(self.Game,self.screen, direction,0,random_y, self.boss)
                    self.boss.current_attackers.append(f1)
                    self.boss.current_attacks.append(f1)
                else:
                    direction = direction + "r"
                    f1 = Fireball(self.Game,self.screen, direction,1280,random_y, self.boss)
                    self.boss.current_attackers.append(f1)
                    self.boss.current_attacks.append(f1)

            else:
                direction = direction + "x"
                random_x = random.randint(50, 1230)
                half_chance2 = random.randint(1,2)
                if(half_chance2 == 1):
                    direction = direction + "t"
                    f1 = Fireball(self.Game,self.screen, direction,random_x,0, self.boss)
                    self.boss.current_attackers.append(f1)
                    self.boss.current_attacks.append(f1)
                else:
                    direction = direction + "d"
                    f1 = Fireball(self.Game,self.screen, direction,random_x,720, self.boss)
                    self.boss.current_attackers.append(f1)
                    self.boss.current_attacks.append(f1)
        

