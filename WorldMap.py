import pygame

from pygame.math import Vector2
from pygame.rect import Rect

from Blocks import *
from Settings import *


class GameState():
    def __init__(self):
        self.worldSize = Vector2(WORLD_MAX_X, WORLD_MAX_Y)
        self.units = [
            GeneralBlock(True, True, Vector2(100, 10), 'test.gif'),
            GeneralBlock(True, True, Vector2(300, 10), 'test.gif')
        ]

    def update(self, moveCommand):
        for unit in self.units:
            unit.move(moveCommand)

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
        self._gameState.update(self._moveCommand)

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
                    self._moveCommand.x = 29
                elif event.key == pygame.K_LEFT:
                    self._moveCommand.x = -29
                elif event.key == pygame.K_DOWN:
                    self._moveCommand.y = 29
                elif event.key == pygame.K_UP:
                    self._moveCommand.y = -29

    def _render_unit(self, unit):
        self._window.blit(unit.texture, unit.location, unit.rect)

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

ui = UserInterface()
ui.run()

pygame.quit()
