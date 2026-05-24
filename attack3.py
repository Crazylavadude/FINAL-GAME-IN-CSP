from enemy_attack_box import attack_boxes
import random
class Attack3():
    def __init__(self, Game, screen, boss):
        self.summon_count = 0
        self.Game = Game
        self.screen = screen
        self.boss = boss
        self.timer = 0

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
        return
    def summon_dagger(self):
        return

            
        