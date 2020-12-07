import pygame
from pygame._sprite import AbstractGroup
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

class HotVerbBlock(BaseBlock):
    def __init__(self, id: str, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 *groups: AbstractGroup,word: str):
        super().__init__(id,moveable,controllable,location,texture,*groups)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(melt) -> defeat'''

class StopVerbBlock(BaseBlock):
    def __init__(self, id: str, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 *groups: AbstractGroup,word: str):
        super().__init__(id,moveable,controllable,location,texture,*groups)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(block) -> block.moveable = False'''

class PushVerbBlock(BaseBlock):
    def __init__(self, id: str, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 *groups: AbstractGroup, word: str):
        super().__init__(id, moveable, controllable, location, texture, *groups)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(block) -> block.moveable = True'''

class WinVerbBlock(BaseBlock):
    def __init__(self, id: str, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 *groups: AbstractGroup, word: str):
        super().__init__(id, moveable, controllable, location, texture, *groups)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(touch) -> win'''

class DefeatVerbBlock(BaseBlock):
    def __init__(self, id: str, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 *groups: AbstractGroup, word: str):
        super().__init__(id, moveable, controllable, location, texture, *groups)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(touch) -> defeat'''

class MeltVerbBlock(BaseBlock):
    def __init__(self, id: str, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 *groups: AbstractGroup, word: str):
        super().__init__(id, moveable, controllable, location, texture, *groups)
        self.word = word
        self._controllable = False
        self.moveable = True
    '''if(touch -> hot) -> defeat'''

#class SinkVerbBlock(BaseBlock):