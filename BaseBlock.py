import pygame

from Settings import *

from pygame.math import Vector2
from pygame.rect import Rect
from pygame.sprite import AbstractGroup


class BaseBlock(pygame.sprite.Sprite):
    def __init__(self, moveable: bool, controllable: bool, location: Vector2, texture: str, *groups: AbstractGroup,
                 **kwargs):
        """
        :param moveable: 方块是否可以移动
        :param controllable: 方块是否可以被控制
        :param location: 方块的初始位置
        :param texture: 方块的贴图
        :param kwargs: 额外的参数
        """

        super().__init__(*groups)
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

        raise NotImplementedError

    def move(self, direction: Vector2, group):
        """
        :param direction: 方块移动方向，Vector(x, y)
        """

        raise NotImplementedError

