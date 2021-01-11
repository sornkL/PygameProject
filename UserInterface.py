import copy
import pygame

from pygame.math import Vector2
from pygame.rect import Rect

from Blocks import *
from MapLoader import *
from GameRule import GameRuleObserver
from GameState import *
from Settings import *
from StatisticsReader import *


class UserInterface():
    def __init__(self, map):
        # pygame.init()
        self._map = map
        self.worldSize = Vector2(WORLD_MAX_X, WORLD_MAX_Y)
        self._cellSize = Vector2(CELL_SIZE_X, CELL_SIZE_Y)
        _windowSize = self.worldSize.elementwise() * self._cellSize
        self._window = pygame.display.set_mode((int(_windowSize.x), int(_windowSize.y)))
        pygame.display.set_caption(GAME_TITLE + " - " + str(type(map).__name__))
        self._gameState = GameState(self._map.load_map())
        self._clock = pygame.time.Clock()
        self._running = True
        self._moveCommand = Vector2(0, 0)
        self._isCountSign = False
        self._loadingPicture = pygame.image.load(self._map.load_picture())
        self._countdown_time = COUNTDOWN

        if type(self._map) == MapMainMenu:
            pygame.mixer.music.load("music/menu.ogg")
        elif type(self._map) == MapAbout:
            pygame.mixer.music.load("music/map.ogg")
        else:
            pygame.mixer.music.load("music/garden.ogg")
        pygame.mixer.music.play(-1)

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
            if not self._isCountSign \
                    and type(self._map).__name__ != "MapMainMenu" \
                    and type(self._map).__name__ != "MapAbout":
                winCountList = check_win_count(STATISTICS_FILE_PATH)
                mapId = int(type(self._map).__name__.split('Map')[1]) - 1
                update_win_count(STATISTICS_FILE_PATH, type(self._map).__name__)
                if winCountList[mapId] == 0:
                    update_first_win_time(STATISTICS_FILE_PATH, type(self._map).__name__)
                self._isCountSign = True
        if testObserver.is_lose(self._gameState.units):
            self._gameState.aliveState = False
            if not self._isCountSign \
                    and type(self._map).__name__ != "MapMainMenu" \
                    and type(self._map).__name__ != "MapAbout":
                update_lose_count(STATISTICS_FILE_PATH, type(self._map).__name__)
                self._isCountSign = True

        for unit in self._gameState.units:
            if unit.is_control() and self._moveCommand != Vector2(0, 0):
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
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self._moveCommand = RIGHT_DIRECTION
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self._moveCommand = LEFT_DIRECTION
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self._moveCommand = BOTTOM_DIRECTION
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self._moveCommand = TOP_DIRECTION
                elif event.key == pygame.K_r:
                    self._gameState = GameState(self._map.load_map())
                    self._isCountSign = False
                elif event.key == pygame.K_SPACE:
                    self._running = False
                    break

    def _loading(self):
        while self._countdown_time > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    self._countdown_time = 0
            self._window.blit(self._loadingPicture, Vector2(0, 0))
            self._window.blit(pygame.image.load("pics/anykey.png"), Vector2(380, 500))
            if type(self._map).__name__ != "MapMainMenu" and type(self._map).__name__ != "MapAbout":
                self._render_unit(FlagBlock("WIN_COUNT_FLAG", Vector2(2, 0), passable=False))
                self._window.blit(pygame.image.load("pics/text_win_count.png"), Vector2(30, 0))
                self._window.blit(pygame.image.load("pics/icon_skull.png"), Vector2(2, 30))
                self._window.blit(pygame.image.load("pics/text_lose_count.png"), Vector2(30, 30))
                self._window.blit(pygame.image.load("pics/icon_clock.png"), Vector2(2, 60))
                self._window.blit(pygame.image.load("pics/text_time_win.png"), Vector2(30, 60))
                statistics_display(self._window, int(type(self._map).__name__.split("Map")[1])-1)
            pygame.display.update()
            self._countdown_time -= 1

    def _render_unit(self, unit):
        unit.cartoon()
        self._window.blit(unit.texture, unit.location)

    def _render(self):
        self._window.fill(BACKGROUND_COLOR)  # 黑色背景

        for unit in self._gameState.units:
            self._render_unit(unit)
        if not self._gameState.aliveState:
            self._window.blit(pygame.image.load("pics/R.png"), Vector2(200, 12))
            self._window.blit(pygame.image.load("pics/button_restart_0_1.png"), Vector2(230, -3))
            self._window.blit(pygame.image.load("pics/space.png"), Vector2(500, 0))
            self._window.blit(pygame.image.load("pics/main_menu.png"), Vector2(595, -1))
        pygame.display.update()

    def run(self):
        while self._running:
            self._process_input()
            self._loading()
            self._update()
            self._render()
            self._clock.tick(60)


if __name__ == '__main__':
    mapTemp = Map9()
    pygame.init()
    ui = UserInterface(mapTemp)
    ui.run()
    pygame.quit()
