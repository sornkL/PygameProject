import pygame

from pygame.rect import Rect
from pygame.math import Vector2

from BaseBlock import BaseBlock
from Settings import *


class GeneralBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, text=False, moveable=False, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = False
        self._controllable = False
        self._moveable = False
        self.texture = pygame.image.load("pics/black.png")


class BabaBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2):
        self.id = id
        self._text = False
        self._moveable = True
        self._controllable = False
        self._passable = True
        self.location = location
        self.textureLeft = pygame.image.load('pics/baba_18_1.png')
        self.textureRight = pygame.image.load('pics/baba_0_1.png')
        self.textureUp = pygame.image.load('pics/baba_7_1.png')
        self.textureDown = pygame.image.load('pics/baba_26_2.png')
        self.texture = self.textureRight
        self.transparentTexture = pygame.image.load('pics/baba_18_1.png').convert_alpha()
        self.transparentTexture.set_alpha(ALPHA)

    def cartoon(self):
        """
        对于无动画效果的方块，当其可以通过时，将不透明度调低
        :return:
        """
        if not self.is_control():
            if self.is_pass():
                self.texture = self.transparentTexture
            else:
                self.texture = self.textureLeft

    def change_direction(self, direction: Vector2):
        """
        改变不同方向对应的贴图
        :param direction: 移动方向
        :return: 无返回值
        """
        if direction.x == 0:
            pass
        elif direction.x > 0:
            self.texture = self.textureRight
        else:
            self.texture = self.textureLeft
        if direction.y == 0:
            pass
        elif direction.y > 0:
            self.texture = self.textureDown
        else:
            self.texture = self.textureUp


class FlagBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        self.id = id
        self._text = False
        self._moveable = moveable
        self._controllable = controllable
        self.location = location
        self._passable = passable
        self.textureList = [pygame.image.load('pics/flag_1.png'), pygame.image.load('pics/flag_2.png'), pygame.image.load('pics/flag_3.png')]
        self.texture = self.textureList[0]
        pic1 = pygame.image.load('pics/flag_1.png').convert_alpha()
        pic2 = pygame.image.load('pics/flag_2.png').convert_alpha()
        pic3 = pygame.image.load('pics/flag_3.png').convert_alpha()
        pic1.set_alpha(ALPHA)
        pic2.set_alpha(ALPHA)
        pic3.set_alpha(ALPHA)
        self.transparentTextureList = [pic1, pic2, pic3]
        self.rect = Rect(self.location.x, self.location.y, CELL_SIZE_X, CELL_SIZE_Y)
        self.frame = 0
        self.list = self.textureList

    def cartoon(self):
        """
        对于有动画效果的方块，当其可以通过时，将不透明度调低
        :return:
        """
        frame = 30
        if not self.is_pass() or self.is_control():
            self.list = self.textureList
        else:
            self.list = self.transparentTextureList

        if self.frame < frame:
            self.texture = self.list[self.frame // 10]
            self.frame += 1

        else:
            self.frame = 0


class SkullBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, text=False, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.textureList = [pygame.image.load('pics/skull_0_1.png'), pygame.image.load('pics/skull_0_2.png'),
                            pygame.image.load('pics/skull_0_3.png')]
        pic1 = pygame.image.load('pics/skull_0_1.png').convert_alpha()
        pic2 = pygame.image.load('pics/skull_0_2.png').convert_alpha()
        pic3 = pygame.image.load('pics/skull_0_3.png').convert_alpha()
        pic1.set_alpha(ALPHA)
        pic2.set_alpha(ALPHA)
        pic3.set_alpha(ALPHA)
        self.transparentTextureList = [pic1, pic2, pic3]
        self.frame = 0
        self.list = self.textureList

    def cartoon(self):
        """
        对于有动画效果的方块，当其可以通过时，将不透明度调低
        :return:
        """
        frame = 60
        if not self.is_pass() or self.is_control():
            self.list = self.textureList
        else:
            self.list = self.transparentTextureList

        if self.frame < frame:
            self.texture = self.list[self.frame // 20]
            self.frame += 1
        else:
            self.frame = 0


class RockBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.textureList = [pygame.image.load('pics/rock_0_1.png'), pygame.image.load('pics/rock_0_2.png'),
                            pygame.image.load('pics/rock_0_3.png')]
        pic1 = pygame.image.load('pics/rock_0_1.png').convert_alpha()
        pic2 = pygame.image.load('pics/rock_0_2.png').convert_alpha()
        pic3 = pygame.image.load('pics/rock_0_3.png').convert_alpha()
        pic1.set_alpha(ALPHA)
        pic2.set_alpha(ALPHA)
        pic3.set_alpha(ALPHA)
        self.transparentTextureList = [pic1, pic2, pic3]
        self.frame = 0
        self.list = self.textureList

    def cartoon(self):
        """
        对于有动画效果的方块，当其可以通过时，将不透明度调低
        :return:
        """
        frame = 60
        if not self.is_pass() or self.is_control():
            self.list = self.textureList
        else:
            self.list = self.transparentTextureList

        if self.frame < frame:
            self.texture = self.list[self.frame // 20]
            self.frame += 1
        else:
            self.frame = 0


class WallBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2 ,moveable=False, controllable=False, passable=True):
        super().__init__(id,location,passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.frame = 0
        color = WALL_COLOR
        if color =='black':
            self.textureList = [pygame.image.load('pics/wall_black_1.png'), pygame.image.load('pics/wall_black_2.png'),
                                pygame.image.load('pics/wall_black_3.png')]
            pic1 = pygame.image.load('pics/wall_black_1.png').convert_alpha()
            pic2 = pygame.image.load('pics/wall_black_2.png').convert_alpha()
            pic3 = pygame.image.load('pics/wall_black_3.png').convert_alpha()
            pic1.set_alpha(ALPHA)
            pic2.set_alpha(ALPHA)
            pic3.set_alpha(ALPHA)
            self.transparentTextureList = [pic1, pic2, pic3]
            self.list = self.textureList
        elif color =='purple':
            self.textureList = [pygame.image.load('pics/wall_purple_1.png'), pygame.image.load('pics/wall_purple_2.png'),
                                pygame.image.load('pics/wall_purple_3.png')]
            pic1 = pygame.image.load('pics/wall_purple_1.png').convert_alpha()
            pic2 = pygame.image.load('pics/wall_purple_2.png').convert_alpha()
            pic3 = pygame.image.load('pics/wall_purple_3.png').convert_alpha()
            pic1.set_alpha(ALPHA)
            pic2.set_alpha(ALPHA)
            pic3.set_alpha(ALPHA)
            self.transparentTextureList = [pic1, pic2, pic3]
            self.list = self.textureList
        elif color == 'red':
            self.textureList = [pygame.image.load('pics/wall_red_1.png'), pygame.image.load('pics/wall_red_2.png'),
                                pygame.image.load('pics/wall_red_3.png')]
            pic1 = pygame.image.load('pics/wall_red_1.png').convert_alpha()
            pic2 = pygame.image.load('pics/wall_red_2.png').convert_alpha()
            pic3 = pygame.image.load('pics/wall_red_3.png').convert_alpha()
            pic1.set_alpha(ALPHA)
            pic2.set_alpha(ALPHA)
            pic3.set_alpha(ALPHA)
            self.transparentTextureList = [pic1, pic2, pic3]
            self.list = self.textureList

    def cartoon(self):
        """
        对于有动画效果的方块，当其可以通过时，将不透明度调低
        :return:
        """
        frame = 90
        if not self.is_pass() or self.is_control():
            self.list = self.textureList
        else:
            self.list = self.transparentTextureList

        if self.frame < frame:
            self.texture = self.list[self.frame // 30]
            self.frame += 1
        else:
            self.frame = 0


class JellyBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.textureList = [pygame.image.load('pics/jelly_0_1.png'), pygame.image.load('pics/jelly_0_2.png'),
                            pygame.image.load('pics/jelly_0_3.png')]
        pic1 = pygame.image.load('pics/jelly_0_1.png').convert_alpha()
        pic2 = pygame.image.load('pics/jelly_0_2.png').convert_alpha()
        pic3 = pygame.image.load('pics/jelly_0_3.png').convert_alpha()
        pic1.set_alpha(ALPHA)
        pic2.set_alpha(ALPHA)
        pic3.set_alpha(ALPHA)
        self.transparentTextureList = [pic1, pic2, pic3]
        self.frame = 0
        self.list = self.textureList

    def cartoon(self):
        """
        对于有动画效果的方块，当其可以通过时，将不透明度调低
        :return:
        """
        frame = 60
        if not self.is_pass() or self.is_control():
            self.list = self.textureList
        else:
            self.list = self.transparentTextureList

        if self.frame < frame:
            self.texture = self.list[self.frame // 20]
            self.frame += 1
        else:
            self.frame = 0


class DoorBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.textureList = [pygame.image.load('pics/door_0_1.png'), pygame.image.load('pics/door_0_2.png'),
                            pygame.image.load('pics/door_0_3.png')]
        pic1 = pygame.image.load('pics/door_0_1.png').convert_alpha()
        pic2 = pygame.image.load('pics/door_0_2.png').convert_alpha()
        pic3 = pygame.image.load('pics/door_0_3.png').convert_alpha()
        pic1.set_alpha(ALPHA)
        pic2.set_alpha(ALPHA)
        pic3.set_alpha(ALPHA)
        self.transparentTextureList = [pic1, pic2, pic3]
        self.frame = 0
        self.list = self.textureList

    def cartoon(self):
        """
        对于有动画效果的方块，当其可以通过时，将不透明度调低
        :return:
        """
        frame = 60
        if not self.is_pass() or self.is_control():
            self.list = self.textureList
        else:
            self.list = self.transparentTextureList

        if self.frame < frame:
            self.texture = self.list[self.frame // 20]
            self.frame += 1
        else:
            self.frame = 0


class KeyBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.textureList = [pygame.image.load('pics/key_0_1.png'), pygame.image.load('pics/key_0_2.png'),
                            pygame.image.load('pics/key_0_3.png')]
        pic1 = pygame.image.load('pics/key_0_1.png').convert_alpha()
        pic2 = pygame.image.load('pics/key_0_2.png').convert_alpha()
        pic3 = pygame.image.load('pics/key_0_3.png').convert_alpha()
        pic1.set_alpha(ALPHA)
        pic2.set_alpha(ALPHA)
        pic3.set_alpha(ALPHA)
        self.transparentTextureList = [pic1, pic2, pic3]
        self.frame = 0
        self.list = self.textureList

    def cartoon(self):
        """
        对于有动画效果的方块，当其可以通过时，将不透明度调低
        :return:
        """
        frame = 60
        if not self.is_pass() or self.is_control():
            self.list = self.textureList
        else:
            self.list = self.transparentTextureList

        if self.frame < frame:
            self.texture = self.list[self.frame // 20]
            self.frame += 1
        else:
            self.frame = 0


class FireBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/fire.png')


class PillarBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/pillar.png')


class Block1(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/number_1.png')


class Block2(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/number_2.png')


class Block3(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/number_3.png');


class Block4(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/number_4.png');


class Block5(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/number_5.png');


class Block6(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/number_6.png');


class Block7(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/number_7.png');


class Block8(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/number_8.png');


class Block9(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/number_9.png');


class Block0(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/number_0.png');


class Blockquit(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/quit.png');


class Blockabout(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/about.png');


class Blockwasd(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/move_.png');


class Blockmove(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/text_move_0_1.png');


class TileBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/tile_0_2.png').convert_alpha()
        self.texture.set_alpha(ALPHA)


class BrickBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/brick_0_1.png')


class RobotBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = True
        self._controllable = False
        self._moveable = True
        self._text = False
        self.texture = pygame.image.load('pics/robot.png')


class YouVerbBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'you'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_you_0_1.png')

    def cartoon(self):
        pass


class HotVerbBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'hot'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_hot_0_2.png')


class StopVerbBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'stop'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_stop_0_1.png')


class PushVerbBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'push'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_push_0_1.png')


class WinVerbBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'win'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_win_0_1.png')


class DefeatVerbBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'defeat'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_defeat_0_1.png')


class MeltVerbBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'melt'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_melt_0_1.png')


class WeakVerbBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'weak'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_weak_0_1.png')


class OpenVerbBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False,passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'open'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_open_0_1.png')


class ShutVerbBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False,passable=False):
        super().__init__(id,location,passable, moveable, controllable)
        self.word = 'shut'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_shut_0_1.png')


class IsBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False,passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'is'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_is_0_1.png')


class BabaNounBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False,passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'baba'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_baba_0_1.png')


class RockNounBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False,passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'rock'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_rock_0_1.png')


class SkullNounBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False,passable=False):
        super().__init__(id,location,passable, moveable, controllable)
        self.word = 'skull'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_skull_0_1.png')


class WallNounBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'wall'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_wall_0_1.png')


class FlagNounBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False, passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'flag'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.texture = pygame.image.load('pics/text_flag_0_1.png')


class JellyNounBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False,passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'jelly'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_jelly_0_1.png')


class KeyNounBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False,passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'key'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_key_0_1.png')


class DoorNounBlock(BaseBlock):
    def __init__(self, id: str, location: Vector2, moveable=True, controllable=False,passable=False):
        super().__init__(id, location, passable, moveable, controllable)
        self.word = 'door'
        self._passable = False
        self._controllable = False
        self._moveable = True
        self._text = True
        self.transparent = False
        self.texture = pygame.image.load('pics/text_door_0_1.png')


class AboutPicture(BaseBlock):
    def __init__(self, id: str, location: Vector2, text=False, moveable=False, controllable=False, passable=True):
        super().__init__(id, location, passable, moveable, controllable)
        self._passable = False
        self._controllable = False
        self._moveable = False
        self._text = False
        self.texture = pygame.image.load("pics/about_page_info.png")
