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
            GeneralBlock("test01", True, True, Vector2(420, 300), 'pics/baba_0_1.png'),
            #GeneralBlock("test02", False, True, Vector2(90, 0), 'pics/blue_test.png'),
            #GeneralBlock("test03", False, True, Vector2(60, 0), 'pics/white_test.png'),
            #GeneralBlock("test04", False, True, Vector2(60, 60), 'pics/white_test.png'),
            #GeneralBlock("test04", False, True, Vector2(120, 60), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(240, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(270, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(300, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(330, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(360, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(390, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(420, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(450, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(480, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(510, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(540, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(570, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(600, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(630, 210), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(240, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(270, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(300, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(330, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(360, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(390, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(420, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(450, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(480, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(510, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(540, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(570, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(600, 330), 'pics/white_test.png'),
            GeneralBlock("test04", False, True, Vector2(630, 330), 'pics/white_test.png'),
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