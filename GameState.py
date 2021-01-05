import pygame

import MapLoader

from Blocks import *
from Settings import *


class GameState():
    def __init__(self, units):
        self.worldSize = Vector2(WORLD_MAX_X, WORLD_MAX_Y)
        self.playerState = False  # 游戏状态，True表示获胜状态
        self.aliveState = True  # 控制状态，True表示场上仍有方块可以被控制
        self.units = units
        self.units.extend([GeneralBlock("NULL_BORDER", Vector2(x, -30)) for x in range(-30, 930, 30)])  # 上边界不会越界
        self.units.extend([GeneralBlock("NULL_BORDER", Vector2(x, 600)) for x in range(-30, 930, 30)])  # 下边界不会越界
        self.units.extend([GeneralBlock("NULL_BORDER", Vector2(-30, y)) for y in range(-30, 630, 30)])  # 左边界不会越界
        self.units.extend([GeneralBlock("NULL_BORDER", Vector2(900, y)) for y in range(-30, 630, 30)])  # 右边界不会越界

        self.isBlockList = []
        for unit in self.units:
            if unit.is_text() and unit.word == "is":
                self.isBlockList.append(unit)

        self.subjectBlockList = [
            BabaBlock("DEFAULT_BABA", Vector2(0, 0)),
            FlagBlock("DEFAULT_FLAG", Vector2(0, 0)),
            JellyBlock("DEFAULT_JELLY", Vector2(0, 0)),
            RockBlock("DEFAULT_ROCK", Vector2(0, 0)),
            SkullBlock("DEFAULT_SKULL", Vector2(0, 0)),
            WallBlock("DEFAULT_WALL", Vector2(0, 0)),
        ]
