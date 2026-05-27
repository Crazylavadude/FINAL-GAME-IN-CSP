from enemy_attack_box import attack_boxes
from summon_wizard import Summon_wizard
from summon_dagger import Summon_dagger
import random
class Attack3():
    def __init__(self, Game, screen, boss):
        self.summon_count = 0
        self.Game = Game
        self.screen = screen
        self.boss = boss
        self.timer = 0
        boss.current_attackers.append(self)

    def spawn(self):
        if(self.summon_count < 3 and self.timer == 0):
            self.timer = 10 * 60
            self.summon_count += 1
            chance = random.randint(0,1)
            if(chance == 1):
                self.summon_dagger()
            else:
                self.summon_wizard()
        if(self.timer > 0):
            self.timer -= 1
    def summon_wizard(self):
        Summon_wizard(self.Game,self.screen,self.boss,self,0,0)
        return
    def summon_dagger(self):
        random_x = random.randint(50,1570)
        random_y = random.randint(400,800)

        Summon_dagger(self.Game,self.screen,self.boss,self,random_x,random_y)
        return

            
        