import pygame
from pygame.rect import Rect
from pygame.math import Vector2

from BaseBlock import BaseBlock
from pygame.sprite import AbstractGroup

from Settings import *


class GeneralBlock(BaseBlock):
    pass


class TestBlock(BaseBlock):
    pass


class GeneralVerbBlock(BaseBlock):
    def __init__(self, id: str, text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str, *groups: AbstractGroup):
        super().__init__(id, text, moveable, controllable, location, texture, *groups)
        self._word = word


class IsBlock(BaseBlock):
    def __init__(self, id: str, text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str, *groups: AbstractGroup):
        super().__init__(id, text, moveable, controllable, location, texture, *groups)
        self._word = word


class GeneralNounBlock(BaseBlock):
    def __init__(self, id: str, text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str,
                 word: str, *groups: AbstractGroup):
        super().__init__(id, text, moveable, controllable, location, texture, *groups)
        self._word = word




