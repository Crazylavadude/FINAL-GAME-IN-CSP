class attack1():
    def __init__(self, Game, screen, boss):
        self.Game = Game
        self.screen = screen
        self.boss = boss

    def spawn(self):
        self.Game.draw.rect(self.screen,(100,100,100), (720, 360,100,200))
    