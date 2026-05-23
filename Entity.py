class Entity():
    def __init__(self, Game, screen):
        self.attribute1  = Game
        self.attribute2 = screen
        self.pos = Game.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    def get_x(self):
        return self.pos.x

    def get_y(self):
        return self.pos.y