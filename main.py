import pygame
import sys

from GameState import *
from MapLoader import *
from UserInterface import *

mapAbout = MapAbout()
mapMainMenu = MapMainMenu()
map1 = Map1()
map2 = Map2()
map3 = Map3()
map4 = Map4()
map5 = Map5()
map6 = Map6()
map7 = Map7()
choices = [mapMainMenu, map1, map2, map3, map4, map5, map6, map7, mapAbout]

running = True

while running:
    pygame.init()
    ui = UserInterface(mapMainMenu)
    ui.run()
    mapChoice = 0

    if ui.check_win_state():
        for unit in ui._gameState.units:
            if unit.is_control():
                for flag in ui._gameState.units:
                    if flag.location == unit.location and flag != unit:
                        mapChoice = int(flag.id.split("map")[1])
                    if flag.location == unit.location and flag.id == "quit":
                        running = False

        if not running:
            break
        ui = UserInterface(choices[mapChoice])
        ui.run()

pygame.quit()
