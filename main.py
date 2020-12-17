import pygame


from GameState import *
from MapLoader import *
from UserInterface import *

map1 = Map1()
map2 = Map2()
map3 = Map3()
map4 = Map4()
map5 = Map5()
map6 = Map6()
mapHard = MapHard()
mapHell = MapHell()

pygame.init()
ui = UserInterface(map1)

ui.run()

pygame.quit()

