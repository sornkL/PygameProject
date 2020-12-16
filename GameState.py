import pygame

import MapLoader

from Blocks import *
from Settings import *

class GameState():
    def __init__(self, units):
        self.worldSize = Vector2(WORLD_MAX_X, WORLD_MAX_Y)
        self.playerState = False  # 游戏状态，True表示获胜状态
        self.units = units

        self.isBlockList = []
        for unit in self.units:
            if unit.is_text() and unit.word == "is":
                self.isBlockList.append(unit)

        self.subjectBlockList = []
        for subjectBlock in self.units:
            if not subjectBlock._text:
                self.subjectBlockList.append(subjectBlock)