import pygame

from Settings import *

from pygame.math import Vector2
from pygame.rect import Rect
from pygame.sprite import AbstractGroup
from typing import Union


class BaseBlock(pygame.sprite.Sprite):
    def __init__(self, id: str, text: bool, moveable: bool, controllable: bool, location: Vector2, texture: str, *groups: AbstractGroup):
        """
        :param id: 每个关卡方块的唯一编号
        :param text: 方块是否是语法方块
        :param moveable: 方块是否可以移动
        :param controllable: 方块是否可以被控制
        :param location: 方块的初始位置
        :param texture: 方块的贴图
        """

        super().__init__(*groups)
        self._id = id
        self._text = text
        self._moveable = moveable
        self._controllable = controllable
        self.location = location
        self.texture = pygame.image.load(texture)
        # self.rect = self.texture.get_rect()
        # self.rect.top, self.rect.bottom = self.location.x, self.location.y
        # self.location = Vector2(int(self.rect.centerx), int(self.rect.centery))
        self.rect = Rect(self.location.x, self.location.y, CELL_SIZE_X, CELL_SIZE_Y)

    def is_move(self) -> bool:
        """
        :return: 返回方块是否可以移动
        """

        return self._moveable

    def is_control(self) -> bool:
        """
        :return: 返回方块是否可以被控制
        """

        return self._controllable

    def _is_collide(self, group: pygame.sprite.Group) -> bool:
        """
        :param group: 传入一个不可移动的Sprite Group用以碰撞检测
        :return: 返回当前控制的方块是否碰撞了不可移动的方块
        """

        return pygame.sprite.spritecollide(self, group, False)

    def move(self, direction: Vector2, group):
        """
        :param direction: 方块移动方向，Vector(x, y)
        """

        if self.is_move() and self.is_control():
            self.location += direction
            self.rect = Rect(self.location.x, self.location.y, CELL_SIZE_X, CELL_SIZE_Y)

            if self.location.x < 0 or self.location.x >= WORLD_MAX_X*CELL_SIZE_X or self.location.y < 0 \
                    or self.location.y >= WORLD_MAX_Y*CELL_SIZE_Y \
                    or self._is_collide(group):
                self.location -= direction
                self.rect = Rect(self.location.x, self.location.y, CELL_SIZE_X, CELL_SIZE_Y)

