import pygame
import sys

from GameState import *
from MapLoader import *
from UserInterface import *

mapMainMenu = MapMainMenu()
mapStart = MapStart()
map1 = Map1()
map2 = Map2()
map3 = Map3()
map4 = Map4()
map5 = Map5()
map6 = Map6()
mapHard = MapHard()
mapHell = MapHell()
choices = [mapMainMenu, map1, map2, map3]

running = True

while running:
    pygame.init()
    ui = UserInterface(mapMainMenu)
    ui.run()
    mapChoice = 0

    if ui.check_win_state():
        for unit in ui._gameState.units:
            if unit.is_control():
                if unit.location == Vector2(330, 30):
                    mapChoice = 1
                elif unit.location == Vector2(420, 30):
                    mapChoice = 2
                elif unit.location == Vector2(510, 30):
                    mapChoice = 3
                elif unit.location == Vector2(600, 90):
                    running = False

        if not running:
            break
        ui = UserInterface(choices[mapChoice])
        ui.run()

pygame.quit()
