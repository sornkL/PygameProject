import pygame

from pygame.math import Vector2
from pygame.rect import Rect

from Blocks import *
from GameRule import GameRuleObserver
from Settings import *


class GameState():
    def __init__(self):
        self.worldSize = Vector2(WORLD_MAX_X, WORLD_MAX_Y)
        self.playerState = False  # 游戏状态，True表示获胜状态
        self.units = [
            GeneralBlock("test01", False, True, True, Vector2(360, 270), 'pics/baba_0_1.png'),

            GeneralBlock("test04", False, False, True, Vector2(240, 210), 'pics/wall_1_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(270, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(300, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(330, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(390, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(420, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(450, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(480, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(510, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(540, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(600, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(630, 210), 'pics/wall_4_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(240, 330), 'pics/wall_1_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(270, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(300, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(330, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(390, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(420, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(450, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(480, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(510, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(540, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(600, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, False, True, Vector2(630, 330), 'pics/wall_4_1.png'),

            GeneralBlock("test04", False, True, False, Vector2(510, 300), 'pics/rock_0_1.png'),
            GeneralBlock("test04", False, True, False, Vector2(510, 270), 'pics/rock_0_1.png'),
            GeneralBlock("test04", False, True, False, Vector2(510, 240), 'pics/rock_0_1.png'),

            GeneralBlock("test04", False, True, False, Vector2(570, 270), 'pics/flag_0_1.png'),

            BabaNounBlock("test03", True, True, False, Vector2(270, 150), 'pics/text_baba_0_1.png', 'baba'),
            IsBlock("test05", True, True, False, Vector2(300, 150), 'pics/text_is_0_1.png', 'is'),
            YouVerbBlock("test05", True, True, False, Vector2(330, 150), 'pics/text_you_0_1.png', 'you'),

            StoneNounBlock("test03", True, True, False, Vector2(540, 150), 'pics/text_rock_0_1.png', 'stone'),
            IsBlock("test05", True, True, False, Vector2(570, 150), 'pics/text_is_0_1.png', 'is'),
            PushVerbBlock("test06", True, True, False, Vector2(600, 150), 'pics/text_push_0_1.png', 'push'),

            WallNounBlock("test03", True, True, False, Vector2(270, 390), 'pics/text_wall_0_1.png', 'wall'),
            IsBlock("test05", True, True, False, Vector2(300, 390), 'pics/text_is_0_1.png', 'is'),
            StopVerbBlock("test06", True, True, False, Vector2(330, 390), 'pics/text_stop_0_1.png', 'stop'),

            FlagNounBlock("test03", True, True, False, Vector2(540, 390), 'pics/text_flag_0_1.png', 'flag'),
            IsBlock("test05", True, True, False, Vector2(570, 390), 'pics/text_is_0_1.png', 'is'),
            WinVerbBlock("test06", True, True, False, Vector2(600, 390), 'pics/text_win_0_1.png', 'win'),
        ]

        self.isBlockList = []
        for unit in self.units:
            if unit._text and unit.word == "is":
                self.isBlockList.append(unit)


class UserInterface():
    def __init__(self):
        pygame.init()
        self._gameState = GameState()
        self._cellSize = Vector2(CELL_SIZE_X, CELL_SIZE_Y)
        _windowSize = self._gameState.worldSize.elementwise() * self._cellSize
        self._window = pygame.display.set_mode((int(_windowSize.x), int(_windowSize.y)))
        self._clock = pygame.time.Clock()
        self._running = True
        self._moveCommand = Vector2(0, 0)

    def _update(self):
        for unit in self._gameState.units:
            testObserver = GameRuleObserver(self._gameState)

            if unit.is_control():
                testObserver._move(unit, self._moveCommand)
            if testObserver._is_win(self._gameState.units):
                print("Victory")

            '''
            test = GameRuleObserver(self._gameState)
            if unit._id == "testIs":
                print(test._is_win(self._gameState.isBlockList))
            '''


    def _process_input(self):
        self._moveCommand = Vector2(0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    self._running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self._moveCommand = RIGHT_DIRECTION
                elif event.key == pygame.K_LEFT:
                    self._moveCommand = LEFT_DIRECTION
                elif event.key == pygame.K_DOWN:
                    self._moveCommand = BOTTOM_DIRECTION
                elif event.key == pygame.K_UP:
                    self._moveCommand = TOP_DIRECTION

    def _render_unit(self, unit):
        self._window.blit(unit.texture, unit.location)

    def _render(self):
        self._window.fill(BACKGROUND_COLOR)  # 黑色背景

        for unit in self._gameState.units:
            self._render_unit(unit)

        pygame.display.update()

    def run(self):
        while self._running:
            self._process_input()
            self._update()
            self._render()
            self._clock.tick(60)


if __name__ == '__main__':
    ui = UserInterface()
    ui.run()

    pygame.quit()
