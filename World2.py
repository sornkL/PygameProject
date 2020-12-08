import pygame

from pygame.math import Vector2
from pygame.rect import Rect

from Blocks import *
from GameRule import GameRuleObserver
from Settings import *

class GameStateWorldOne():
    def __init__(self):
        self.worldSize = Vector2(WORLD_MAX_X, WORLD_MAX_Y)
        self.units = [
            GeneralBlock("test01", False, True, True,  Vector2(510, 420), 'pics/wall_0_1.png'),

            GeneralBlock("test04", False, False, True, Vector2(240, 210), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(270, 210), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(300, 210), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(330, 210), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 210), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 180), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 150), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 120), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 90), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(390, 90), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(420, 90), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(450, 90), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(480, 90), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(510, 90), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(540, 90), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 90), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 120), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 150), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 180), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 210), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 240), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 270), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 300), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 360), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 390), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 420), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 450), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(570, 480), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(540, 480), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(510, 480), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(480, 480), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(480, 510), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(450, 510), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(420, 510), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(390, 510), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 510), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 480), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 450), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 420), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 390), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 360), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(360, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(330, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(300, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(270, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(240, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(240, 300), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(240, 270), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(240, 240), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(390, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(420, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(450, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(480, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(510, 330), 'pics/flag_0_1.png'),
            GeneralBlock("test04", False, False, True, Vector2(540, 330), 'pics/flag_0_1.png'),

            WallNounBlock("test03", True, True, False, Vector2(270, 390), 'pics/text_wall_0_1.png', 'wall'),
            IsBlock("test05", True, True, False, Vector2(270, 420), 'pics/text_is_0_1.png', 'is'),
            YouVerbBlock("test05", True, True, False, Vector2(270, 450), 'pics/text_you_0_1.png', 'you'),

            FlagNounBlock("test03", True, True, False, Vector2(420, 390), 'pics/text_flag_0_1.png', 'flag'),
            IsBlock("test05", True, True, False, Vector2(420, 420), 'pics/text_is_0_1.png', 'is'),
            StopVerbBlock("test06", True, True, False, Vector2(420, 450), 'pics/text_stop_0_1.png', 'stop'),

            WinVerbBlock("test06", True, True, False, Vector2(510, 210), 'pics/text_win_0_1.png', 'win'),

            BabaNounBlock("test03", True, True, False, Vector2(300, 270), 'pics/text_baba_0_1.png', 'baba'),
            IsBlock("test05", True, True, False, Vector2(420, 150), 'pics/text_is_0_1.png', 'is'),
        ]
        self.collideCheckGroup = pygame.sprite.Group()
        for unit in self.units:
            if not unit.is_move():
                self.collideCheckGroup.add(unit)

    def update_move(self, moveCommand, moveTarget):
        for unit in self.units:
            if unit == moveTarget:
                unit.move(moveCommand, self.collideCheckGroup)



class UserInterface():
    def __init__(self):
        pygame.init()
        self._gameState = GameStateWorldOne()
        self._cellSize = Vector2(CELL_SIZE_X, CELL_SIZE_Y)
        _windowSize = self._gameState.worldSize.elementwise() * self._cellSize
        self._window = pygame.display.set_mode((int(_windowSize.x), int(_windowSize.y)))
        self._clock = pygame.time.Clock()
        self._running = True
        self._moveCommand = Vector2(0, 0)

    def _update(self):
        for unit in self._gameState.units:
            self._gameState.update_move(self._moveCommand, unit)

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
                    self._moveCommand.x = CELL_SIZE_X
                elif event.key == pygame.K_LEFT:
                    self._moveCommand.x = -CELL_SIZE_X
                elif event.key == pygame.K_DOWN:
                    self._moveCommand.y = CELL_SIZE_X
                elif event.key == pygame.K_UP:
                    self._moveCommand.y = -CELL_SIZE_X

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