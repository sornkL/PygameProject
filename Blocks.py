import pygame
from pygame.math import Vector2

from BaseBlock import BaseBlock
from Settings import *


class GeneralBlock(BaseBlock):
    def move(self, direction: Vector2):
        if self._is_move() and self._is_control():
            _newLocation = self.location + direction

            if _newLocation.x < 0 or _newLocation.x > WORLD_MAX_X*CELL_SIZE_X or _newLocation.y < 0 or _newLocation.y > WORLD_MAX_Y*CELL_SIZE_Y:
                return

            self.location = _newLocation

