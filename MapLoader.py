import pygame

from Blocks import *


class Map1():
    def load_map(self):
        units = [
            BabaBlock("testBaba",  Vector2(360, 270)),

            WallBlock("test04",  Vector2(240, 210)),
            WallBlock("test04",  Vector2(270, 210)),
            WallBlock("test04",  Vector2(300, 210)),
            WallBlock("test04",  Vector2(330, 210)),
            WallBlock("test04",  Vector2(360, 210)),
            WallBlock("test04",  Vector2(390, 210)),
            WallBlock("test04",  Vector2(420, 210)),
            WallBlock("test04",  Vector2(450, 210)),
            WallBlock("test04",  Vector2(480, 210)),
            WallBlock("test04",  Vector2(510, 210)),
            WallBlock("test04",  Vector2(540, 210)),
            WallBlock("test04",  Vector2(570, 210)),
            WallBlock("test04",  Vector2(600, 210)),
            WallBlock("test04",  Vector2(630, 210)),
            WallBlock("test04",  Vector2(240, 330)),
            WallBlock("test1215WallBlock",  Vector2(270, 330)),
            WallBlock("test04",  Vector2(300, 330)),
            WallBlock("test04",  Vector2(330, 330)),
            WallBlock("test04",  Vector2(360, 330)),
            WallBlock("test04",  Vector2(390, 330)),
            WallBlock("test04",  Vector2(420, 330)),
            WallBlock("test04",  Vector2(450, 330)),
            WallBlock("test04",  Vector2(480, 330)),
            WallBlock("test04",  Vector2(510, 330)),
            WallBlock("test04",  Vector2(540, 330)),
            WallBlock("test04",  Vector2(570, 330)),
            WallBlock("test04",  Vector2(600, 330)),
            WallBlock("test04",  Vector2(630, 330)),

            SkullBlock("testRock1",  Vector2(510, 300)),
            SkullBlock("testRock2",  Vector2(510, 270)),
            SkullBlock("testRock3",  Vector2(510, 240)),

            FlagBlock("test04",  Vector2(570, 270)),

            BabaNounBlock("testBabaNoun",  Vector2(270, 150)),
            IsBlock("testIs01",  Vector2(300, 150)),
            YouVerbBlock("testYouVerb",  Vector2(330, 150)),

            SkullNounBlock("testRockNoun",  Vector2(540, 150)),
            IsBlock("testIs02",  Vector2(570, 150)),
            PushVerbBlock("testPushVerb",  Vector2(600, 150)),

            WallNounBlock("testWallNoun",  Vector2(270, 390)),
            IsBlock("testIs03",  Vector2(300, 390)),
            StopVerbBlock("testStopVerb",  Vector2(330, 390)),

            FlagNounBlock("testFlagNoun",  Vector2(540, 390)),
            IsBlock("testIs04",  Vector2(570, 390)),
            WinVerbBlock("testWinVerb",  Vector2(600, 390)),
        ]

        return units

class Map2:
    def load_map(self):
        units = [
            WallBlock("self", Vector2(510, 420)),

            FlagBlock("test04", Vector2(240, 210)),
            FlagBlock("test04", Vector2(270, 210)),
            FlagBlock("test04", Vector2(300, 210)),
            FlagBlock("test04", Vector2(330, 210)),
            FlagBlock("test04", Vector2(360, 210)),
            FlagBlock("test04", Vector2(360, 180)),
            FlagBlock("test04", Vector2(360, 150)),
            FlagBlock("test04", Vector2(360, 120)),
            FlagBlock("test04", Vector2(360, 90)),
            FlagBlock("test04", Vector2(390, 90)),
            FlagBlock("test04", Vector2(420, 90)),
            FlagBlock("test04", Vector2(450, 90)),
            FlagBlock("test04", Vector2(480, 90)),
            FlagBlock("test04", Vector2(510, 90)),
            FlagBlock("test04", Vector2(540, 90)),
            FlagBlock("test04", Vector2(570, 90)),
            FlagBlock("test04", Vector2(570, 120)),
            FlagBlock("test04", Vector2(570, 150)),
            FlagBlock("test04", Vector2(570, 180)),
            FlagBlock("test04", Vector2(570, 210)),
            FlagBlock("test04", Vector2(570, 240)),
            FlagBlock("test04", Vector2(570, 270)),
            FlagBlock("test04", Vector2(570, 300)),
            FlagBlock("test04", Vector2(570, 330)),
            FlagBlock("test04", Vector2(570, 360)),
            FlagBlock("test04", Vector2(570, 390)),
            FlagBlock("test04", Vector2(570, 420)),
            FlagBlock("test04", Vector2(570, 450)),
            FlagBlock("test04", Vector2(570, 480)),
            FlagBlock("test04", Vector2(540, 480)),
            FlagBlock("test04", Vector2(510, 480)),
            FlagBlock("test04", Vector2(480, 480)),
            FlagBlock("test04", Vector2(480, 510)),
            FlagBlock("test04", Vector2(450, 510)),
            FlagBlock("test04", Vector2(420, 510)),
            FlagBlock("test04", Vector2(390, 510)),
            FlagBlock("test04", Vector2(360, 510)),
            FlagBlock("test04", Vector2(360, 480)),
            FlagBlock("test04", Vector2(360, 450)),
            FlagBlock("test04", Vector2(360, 420)),
            FlagBlock("test04", Vector2(360, 390)),
            FlagBlock("test04", Vector2(360, 360)),
            FlagBlock("test04", Vector2(360, 330)),
            FlagBlock("test04", Vector2(330, 330)),
            FlagBlock("test04", Vector2(300, 330)),
            FlagBlock("test04", Vector2(270, 330)),
            FlagBlock("test04", Vector2(240, 330)),
            FlagBlock("test04", Vector2(240, 300)),
            FlagBlock("test04", Vector2(240, 270)),
            FlagBlock("test04", Vector2(240, 240)),
            FlagBlock("test04", Vector2(390, 330)),
            FlagBlock("test04", Vector2(420, 330)),
            FlagBlock("test04", Vector2(450, 330)),
            FlagBlock("test04", Vector2(480, 330)),
            FlagBlock("test04", Vector2(510, 330)),
            FlagBlock("test04", Vector2(540, 330)),

            WallNounBlock("text_wall", Vector2(270, 390), 'red'),
            IsBlock("text_is1", Vector2(270, 420)),
            YouVerbBlock("text_you", Vector2(270, 450)),

            FlagNounBlock("text_flag", Vector2(420, 390)),
            IsBlock("text_is2",Vector2(420, 420)),
            StopVerbBlock("text_stop", Vector2(420, 450)),

            WinVerbBlock("text_win", Vector2(510, 210)),

            BabaNounBlock("text_baba", Vector2(300, 270)),
            IsBlock("text_is3", Vector2(420, 150)),
        ]

        return units