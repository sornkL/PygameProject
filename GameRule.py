import pygame

from typing import Union
from pygame.math import Vector2

from Blocks import *

class GameRuleObserver():
    def __init__(self, gameState):
        self._gameState = gameState

    def _is_exist(self, objectBlock: Union[GeneralBlock], direction: Vector2) -> Union[None, GeneralBlock]:
        """
        :param objectBlock: 某个特定的方块
        :param direction: 紧挨着object的方向
        :return: 返回object的direction方向是否有其他方块
                 除非返回None，否则返回一个特定block类型的数据，表示object在direction方向的方块信息
        """

        _newLocation = objectBlock.location + direction
        for unit in self._gameState.units:
            if unit.location == _newLocation:
                return unit
            else:
                continue

    def _observe(self, objectBlock: Union[GeneralBlock]) -> Union[list]:
        """
        :param objectBlock: 某个特定的方块
        :return: 按照"上下左右"的顺序返回被观察的方块四个方向上的方块数据，若某个方向上没有方块，则为None
        """

        blocksAroundList = []
        for direction in DIRECTION:
            blocksAroundList.append(self._is_exist(objectBlock, direction))

        return blocksAroundList
