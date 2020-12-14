import pygame

import Map1

from pygame.math import Vector2
from pygame.rect import Rect

from Blocks import *
from GameRule import GameRuleObserver
from GameState import *
from Settings import *


class UserInterface():
    def __init__(self):
        pygame.init()
        self._gameState = GameState(Map1.units)
        self._cellSize = Vector2(CELL_SIZE_X, CELL_SIZE_Y)
        _windowSize = self._gameState.worldSize.elementwise() * self._cellSize
        self._window = pygame.display.set_mode((int(_windowSize.x), int(_windowSize.y)))
        self._clock = pygame.time.Clock()
        self._running = True
        self._moveCommand = Vector2(0, 0)

    def _update(self):
        testObserver = GameRuleObserver(self._gameState)
        testObserver.endow(self._gameState.isBlockList)
        for unit in self._gameState.units:
            if unit.is_control():
                testObserver._move(unit, self._moveCommand)
            if testObserver._is_win(self._gameState.units):
                print("Victory")


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
