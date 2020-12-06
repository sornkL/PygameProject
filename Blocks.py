import pygame
from pygame.rect import Rect
from pygame.math import Vector2

from BaseBlock import BaseBlock
from Settings import *


class GeneralBlock(BaseBlock):
    def _is_collide(self, group: pygame.sprite.Group) -> bool:
        return pygame.sprite.spritecollide(self, group, False)

    def move(self, direction: Vector2, group):
        if self.is_move() and self.is_control():
            self.location += direction
            self.rect = Rect(self.location.x, self.location.y, CELL_SIZE_X, CELL_SIZE_Y)

            if self.location.x < 0 or self.location.x >= WORLD_MAX_X*CELL_SIZE_X or self.location.y < 0 \
                    or self.location.y >= WORLD_MAX_Y*CELL_SIZE_Y \
                    or self._is_collide(group):
                self.location -= direction
                self.rect = Rect(self.location.x, self.location.y, CELL_SIZE_X, CELL_SIZE_Y)


