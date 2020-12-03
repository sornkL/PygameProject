import pygame
from pygame.math import Vector2
from pygame.rect import Rect

class BaseBlock():
    def __init__(self, moveable: bool, controllable: bool, location: Vector2, texture: str, **kwargs):
        """
        :param moveable: 方块是否可以移动
        :param controllable: 方块是否可以被控制
        :param location: 方块的初始位置
        :param texture: 方块的贴图
        :param kwargs: 额外的参数
        """

        self._moveable = moveable
        self._controllable = controllable
        self.location = location
        self.texture = pygame.image.load(texture)
        self.rect = self.texture.get_rect()
        # self.location = Vector2(int(self.rect.centerx), int(self.rect.centery))

    def _is_move(self) -> bool:
        """

        :return: 返回方块是否可以移动
        """
        if self._moveable:  # 可以移动
            return True
        else:
            return False

    def _is_control(self) -> bool:
        """

        :return: 返回方块是否可以被控制
        """
        if self._controllable:
            return True
        else:
            return False

    def move(self, direction: Vector2):
        """
        :param direction: 方块移动方向，Vector(x, y)
        """
        raise NotImplementedError

