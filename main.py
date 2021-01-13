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
map8 = Map8()
map9 = Map9()
map10 = Map10()
map11 = Map11()
choices = [mapMainMenu, map1, map2, map3, map4, map5, map6, map7, map8, map9, map10, map11, mapAbout]

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
                    if flag.location == unit.location:
                        if flag != unit and flag.id != "quit" and flag.id != "mapAbout":
                            mapChoice = int(flag.id.split("map")[1])
                        elif flag.id == "quit":
                            running = False
                        elif flag.id == "mapAbout":
                            mapChoice = 12

        if not running:
            break
        ui = UserInterface(choices[mapChoice])
        ui.run()

pygame.quit()
