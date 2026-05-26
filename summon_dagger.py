class Summon_dagger():
    def __init__(self, Game, screen, boss, x, y):
        self.Game = Game
        self.screen =screen
        self.boss = boss
        self.x = x
        self.y = y
        self.image = self.Game.image.load("Summon-dagger.png").convert_alpha()
        boss.current_attackers.append(self)

    def spawn(self):
        return