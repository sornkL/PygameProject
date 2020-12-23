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
mapHard = MapHard()
mapHell = MapHell()
choices = [mapMainMenu, map1, map2, map3, map4, map5, mapHard, mapHell, mapAbout]

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
                    if flag.location == unit.location and flag.id == "map1":
                        mapChoice = 1
                    elif flag.location == unit.location and flag.id == "map2":
                        mapChoice = 2
                    elif flag.location == unit.location and flag.id == "map3":
                        mapChoice = 3
                    elif flag.location == unit.location and flag.id == "map4":
                        mapChoice = 4
                    elif flag.location == unit.location and flag.id == "map5":
                        mapChoice = 5
                    elif flag.location == unit.location and flag.id == "mapHard":
                        mapChoice = 6
                    elif flag.location == unit.location and flag.id == "mapHell":
                        mapChoice = 7
                    elif flag.location == unit.location and flag.id == "mapAbout":
                        mapChoice = 8
                    elif flag.location == unit.location and flag.id == "quit":
                        running = False

        if not running:
            break
        ui = UserInterface(choices[mapChoice])
        ui.run()

pygame.quit()
