
from code.Entity import Entity

from code.Const import ENTITY_SPEED


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple, owner, direction: int = 1):
        super().__init__(name, position)
        self.direction = direction
        self.owner = owner

    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name] * self.direction