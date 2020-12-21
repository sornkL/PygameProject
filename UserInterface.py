import pygame

from pygame.math import Vector2
from pygame.rect import Rect

from Blocks import *
from MapLoader import *
from GameRule import GameRuleObserver
from GameState import *
from Settings import *


class UserInterface():
    def __init__(self, map):
        # pygame.init()
        self._map = map
        self.worldSize = Vector2(WORLD_MAX_X, WORLD_MAX_Y)
        self._cellSize = Vector2(CELL_SIZE_X, CELL_SIZE_Y)
        _windowSize = self.worldSize.elementwise() * self._cellSize
        self._window = pygame.display.set_mode((int(_windowSize.x), int(_windowSize.y)))
        self._gameState = GameState(self._map.load_map())
        self._clock = pygame.time.Clock()
        self._running = True
        self._moveCommand = Vector2(0, 0)

    def check_win_state(self):
        return self._gameState.playerState

    def check_lose_state(self):
        return not self._gameState.aliveState

    def _update(self):
        testObserver = GameRuleObserver(self._gameState)
        for i in range(len(self._gameState.units)):
            if self._gameState.units[i].is_text():
                self._gameState.units[i].texture.set_alpha(ALPHA)
        testObserver.endow(self._gameState.isBlockList)
        testObserver.transform(self._gameState.isBlockList)

        if self._gameState.playerState:
            self._running = False
        if testObserver.is_win(self._gameState.isBlockList):
            self._gameState.playerState = True
        if testObserver.is_lose(self._gameState.units):
            self._gameState.aliveState = False

        for unit in self._gameState.units:
            if unit.is_control():
                testObserver.move(unit, self._moveCommand)

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
                elif event.key == pygame.K_r:
                    self._gameState = GameState(self._map.load_map())
                elif event.key == pygame.K_SPACE:
                    self._running = False
                    break

    def _render_unit(self, unit):
        unit.cartoon()
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
    pygame.init()
    map = MapHell()
    ui = UserInterface(map)  # 加载地图
    ui.run()

    pygame.quit()
