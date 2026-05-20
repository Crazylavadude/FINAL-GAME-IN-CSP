from Entity import Entity
class Player(Entity):
    def __init__(self, Game, screen):
        super().__init__(Game, screen)

    def player_move(self, dt):
            keys = self.attribute1.key.get_pressed()
            if keys[self.attribute1.K_w]:
                self.pos.y -= 300 * dt
            if keys[self.attribute1.K_s]:
                self.pos.y += 300 * dt
            if keys[self.attribute1.K_a]:
                self.pos.x -= 300 * dt
            if keys[self.attribute1.K_d]:
                self.pos.x += 300 * dt
            return self.pos