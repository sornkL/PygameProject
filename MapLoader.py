import pygame

from Blocks import *


class MapMainMenu():
    def load_map(self):
        units = [
            TileBlock("00", Vector2(90, 240)),
            TileBlock("00", Vector2(120, 240)),
            TileBlock("00", Vector2(150, 240)),
            TileBlock("00", Vector2(180, 240)),
            TileBlock("00", Vector2(210, 240)),
            TileBlock("00", Vector2(240, 240)),
            TileBlock("00", Vector2(270, 240)),
            TileBlock("00", Vector2(300, 240)),
            TileBlock("00", Vector2(330, 240)),
            TileBlock("00", Vector2(360, 240)),
            TileBlock("00", Vector2(390, 240)),
            TileBlock("00", Vector2(420, 240)),
            TileBlock("00", Vector2(450, 240)),
            TileBlock("00", Vector2(480, 240)),
            TileBlock("00", Vector2(510, 240)),
            TileBlock("00", Vector2(540, 240)),
            TileBlock("00", Vector2(570, 240)),
            TileBlock("00", Vector2(600, 240)),
            TileBlock("00", Vector2(630, 240)),
            TileBlock("00", Vector2(660, 240)),
            TileBlock("00", Vector2(690, 240)),
            TileBlock("00", Vector2(690, 210)),
            TileBlock("00", Vector2(720, 210)),
            TileBlock("00", Vector2(720, 180)),
            TileBlock("00", Vector2(750, 180)),
            TileBlock("00", Vector2(780, 180)),

            TileBlock("00", Vector2(90, 270)),
            TileBlock("00", Vector2(120, 270)),
            TileBlock("00", Vector2(150, 270)),
            TileBlock("00", Vector2(180, 270)),
            TileBlock("00", Vector2(210, 270)),
            TileBlock("00", Vector2(240, 270)),
            TileBlock("00", Vector2(270, 270)),
            TileBlock("00", Vector2(300, 270)),
            TileBlock("00", Vector2(330, 270)),
            TileBlock("00", Vector2(360, 270)),
            TileBlock("00", Vector2(390, 270)),
            TileBlock("00", Vector2(420, 270)),
            TileBlock("00", Vector2(450, 270)),
            TileBlock("00", Vector2(480, 270)),
            TileBlock("00", Vector2(510, 270)),
            TileBlock("00", Vector2(540, 270)),
            TileBlock("00", Vector2(570, 270)),
            TileBlock("00", Vector2(600, 270)),
            TileBlock("00", Vector2(630, 270)),
            TileBlock("00", Vector2(660, 270)),

            TileBlock("00", Vector2(90, 300)),
            TileBlock("00", Vector2(120, 300)),
            TileBlock("00", Vector2(150, 300)),
            TileBlock("00", Vector2(180, 300)),
            TileBlock("00", Vector2(210, 300)),
            TileBlock("00", Vector2(240, 300)),
            TileBlock("00", Vector2(270, 300)),
            TileBlock("00", Vector2(300, 300)),
            TileBlock("00", Vector2(330, 300)),
            TileBlock("00", Vector2(360, 300)),
            TileBlock("00", Vector2(390, 300)),
            TileBlock("00", Vector2(420, 300)),
            TileBlock("00", Vector2(450, 300)),
            TileBlock("00", Vector2(480, 300)),
            TileBlock("00", Vector2(510, 300)),
            TileBlock("00", Vector2(540, 300)),
            TileBlock("00", Vector2(570, 300)),
            TileBlock("00", Vector2(600, 300)),
            TileBlock("00", Vector2(630, 300)),
            TileBlock("00", Vector2(660, 300)),
            TileBlock("00", Vector2(690, 300)),
            TileBlock("00", Vector2(690, 330)),
            TileBlock("00", Vector2(720, 330)),
            TileBlock("00", Vector2(720, 360)),
            TileBlock("00", Vector2(750, 360)),
            TileBlock("00", Vector2(780, 360)),

            TileBlock("00", Vector2(750, 300)),
            TileBlock("00", Vector2(750, 270)),
            TileBlock("00", Vector2(750, 240)),
            TileBlock("00", Vector2(780, 240)),
            TileBlock("00", Vector2(780, 300)),
            TileBlock("00", Vector2(810, 300)),
            TileBlock("00", Vector2(810, 270)),
            TileBlock("00", Vector2(810, 240)),

            WallBlock("00", Vector2(690, 180)),
            TileBlock("00", Vector2(690, 210)),
            FireBlock("00", Vector2(690, 210)),
            WallBlock("00", Vector2(720, 150)),
            TileBlock("00", Vector2(720, 180)),
            FireBlock("00", Vector2(720, 180)),
            WallBlock("00", Vector2(750, 150)),
            WallBlock("00", Vector2(780, 150)),
            WallBlock("00", Vector2(810, 150)),
            TileBlock("00", Vector2(810, 180)),
            FireBlock("00", Vector2(810, 180)),
            WallBlock("00", Vector2(840, 180)),
            TileBlock("00", Vector2(840, 210)),
            FireBlock("00", Vector2(840, 210)),

            WallBlock("00", Vector2(690, 360)),
            TileBlock("00", Vector2(690, 330)),
            FireBlock("00", Vector2(690, 330)),
            WallBlock("00", Vector2(720, 390)),
            TileBlock("00", Vector2(720, 360)),
            FireBlock("00", Vector2(720, 360)),
            WallBlock("00", Vector2(750, 390)),
            WallBlock("00", Vector2(780, 390)),
            WallBlock("00", Vector2(810, 390)),
            TileBlock("00", Vector2(810, 360)),
            FireBlock("00", Vector2(810, 360)),
            WallBlock("00", Vector2(840, 360)),
            TileBlock("00", Vector2(840, 330)),
            FireBlock("00", Vector2(840, 330)),

            WallBlock("00", Vector2(870, 330)),
            WallBlock("00", Vector2(870, 300)),
            WallBlock("00", Vector2(870, 270)),
            WallBlock("00", Vector2(870, 240)),
            WallBlock("00", Vector2(870, 210)),

            # FireBlock("00", Vector2(750, 300)),
            # FireBlock("00", Vector2(810, 300)),
            # FireBlock("00", Vector2(750, 240)),
            # FireBlock("00", Vector2(810, 240)),

            BabaBlock("baba", Vector2(150, 270)),

            Block1("1", Vector2(150, 150)),
            FlagBlock("map1", Vector2(150, 180)),
            DoorBlock("door1", Vector2(150, 210)),
            RobotBlock("00", Vector2(120, 210)),
            PillarBlock("00", Vector2(90, 210)),
            WallBlock("00", Vector2(90, 180)),
            WallBlock("00", Vector2(90, 150)),
            PillarBlock("00", Vector2(180, 210)),
            WallBlock("00", Vector2(180, 180)),
            WallBlock("00", Vector2(180, 150)),

            Block3("3", Vector2(240, 150)),
            FlagBlock("map3", Vector2(240, 180)),
            DoorBlock("door3", Vector2(240, 210)),
            RobotBlock("00", Vector2(210, 210)),
            PillarBlock("00", Vector2(270, 210)),
            WallBlock("00", Vector2(270, 180)),
            WallBlock("00", Vector2(270, 150)),

            Block5("5", Vector2(330, 150)),
            FlagBlock("map5", Vector2(330, 180)),
            DoorBlock("door5", Vector2(330, 210)),
            RobotBlock("00", Vector2(300, 210)),
            PillarBlock("00", Vector2(360, 210)),
            WallBlock("00", Vector2(360, 180)),
            WallBlock("00", Vector2(360, 150)),

            Block7("7", Vector2(420, 150)),
            FlagBlock("map7", Vector2(420, 180)),
            DoorBlock("door7", Vector2(420, 210)),
            RobotBlock("00", Vector2(390, 210)),
            PillarBlock("00", Vector2(450, 210)),
            WallBlock("00", Vector2(450, 180)),
            WallBlock("00", Vector2(450, 150)),

            Block9("9", Vector2(510, 150)),
            FlagBlock("map9", Vector2(510, 180)),
            DoorBlock("door7", Vector2(510, 210)),
            RobotBlock("00", Vector2(480, 210)),
            PillarBlock("00", Vector2(540, 210)),
            WallBlock("00", Vector2(540, 180)),
            WallBlock("00", Vector2(540, 150)),
            WallBlock("00", Vector2(660, 180)),
            WallBlock("00", Vector2(660, 150)),
            PillarBlock("00", Vector2(660, 210)),

            Block1("1", Vector2(610, 150)),
            Block1("1", Vector2(590, 150)),
            FlagBlock("map11",Vector2(600,180)),
            DoorBlock("doorabout", Vector2(600, 210)),
            RobotBlock("00", Vector2(570, 210)),
            RobotBlock("00", Vector2(630, 210)),

            Block2("2", Vector2(150, 390)),
            FlagBlock("map2", Vector2(150, 360)),
            DoorBlock("door2", Vector2(150, 330)),
            RobotBlock("00", Vector2(120, 330)),
            PillarBlock("00", Vector2(90, 330)),
            WallBlock("00", Vector2(90, 360)),
            WallBlock("00", Vector2(90, 390)),
            PillarBlock("00", Vector2(180, 330)),
            WallBlock("00", Vector2(180, 360)),
            WallBlock("00", Vector2(180, 390)),

            Block4("4", Vector2(240, 390)),
            FlagBlock("map4", Vector2(240, 360)),
            DoorBlock("door2", Vector2(240, 330)),
            RobotBlock("00", Vector2(210, 330)),
            PillarBlock("00", Vector2(270, 330)),
            WallBlock("00", Vector2(270, 360)),
            WallBlock("00", Vector2(270, 390)),

            Block6("6", Vector2(330, 390)),
            FlagBlock("map6", Vector2(330, 360)),
            DoorBlock("door2", Vector2(330, 330)),
            RobotBlock("00", Vector2(300, 330)),
            PillarBlock("00", Vector2(360, 330)),
            WallBlock("00", Vector2(360, 360)),
            WallBlock("00", Vector2(360, 390)),

            Block8("8", Vector2(420, 390)),
            FlagBlock("map8", Vector2(420, 360)),
            DoorBlock("door2", Vector2(420, 330)),
            RobotBlock("00", Vector2(390, 330)),
            PillarBlock("00", Vector2(450, 330)),
            WallBlock("00", Vector2(450, 360)),
            WallBlock("00", Vector2(450, 390)),

            Block1("1", Vector2(480, 390)),
            Block0("0", Vector2(510, 390)),
            FlagBlock("map10", Vector2(510, 360)),
            DoorBlock("door2", Vector2(510, 330)),
            RobotBlock("00", Vector2(480, 330)),

            Blockabout("00", Vector2(562, 379)),
            FlagBlock("mapAbout", Vector2(600, 360)),
            DoorBlock("doorabout", Vector2(600, 330)),
            RobotBlock("00", Vector2(570, 330)),
            RobotBlock("00", Vector2(630, 330)),
            PillarBlock("00", Vector2(660, 330)),
            WallBlock("00", Vector2(660, 360)),
            WallBlock("00", Vector2(660, 390)),
            PillarBlock("00", Vector2(540, 330)),
            WallBlock("00", Vector2(540, 360)),
            WallBlock("00", Vector2(540, 390)),

            Blockquit("quit", Vector2(750, 290)),
            FlagBlock("quit", Vector2(780, 270)),
            Block0("quit", Vector2(780, 270)),

            Blockwasd("00", Vector2(359, 490)),
            Blockmove("00", Vector2(481, 520)),

            BabaNounBlock("testBabaNoun", Vector2(810, 570)),
            IsBlock("testIs01", Vector2(840, 570)),
            YouVerbBlock("testYouVerb", Vector2(870, 570)),

            FlagNounBlock("testFlagNoun", Vector2(540, 600)),
            IsBlock("testIs04", Vector2(570, 600)),
            WinVerbBlock("testWinVerb", Vector2(600, 600)),

            WallNounBlock("testFlagNoun", Vector2(630, 600)),
            IsBlock("testIs04", Vector2(660, 600)),
            StopVerbBlock("testWinVerb", Vector2(690, 600)),

            DoorNounBlock("testFlagNoun", Vector2(750, 600)),
            IsBlock("testIs04", Vector2(780, 600)),
            WeakVerbBlock("testWinVerb", Vector2(810, 600)),

        ]

        return units

    def load_picture(self):
        return "pics/mapMain.png"


class Map1():
    def load_map(self):
        units = [

            TileBlock("00", Vector2(240, 240)),
            TileBlock("00", Vector2(270, 240)),
            TileBlock("00", Vector2(300, 240)),
            TileBlock("00", Vector2(330, 240)),
            TileBlock("00", Vector2(360, 240)),
            TileBlock("00", Vector2(390, 240)),
            TileBlock("00", Vector2(420, 240)),
            TileBlock("00", Vector2(450, 240)),
            TileBlock("00", Vector2(480, 240)),
            TileBlock("00", Vector2(510, 240)),
            TileBlock("00", Vector2(540, 240)),
            TileBlock("00", Vector2(570, 240)),
            TileBlock("00", Vector2(600, 240)),
            TileBlock("00", Vector2(630, 240)),

            TileBlock("00", Vector2(240, 270)),
            TileBlock("00", Vector2(270, 270)),
            TileBlock("00", Vector2(300, 270)),
            TileBlock("00", Vector2(330, 270)),
            TileBlock("00", Vector2(360, 270)),
            TileBlock("00", Vector2(390, 270)),
            TileBlock("00", Vector2(420, 270)),
            TileBlock("00", Vector2(450, 270)),
            TileBlock("00", Vector2(480, 270)),
            TileBlock("00", Vector2(510, 270)),
            TileBlock("00", Vector2(540, 270)),
            TileBlock("00", Vector2(570, 270)),
            TileBlock("00", Vector2(600, 270)),
            TileBlock("00", Vector2(630, 270)),

            TileBlock("00", Vector2(240, 300)),
            TileBlock("00", Vector2(270, 300)),
            TileBlock("00", Vector2(300, 300)),
            TileBlock("00", Vector2(330, 300)),
            TileBlock("00", Vector2(360, 300)),
            TileBlock("00", Vector2(390, 300)),
            TileBlock("00", Vector2(420, 300)),
            TileBlock("00", Vector2(450, 300)),
            TileBlock("00", Vector2(480, 300)),
            TileBlock("00", Vector2(510, 300)),
            TileBlock("00", Vector2(540, 300)),
            TileBlock("00", Vector2(570, 300)),
            TileBlock("00", Vector2(600, 300)),
            TileBlock("00", Vector2(630, 300)),

            WallBlock("test04", Vector2(240, 210)),
            WallBlock("test04", Vector2(270, 210)),
            WallBlock("test04", Vector2(300, 210)),
            WallBlock("test04", Vector2(330, 210)),
            WallBlock("test04", Vector2(360, 210)),
            WallBlock("test04", Vector2(390, 210)),
            WallBlock("test04", Vector2(420, 210)),
            WallBlock("test04", Vector2(450, 210)),
            WallBlock("test04", Vector2(480, 210)),
            WallBlock("test04", Vector2(510, 210)),
            WallBlock("test04", Vector2(540, 210)),
            WallBlock("test04", Vector2(570, 210)),
            WallBlock("test04", Vector2(600, 210)),
            WallBlock("test04", Vector2(630, 210)),
            WallBlock("test04", Vector2(240, 330)),
            WallBlock("test1215WallBlock", Vector2(270, 330)),
            WallBlock("test04", Vector2(300, 330)),
            WallBlock("test04", Vector2(330, 330)),
            WallBlock("test04", Vector2(360, 330)),
            WallBlock("test04", Vector2(390, 330)),
            WallBlock("test04", Vector2(420, 330)),
            WallBlock("test04", Vector2(450, 330)),
            WallBlock("test04", Vector2(480, 330)),
            WallBlock("test04", Vector2(510, 330)),
            WallBlock("test04", Vector2(540, 330)),
            WallBlock("test04", Vector2(570, 330)),
            WallBlock("test04", Vector2(600, 330)),
            WallBlock("test04", Vector2(630, 330)),

            RockBlock("testRock1", Vector2(510, 300)),
            RockBlock("testRock2", Vector2(510, 270)),
            RockBlock("testRock3", Vector2(510, 240)),

            FlagBlock("test04", Vector2(570, 270)),

            BabaNounBlock("testBabaNoun", Vector2(270, 150)),
            IsBlock("testIs01", Vector2(300, 150)),
            YouVerbBlock("testYouVerb", Vector2(330, 150)),

            RockNounBlock("testRockNoun", Vector2(540, 150)),
            IsBlock("testIs02", Vector2(570, 150)),
            PushVerbBlock("testPushVerb", Vector2(600, 150)),

            WallNounBlock("testWallNoun", Vector2(270, 390)),
            IsBlock("testIs03", Vector2(300, 390)),
            StopVerbBlock("testStopVerb", Vector2(330, 390)),

            FlagNounBlock("testFlagNoun", Vector2(540, 390)),
            IsBlock("testIs04", Vector2(570, 390)),
            WinVerbBlock("testWinVerb", Vector2(600, 390)),

            BabaBlock("testBaba", Vector2(360, 270))
        ]

        return units

    def load_picture(self):
        return "pics/map1.png"


class Map2():
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
            IsBlock("text_is2", Vector2(420, 420)),
            StopVerbBlock("text_stop", Vector2(420, 450)),

            WinVerbBlock("text_win", Vector2(510, 210)),

            BabaNounBlock("text_baba", Vector2(300, 270)),
            IsBlock("text_is3", Vector2(420, 150)),
        ]

        return units

    def load_picture(self):
        return "pics/map2.png"


class Map3():
    def load_map(self):
        units = [

            # 临时墙
            WallBlock("Null", Vector2(300, 150)),
            WallBlock("Null", Vector2(330, 150)),
            WallBlock("Null", Vector2(360, 150)),
            WallBlock("Null", Vector2(390, 150)),
            WallBlock("Null", Vector2(420, 150)),
            WallBlock("Null", Vector2(450, 150)),
            WallBlock("Null", Vector2(480, 150)),
            WallBlock("Null", Vector2(510, 150)),
            WallBlock("Null", Vector2(540, 150)),

            WallBlock("Null", Vector2(300, 420)),
            WallBlock("Null", Vector2(330, 420)),
            WallBlock("Null", Vector2(360, 420)),
            WallBlock("Null", Vector2(390, 420)),
            WallBlock("Null", Vector2(420, 420)),
            WallBlock("Null", Vector2(450, 420)),
            WallBlock("Null", Vector2(480, 420)),
            WallBlock("Null", Vector2(510, 420)),
            WallBlock("Null", Vector2(540, 420)),

            WallBlock("Null", Vector2(300, 180)),
            WallBlock("Null", Vector2(300, 210)),
            WallBlock("Null", Vector2(300, 240)),
            WallBlock("Null", Vector2(300, 270)),
            WallBlock("Null", Vector2(300, 300)),
            WallBlock("Null", Vector2(300, 330)),
            WallBlock("Null", Vector2(300, 360)),
            WallBlock("Null", Vector2(300, 390)),

            WallBlock("Null", Vector2(540, 180)),
            WallBlock("Null", Vector2(540, 210)),
            WallBlock("Null", Vector2(540, 240)),
            WallBlock("Null", Vector2(540, 270)),
            WallBlock("Null", Vector2(540, 300)),
            WallBlock("Null", Vector2(540, 330)),
            WallBlock("Null", Vector2(540, 360)),
            WallBlock("Null", Vector2(540, 390)),
            # 结束墙

            TileBlock("l-u", Vector2(360, 180)),
            TileBlock("l-u", Vector2(390, 180)),
            TileBlock("l-u", Vector2(420, 180)),
            TileBlock("l-u", Vector2(450, 180)),
            TileBlock("l-u", Vector2(480, 180)),
            TileBlock("r-u", Vector2(510, 180)),
            TileBlock("r-u", Vector2(510, 210)),
            TileBlock("r-u", Vector2(510, 240)),
            TileBlock("r-u", Vector2(510, 270)),
            TileBlock("r-u", Vector2(510, 300)),
            TileBlock("r-u", Vector2(510, 330)),
            TileBlock("r-u", Vector2(510, 360)),
            TileBlock("r-b", Vector2(510, 390)),
            TileBlock("r-b", Vector2(480, 390)),
            TileBlock("r-b", Vector2(450, 390)),
            TileBlock("r-b", Vector2(420, 390)),
            TileBlock("r-b", Vector2(390, 390)),
            TileBlock("r-b", Vector2(360, 390)),

            TileBlock("l-b", Vector2(330, 390)),
            TileBlock("l-b", Vector2(330, 360)),
            TileBlock("l-b", Vector2(330, 330)),
            TileBlock("l-b", Vector2(330, 300)),
            TileBlock("l-b", Vector2(330, 270)),
            TileBlock("l-b", Vector2(330, 240)),
            TileBlock("l-b", Vector2(330, 210)),
            TileBlock("l-u", Vector2(330, 180)),

            TileBlock("BabaNounBlock", Vector2(120, 300)),
            TileBlock("Is00", Vector2(150, 300)),
            TileBlock("YouVerbBlock", Vector2(180, 300)),

            TileBlock("BabaNounBlock", Vector2(120, 270)),
            TileBlock("Is00", Vector2(150, 270)),
            TileBlock("YouVerbBlock", Vector2(180, 270)),

            TileBlock("FlagNounBlock", Vector2(120, 240)),
            TileBlock("Is01", Vector2(150, 240)),
            TileBlock("WinVerbBlock", Vector2(180, 240)),

            RockBlock("01", Vector2(330, 240)),
            RockBlock("01", Vector2(360, 240)),
            RockBlock("01", Vector2(390, 240)),
            RockBlock("01", Vector2(390, 210)),

            BabaNounBlock("BabaNounBlock", Vector2(120, 300)),
            IsBlock("Is00", Vector2(150, 300)),
            YouVerbBlock("YouVerbBlock", Vector2(180, 300)),

            FlagNounBlock("FlagNounBlock", Vector2(120, 240)),
            IsBlock("Is01", Vector2(150, 240)),
            WinVerbBlock("WinVerbBlock", Vector2(180, 240)),

            RockNounBlock("RockNounBlock", Vector2(360, 330)),
            IsBlock("Is02", Vector2(390, 330)),
            StopVerbBlock("StopVerbBlock", Vector2(420, 330)),

            StopVerbBlock("StopVerbBlock", Vector2(480, 270)),
            IsBlock("Is03", Vector2(480, 240)),
            WallNounBlock("WallNounBlock", Vector2(480, 210)),

            WallNounBlock("WallNounBlock", Vector2(0, 0)),
            IsBlock("Is03", Vector2(30, 0)),
            DefeatVerbBlock("DefeatVerbBlock", Vector2(60, 0)),

            BabaBlock("Baba", Vector2(330, 180))
        ]

        return units

    def load_picture(self):
        return "pics/map3.png"


class Map4():
    def load_map(self):
        units = [
            TileBlock("0", Vector2(270, 240)),
            TileBlock("0", Vector2(270, 270)),
            TileBlock("0", Vector2(270, 300)),
            TileBlock("0", Vector2(300, 240)),
            TileBlock("0", Vector2(300, 270)),
            TileBlock("0", Vector2(300, 300)),
            TileBlock("0", Vector2(330, 240)),
            TileBlock("0", Vector2(330, 270)),
            TileBlock("0", Vector2(330, 300)),


            WallBlock("n", Vector2(0, -30)),
            BabaBlock("Baba", Vector2(300, 270)),

            WallBlock("01", Vector2(300, 210)),
            WallBlock("02", Vector2(330, 210)),
            WallBlock("03", Vector2(270, 210)),
            WallBlock("04", Vector2(240, 210)),
            WallBlock("05", Vector2(360, 210)),

            WallBlock("06", Vector2(300, 330)),
            WallBlock("07", Vector2(330, 330)),
            WallBlock("08", Vector2(270, 330)),
            WallBlock("09", Vector2(240, 330)),
            WallBlock("10", Vector2(360, 330)),

            WallBlock("11", Vector2(360, 240)),
            RockBlock("12", Vector2(360, 270)),
            WallBlock("13", Vector2(360, 300)),

            WallBlock("14", Vector2(240, 240)),
            WallBlock("15", Vector2(240, 270)),
            WallBlock("16", Vector2(240, 300)),

            TileBlock("RockNounBlock", Vector2(270, 120)),
            TileBlock("Is02", Vector2(300, 120)),
            TileBlock("PushVerbBlock", Vector2(330, 120)),

            RockNounBlock("RockNounBlock", Vector2(270, 120)),
            IsBlock("Is02", Vector2(300, 120)),
            PushVerbBlock("PushVerbBlock", Vector2(330, 120)),

            RockBlock("17", Vector2(420, 90)),
            RockBlock("18", Vector2(480, 120)),
            RockBlock("19", Vector2(630, 420)),
            RockBlock("20", Vector2(660, 90)),
            RockBlock("21", Vector2(450, 390)),

            TileBlock("WallNoun", Vector2(270, 420)),
            TileBlock("Is03", Vector2(300, 420)),
            TileBlock("StopVerb", Vector2(330, 420)),

            BabaNounBlock("WallNoun", Vector2(270, 420)),
            IsBlock("Is03", Vector2(300, 420)),
            YouVerbBlock("StopVerb", Vector2(330, 420)),

            TileBlock("Flag", Vector2(600, 240)),
            TileBlock("Flag", Vector2(600, 270)),
            TileBlock("Flag", Vector2(600, 300)),
            TileBlock("Flag", Vector2(630, 240)),
            TileBlock("Flag", Vector2(630, 270)),
            TileBlock("Flag", Vector2(630, 300)),
            TileBlock("Flag", Vector2(660, 240)),
            TileBlock("Flag", Vector2(660, 270)),
            TileBlock("Flag", Vector2(660, 300)),

            FlagBlock("Flag", Vector2(630, 270)),

            SkullBlock("22", Vector2(570, 210)),
            SkullBlock("23", Vector2(600, 210)),
            SkullBlock("24", Vector2(630, 210)),
            SkullBlock("25", Vector2(660, 210)),
            SkullBlock("26", Vector2(690, 210)),

            SkullBlock("22", Vector2(570, 330)),
            SkullBlock("23", Vector2(600, 330)),
            SkullBlock("24", Vector2(630, 330)),
            SkullBlock("25", Vector2(660, 330)),
            SkullBlock("26", Vector2(690, 330)),

            SkullBlock("23", Vector2(690, 240)),
            SkullBlock("24", Vector2(690, 270)),
            SkullBlock("25", Vector2(690, 300)),

            SkullBlock("23", Vector2(570, 240)),
            SkullBlock("24", Vector2(570, 270)),
            SkullBlock("25", Vector2(570, 300)),

            WallNounBlock("BabaNoun", Vector2(0, 210)),
            IsBlock("Is01", Vector2(0, 240)),
            StopVerbBlock("YouVerb", Vector2(0, 270)),

            SkullNounBlock("RockNoun", Vector2(810, 570)),
            IsBlock("Is02", Vector2(840, 570)),
            DefeatVerbBlock("DefeatVerb", Vector2(870, 570)),

            FlagNounBlock("FlagNoun", Vector2(0, 0)),
            IsBlock("Is04", Vector2(30, 0)),
            WinVerbBlock("WinVerb", Vector2(60, 0)),
        ]


        return units

    def load_picture(self):
        return "pics/map4.png"


class Map5():
    def load_map(self):
        units = [
            #临时墙
            WallBlock("Null", Vector2(180, 150)),
            WallBlock("Null", Vector2(210, 150)),
            WallBlock("Null", Vector2(240, 150)),
            WallBlock("Null", Vector2(270, 150)),
            WallBlock("Null", Vector2(300, 150)),
            WallBlock("Null", Vector2(330, 150)),
            WallBlock("Null", Vector2(360, 150)),
            WallBlock("Null", Vector2(390, 150)),
            WallBlock("Null", Vector2(420, 150)),
            WallBlock("Null", Vector2(450, 150)),
            WallBlock("Null", Vector2(480, 150)),
            WallBlock("Null", Vector2(510, 150)),
            WallBlock("Null", Vector2(540, 150)),
            WallBlock("Null", Vector2(570, 150)),
            WallBlock("Null", Vector2(600, 150)),
            WallBlock("Null", Vector2(630, 150)),
            WallBlock("Null", Vector2(660, 150)),

            WallBlock("Null", Vector2(180, 420)),
            WallBlock("Null", Vector2(210, 420)),
            WallBlock("Null", Vector2(240, 420)),
            WallBlock("Null", Vector2(270, 420)),
            WallBlock("Null", Vector2(300, 420)),
            WallBlock("Null", Vector2(330, 420)),
            WallBlock("Null", Vector2(360, 420)),
            WallBlock("Null", Vector2(390, 420)),
            WallBlock("Null", Vector2(420, 420)),
            WallBlock("Null", Vector2(450, 420)),
            WallBlock("Null", Vector2(480, 420)),
            WallBlock("Null", Vector2(510, 420)),
            WallBlock("Null", Vector2(540, 420)),
            WallBlock("Null", Vector2(570, 420)),
            WallBlock("Null", Vector2(600, 420)),
            WallBlock("Null", Vector2(630, 420)),
            WallBlock("Null", Vector2(660, 420)),

            WallBlock("Null", Vector2(180, 180)),
            WallBlock("Null", Vector2(180, 210)),
            WallBlock("Null", Vector2(180, 240)),
            WallBlock("Null", Vector2(180, 270)),
            WallBlock("Null", Vector2(180, 300)),
            WallBlock("Null", Vector2(180, 330)),
            WallBlock("Null", Vector2(180, 360)),
            WallBlock("Null", Vector2(180, 390)),

            WallBlock("Null", Vector2(570, 180)),
            WallBlock("Null", Vector2(570, 210)),
            WallBlock("Null", Vector2(570, 240)),
            WallBlock("Null", Vector2(570, 270)),
            WallBlock("Null", Vector2(570, 300)),
            WallBlock("Null", Vector2(570, 330)),
            WallBlock("Null", Vector2(570, 360)),
            WallBlock("Null", Vector2(570, 390)),
            #结束墙

            BabaBlock("Baba", Vector2(300, 300)),

            FlagBlock("Flag", Vector2(510, 210)),

            BabaNounBlock("BabaNounBlock", Vector2(240, 210)),
            IsBlock("Is00", Vector2(270, 210)),
            YouVerbBlock("YouVerbBlock", Vector2(300, 210)),

            RockBlock("Null", Vector2(330, 180)),
            RockBlock("Null", Vector2(210, 240)),
            RockBlock("Null", Vector2(210, 330)),
            RockBlock("Null", Vector2(240, 360)),
            RockBlock("Null", Vector2(330, 390)),
            RockBlock("Null", Vector2(420, 390)),
            RockBlock("Null", Vector2(390, 360)),
            RockBlock("Null", Vector2(390, 330)),
            RockBlock("Null", Vector2(390, 300)),
            RockBlock("Null", Vector2(420, 240)),
            RockBlock("Null", Vector2(450, 270)),
            RockBlock("Null", Vector2(480, 300)),
            RockBlock("Null", Vector2(480, 360)),
            RockBlock("Null", Vector2(510, 270)),
            RockBlock("Null", Vector2(540, 300)),

            FlagNounBlock("FlagNounBlock", Vector2(450, 330)),
            WinVerbBlock("WinVerbBlock", Vector2(510, 330)),

            RockNounBlock("RockNounBlock", Vector2(870, 270)),
            IsBlock("Is02", Vector2(870, 300)),
            StopVerbBlock("StopVerbBlock", Vector2(870, 330)),

        ]

        return units

    def load_picture(self):
        return "pics/map5.png"


class Map6():
    def load_map(self):
        units = [
            WallNounBlock("LeftUp", Vector2(180,150)),
            WallNounBlock("RightBottom", Vector2(210+15*30,180+8*30)),
            #临时墙
            WallBlock("Null", Vector2(180, 150)),
            WallBlock("Null", Vector2(210, 150)),
            WallBlock("Null", Vector2(240, 150)),
            WallBlock("Null", Vector2(270, 150)),
            WallBlock("Null", Vector2(300, 150)),
            WallBlock("Null", Vector2(330, 150)),
            WallBlock("Null", Vector2(360, 150)),
            WallBlock("Null", Vector2(390, 150)),
            WallBlock("Null", Vector2(420, 150)),
            WallBlock("Null", Vector2(450, 150)),
            WallBlock("Null", Vector2(480, 150)),
            WallBlock("Null", Vector2(510, 150)),
            WallBlock("Null", Vector2(540, 150)),
            WallBlock("Null", Vector2(570, 150)),
            WallBlock("Null", Vector2(600, 150)),
            WallBlock("Null", Vector2(630, 150)),
            WallBlock("Null", Vector2(660, 150)),

            WallBlock("Null", Vector2(180, 420)),
            WallBlock("Null", Vector2(210, 420)),
            WallBlock("Null", Vector2(240, 420)),
            WallBlock("Null", Vector2(270, 420)),
            WallBlock("Null", Vector2(300, 420)),
            WallBlock("Null", Vector2(330, 420)),
            WallBlock("Null", Vector2(360, 420)),
            WallBlock("Null", Vector2(390, 420)),
            WallBlock("Null", Vector2(420, 420)),
            WallBlock("Null", Vector2(450, 420)),
            WallBlock("Null", Vector2(480, 420)),
            WallBlock("Null", Vector2(510, 420)),
            WallBlock("Null", Vector2(540, 420)),
            WallBlock("Null", Vector2(570, 420)),
            WallBlock("Null", Vector2(600, 420)),
            WallBlock("Null", Vector2(630, 420)),
            WallBlock("Null", Vector2(660, 420)),

            WallBlock("Null", Vector2(660, 390)),
            WallBlock("Null", Vector2(660, 360)),
            WallBlock("Null", Vector2(660, 330)),
            WallBlock("Null", Vector2(660, 300)),
            WallBlock("Null", Vector2(660, 270)),
            WallBlock("Null", Vector2(660, 240)),
            WallBlock("Null", Vector2(660, 210)),
            WallBlock("Null", Vector2(660, 180)),

            WallBlock("Null", Vector2(180, 390)),
            WallBlock("Null", Vector2(180, 360)),
            WallBlock("Null", Vector2(180, 330)),
            WallBlock("Null", Vector2(180, 300)),
            WallBlock("Null", Vector2(180, 270)),
            WallBlock("Null", Vector2(180, 240)),
            WallBlock("Null", Vector2(180, 210)),
            WallBlock("Null", Vector2(180, 180)),

            #结束墙
            BabaBlock("Baba",  Vector2(300, 210)),

            BabaNounBlock("BabaNounBlock", Vector2(270, 240)),
            IsBlock("Is00", Vector2(300, 240)),
            YouVerbBlock("YouVerbBlock", Vector2(330, 240)),

            WallNounBlock("WallNounBlock", Vector2(210,390)),
            IsBlock("Is01", Vector2(240,390)),
            StopVerbBlock("StopVerbBlock", Vector2(270,390)),
            WallBlock("00", Vector2(300, 390)),
            WallBlock("01", Vector2(330, 390)),
            SkullBlock("02", Vector2(330, 360)),
            SkullBlock("03", Vector2(360, 360)),
            FlagBlock("Flag", Vector2(390, 360)),
            WallBlock("04", Vector2(330, 330)),
            WallBlock("04.1", Vector2(330, 300)),
            WallBlock("05", Vector2(360, 300)),
            WallBlock("06", Vector2(390, 300)),
            WallBlock("07", Vector2(420, 300)),
            WallBlock("08", Vector2(450, 300)),
            WallBlock("09", Vector2(450, 330)),
            WallBlock("10", Vector2(450, 360)),
            WallBlock("11", Vector2(450, 390)),
            WallBlock("12", Vector2(450, 270)),
            WallBlock("13", Vector2(450, 240)),
            RockBlock("14", Vector2(450, 210)),
            WallBlock("15", Vector2(450, 180)),
            WallBlock("16", Vector2(480, 180)),
            WallBlock("17", Vector2(510, 180)),
            WallBlock("18", Vector2(540, 180)),
            WallBlock("19", Vector2(570, 180)),
            WallBlock("20.1", Vector2(600, 180)),
            WallBlock("20", Vector2(630, 180)),
            WallBlock("21", Vector2(630, 210)),
            WallBlock("22", Vector2(630, 240)),
            WallBlock("23", Vector2(630, 270)),
            WallBlock("24", Vector2(630, 300)),
            WallBlock("25", Vector2(630, 330)),
            WallBlock("26", Vector2(630, 360)),
            WallBlock("27", Vector2(630, 390)),
            WallBlock("28", Vector2(600, 300)),
            WallBlock("29", Vector2(570, 300)),
            WallBlock("30", Vector2(540, 300)),
            WallBlock("31", Vector2(540, 270)),
            WallBlock("32", Vector2(540, 240)),
            SkullNounBlock("SkullNounBlock", Vector2(540, 210)),
            FlagNounBlock("FlagNounBlock", Vector2(570, 210)),
            IsBlock("Is03", Vector2(570, 240)),
            DefeatVerbBlock("DefeatVerbBlock", Vector2(570, 270)),
            IsBlock("Is04", Vector2(600, 240)),
            WinVerbBlock("WinVerbBlock", Vector2(600, 270)),

            RockNounBlock("RockNoun",  Vector2(510, 360)),
            IsBlock("Is03",  Vector2(540, 360)),
            PushVerbBlock("PushVerb",  Vector2(570, 360)),
        ]

        return units

    def load_picture(self):
        return "pics/map6.png"


class Map7():
    def load_map(self):
        units = [
            WallNounBlock("LeftUp", Vector2(180,150)),
            WallNounBlock("RightBottom", Vector2(210+15*30,180+8*30)),

            #临时墙
            WallBlock("Null", Vector2(180, 150)),
            WallBlock("Null", Vector2(210, 150)),
            WallBlock("Null", Vector2(240, 150)),
            WallBlock("Null", Vector2(270, 150)),
            WallBlock("Null", Vector2(300, 150)),
            WallBlock("Null", Vector2(330, 150)),
            WallBlock("Null", Vector2(360, 150)),
            WallBlock("Null", Vector2(390, 150)),
            WallBlock("Null", Vector2(420, 150)),
            WallBlock("Null", Vector2(450, 150)),
            WallBlock("Null", Vector2(480, 150)),
            WallBlock("Null", Vector2(510, 150)),
            WallBlock("Null", Vector2(540, 150)),
            WallBlock("Null", Vector2(570, 150)),
            WallBlock("Null", Vector2(600, 150)),
            WallBlock("Null", Vector2(630, 150)),
            WallBlock("Null", Vector2(660, 150)),

            WallBlock("Null", Vector2(180, 420)),
            WallBlock("Null", Vector2(210, 420)),
            WallBlock("Null", Vector2(240, 420)),
            WallBlock("Null", Vector2(270, 420)),
            WallBlock("Null", Vector2(300, 420)),
            WallBlock("Null", Vector2(330, 420)),
            WallBlock("Null", Vector2(360, 420)),
            WallBlock("Null", Vector2(390, 420)),
            WallBlock("Null", Vector2(420, 420)),
            WallBlock("Null", Vector2(450, 420)),
            WallBlock("Null", Vector2(480, 420)),
            WallBlock("Null", Vector2(510, 420)),
            WallBlock("Null", Vector2(540, 420)),
            WallBlock("Null", Vector2(570, 420)),
            WallBlock("Null", Vector2(600, 420)),
            WallBlock("Null", Vector2(630, 420)),
            WallBlock("Null", Vector2(660, 420)),

            WallBlock("Null", Vector2(660, 390)),
            WallBlock("Null", Vector2(660, 360)),
            WallBlock("Null", Vector2(660, 330)),
            WallBlock("Null", Vector2(660, 300)),
            WallBlock("Null", Vector2(660, 270)),
            WallBlock("Null", Vector2(660, 240)),
            WallBlock("Null", Vector2(660, 210)),
            WallBlock("Null", Vector2(660, 180)),

            WallBlock("Null", Vector2(180, 390)),
            WallBlock("Null", Vector2(180, 360)),
            WallBlock("Null", Vector2(180, 330)),
            WallBlock("Null", Vector2(180, 300)),
            WallBlock("Null", Vector2(180, 270)),
            WallBlock("Null", Vector2(180, 240)),
            WallBlock("Null", Vector2(180, 210)),
            WallBlock("Null", Vector2(180, 180)),

            #结束墙
            BabaBlock("Baba",  Vector2(300, 210)),

            BabaNounBlock("BabaNounBlock", Vector2(270, 240)),
            IsBlock("Is00", Vector2(300, 240)),
            YouVerbBlock("YouVerbBlock", Vector2(330, 240)),

            WallNounBlock("WallNounBlock", Vector2(210,390)),
            IsBlock("Is01", Vector2(240,390)),
            StopVerbBlock("StopVerbBlock", Vector2(270,390)),
            WallBlock("00", Vector2(300, 390)),
            WallBlock("01", Vector2(330, 390)),
            SkullBlock("02", Vector2(330, 360)),
            FlagBlock("Flag", Vector2(390, 360)),
            WallBlock("04", Vector2(330, 330)),
            WallBlock("04.1", Vector2(330, 300)),
            WallBlock("05", Vector2(360, 300)),
            WallBlock("06", Vector2(390, 300)),
            WallBlock("07", Vector2(420, 300)),
            WallBlock("08", Vector2(450, 300)),
            WallBlock("09", Vector2(450, 330)),
            WallBlock("10", Vector2(450, 360)),
            WallBlock("11", Vector2(450, 390)),
            WallBlock("12", Vector2(450, 270)),
            WallBlock("13", Vector2(450, 240)),
            RockBlock("14", Vector2(450, 210)),
            JellyBlock("JellyBlock", Vector2(480, 210)),
            WallBlock("15", Vector2(450, 180)),
            WallBlock("16", Vector2(480, 180)),
            WallBlock("17", Vector2(510, 180)),
            WallBlock("18", Vector2(540, 180)),
            WallBlock("19", Vector2(570, 180)),
            WallBlock("20.1", Vector2(600, 180)),
            WallBlock("20", Vector2(630, 180)),
            WallBlock("24", Vector2(630, 300)),
            WallBlock("25", Vector2(630, 330)),
            WallBlock("26", Vector2(630, 360)),
            WallBlock("27", Vector2(630, 390)),
            WallBlock("28", Vector2(600, 300)),
            WallBlock("29", Vector2(570, 300)),
            WallBlock("30", Vector2(540, 300)),
            WallBlock("31", Vector2(540, 270)),
            WallBlock("32", Vector2(540, 240)),
            SkullNounBlock("SkullNounBlock", Vector2(540, 210)),
            FlagNounBlock("FlagNounBlock", Vector2(570, 210)),
            IsBlock("Is03", Vector2(570, 240)),
            DefeatVerbBlock("DefeatVerbBlock", Vector2(570, 270)),
            IsBlock("Is04", Vector2(600, 240)),
            WinVerbBlock("WinVerbBlock", Vector2(600, 270)),
            JellyNounBlock("JellyNounBlock", Vector2(630,210)),
            IsBlock("Is05", Vector2(630, 240)),
            PushVerbBlock("PushVerbBlock01", Vector2(630, 270)),

            RockNounBlock("RockNoun",  Vector2(510, 360)),
            IsBlock("Is06",  Vector2(540, 360)),
            PushVerbBlock("PushVerb",  Vector2(570, 360)),
        ]

        return units

    def load_picture(self):
        return "pics/map7.png"


class Map8():
    def load_map(self):
        units = [
            BabaBlock("testBaba", Vector2(360, 240)),
            RockBlock("testRock1", Vector2(420, 240)),

            WallBlock("test04", Vector2(240, 90)),
            WallBlock("test04", Vector2(270, 90)),
            WallBlock("test04", Vector2(300, 90)),
            WallBlock("test04", Vector2(330, 90)),
            WallBlock("test04", Vector2(360, 90)),
            WallBlock("test04", Vector2(390, 90)),
            WallBlock("test04", Vector2(420, 90)),
            WallBlock("test04", Vector2(450, 90)),
            WallBlock("test04", Vector2(480, 90)),
            WallBlock("test04", Vector2(510, 90)),
            WallBlock("test04", Vector2(540, 90)),

            WallBlock("test04", Vector2(540, 120)),
            WallBlock("test04", Vector2(540, 150)),
            WallBlock("test04", Vector2(540, 180)),
            WallBlock("test04", Vector2(540, 210)),
            WallBlock("test04", Vector2(540, 240)),

            WallBlock("test04", Vector2(570, 240)),
            WallBlock("test04", Vector2(600, 240)),
            WallBlock("test04", Vector2(630, 240)),

            WallBlock("test04", Vector2(630, 270)),
            WallBlock("test04", Vector2(630, 300)),
            WallBlock("test04", Vector2(630, 330)),
            WallBlock("test04", Vector2(630, 360)),
            WallBlock("test04", Vector2(630, 390)),
            WallBlock("test04", Vector2(630, 420)),

            WallBlock("test04", Vector2(630, 420)),
            WallBlock("test04", Vector2(600, 420)),
            WallBlock("test04", Vector2(570, 420)),
            WallBlock("test04", Vector2(540, 420)),
            WallBlock("test04", Vector2(510, 420)),
            WallBlock("test04", Vector2(480, 420)),
            WallBlock("test04", Vector2(450, 420)),
            WallBlock("test04", Vector2(420, 420)),
            WallBlock("test04", Vector2(390, 420)),
            WallBlock("test04", Vector2(360, 420)),
            WallBlock("test04", Vector2(330, 420)),
            WallBlock("test04", Vector2(300, 420)),
            WallBlock("test04", Vector2(270, 420)),
            WallBlock("test04", Vector2(240, 420)),

            WallBlock("test04", Vector2(240, 390)),
            WallBlock("test04", Vector2(240, 360)),
            WallBlock("test04", Vector2(240, 330)),
            WallBlock("test04", Vector2(240, 300)),
            WallBlock("test04", Vector2(240, 270)),
            WallBlock("test04", Vector2(240, 240)),
            WallBlock("test04", Vector2(240, 210)),
            WallBlock("test04", Vector2(240, 180)),
            WallBlock("test04", Vector2(240, 150)),
            WallBlock("test04", Vector2(240, 120)),

            BabaNounBlock("testBabaNoun", Vector2(360, 180)),
            IsBlock("testIs01", Vector2(390, 180)),
            YouVerbBlock("testYouVerb", Vector2(420, 180)),

            RockNounBlock("testRockNoun", Vector2(360, 300)),
            PushVerbBlock("testPushVerb", Vector2(420, 300)),

            WinVerbBlock("testWinVerb", Vector2(600, 150)),

            WallNounBlock("testWallNoun", Vector2(600, 300)),
            IsBlock("testIs03", Vector2(600, 330)),
            StopVerbBlock("testStopVerb", Vector2(600, 360)),
        ]

        return units

    def load_picture(self):
        return "pics/map8.png"


class Map9():
    def load_map(self):
        units = [
            BabaBlock("testBaba", Vector2(360, 240)),
            RockBlock("testRock1", Vector2(420, 240)),

            WallBlock("test04", Vector2(240, 90)),
            WallBlock("test04", Vector2(270, 90)),
            WallBlock("test04", Vector2(300, 90)),
            WallBlock("test04", Vector2(330, 90)),
            WallBlock("test04", Vector2(360, 90)),
            WallBlock("test04", Vector2(390, 90)),
            WallBlock("test04", Vector2(420, 90)),
            WallBlock("test04", Vector2(450, 90)),
            WallBlock("test04", Vector2(480, 90)),
            WallBlock("test04", Vector2(510, 90)),
            WallBlock("test04", Vector2(540, 90)),

            WallBlock("test04", Vector2(540, 120)),
            WallBlock("test04", Vector2(540, 150)),
            WallBlock("test04", Vector2(540, 180)),
            WallBlock("test04", Vector2(540, 210)),
            WallBlock("test04", Vector2(540, 240)),

            WallBlock("test04", Vector2(570, 240)),
            WallBlock("test04", Vector2(600, 240)),
            WallBlock("test04", Vector2(630, 240)),

            WallBlock("test04", Vector2(630, 270)),
            WallBlock("test04", Vector2(630, 300)),
            WallBlock("test04", Vector2(630, 330)),
            WallBlock("test04", Vector2(630, 360)),
            WallBlock("test04", Vector2(630, 390)),


            WallBlock("test04", Vector2(630, 420)),
            WallBlock("test04", Vector2(600, 420)),
            WallBlock("test04", Vector2(570, 420)),
            WallBlock("test04", Vector2(540, 420)),
            WallBlock("test04", Vector2(510, 420)),
            WallBlock("test04", Vector2(480, 420)),
            WallBlock("test04", Vector2(450, 420)),
            WallBlock("test04", Vector2(420, 420)),
            WallBlock("test04", Vector2(390, 420)),
            WallBlock("test04", Vector2(360, 420)),
            WallBlock("test04", Vector2(330, 420)),
            WallBlock("test04", Vector2(300, 420)),
            WallBlock("test04", Vector2(270, 420)),
            WallBlock("test04", Vector2(240, 420)),

            WallBlock("test04", Vector2(240, 390)),
            WallBlock("test04", Vector2(240, 360)),
            WallBlock("test04", Vector2(240, 330)),
            WallBlock("test04", Vector2(240, 300)),
            WallBlock("test04", Vector2(240, 270)),
            WallBlock("test04", Vector2(240, 240)),
            WallBlock("test04", Vector2(240, 210)),
            WallBlock("test04", Vector2(240, 180)),
            WallBlock("test04", Vector2(240, 150)),
            WallBlock("test04", Vector2(240, 120)),

            BabaNounBlock("testBabaNoun", Vector2(360, 180)),
            IsBlock("testIs01", Vector2(390, 180)),
            YouVerbBlock("testYouVerb", Vector2(420, 180)),

            RockNounBlock("testRockNoun", Vector2(360, 300)),
            IsBlock("testIs", Vector2(390, 300)),

            WinVerbBlock("testWinVerb", Vector2(600, 150)),

            WallNounBlock("testWallNoun", Vector2(600, 300)),
            IsBlock("testIs03", Vector2(600, 330)),
            StopVerbBlock("testStopVerb", Vector2(600, 360)),
        ]

        return units

    def load_picture(self):
        return "pics/map9.png"


class Map10():
    def load_map(self):
        units = [
            BabaBlock("testBaba", Vector2(240, 240)),
            KeyBlock("testkey", Vector2(180, 240)),

            WallBlock("test04", Vector2(120, 60)),
            WallBlock("test04", Vector2(150, 60)),
            WallBlock("test04", Vector2(180, 60)),
            WallBlock("test04", Vector2(210, 60)),
            WallBlock("test04", Vector2(240, 60)),

            WallBlock("test04", Vector2(120, 90)),
            BabaNounBlock("testBabaNoun", Vector2(150, 90)),
            IsBlock("testIs01", Vector2(180, 90)),
            YouVerbBlock("testYouVerb", Vector2(210, 90)),
            WallBlock("test04", Vector2(240, 90)),

            WallBlock("test04", Vector2(120, 120)),
            WallBlock("test04", Vector2(150, 120)),
            WallBlock("test04", Vector2(180, 120)),
            WallBlock("test04", Vector2(210, 120)),
            WallBlock("test04", Vector2(240, 120)),

            WallBlock("test04", Vector2(120, 150)),
            WallNounBlock("testWallNoun", Vector2(150, 150)),
            IsBlock("testIs03", Vector2(180, 150)),
            StopVerbBlock("testStopVerb", Vector2(210, 150)),
            WallBlock("test04", Vector2(240, 150)),

            WallBlock("test04", Vector2(120, 180)),
            WallBlock("test04", Vector2(120, 210)),
            WallBlock("test04", Vector2(120, 240)),
            WallBlock("test04", Vector2(120, 270)),
            WallBlock("test04", Vector2(120, 300)),
            WallBlock("test04", Vector2(150, 180)),
            WallBlock("test04", Vector2(180, 180)),
            WallBlock("test04", Vector2(210, 180)),
            WallBlock("test04", Vector2(240, 180)),
            WallBlock("test04", Vector2(270, 180)),
            WallBlock("test04", Vector2(300, 180)),
            WallBlock("test04", Vector2(150, 300)),
            WallBlock("test04", Vector2(180, 300)),
            WallBlock("test04", Vector2(210, 300)),
            WallBlock("test04", Vector2(240, 300)),
            WallBlock("test04", Vector2(270, 300)),
            WallBlock("test04", Vector2(300, 300)),
            WallBlock("test04", Vector2(300, 270)),
            DoorBlock("test04", Vector2(300, 240)),
            WallBlock("test04", Vector2(300, 210)),

            KeyNounBlock("keynoun", Vector2(240,360)),
            IsBlock("is",Vector2(270,360)),
            OpenVerbBlock("open",Vector2(300,360)),
            IsBlock("is", Vector2(240,390)),
            PushVerbBlock("push", Vector2(240,420)),

            RockBlock("rock",Vector2(360,240)),
            KeyBlock("key", Vector2(390, 240)),
            DoorBlock("door",Vector2(450,240)),
            RockNounBlock("rocknoun",Vector2(540,240)),
            DoorBlock("door", Vector2(540,300)),
            FlagBlock("flag",Vector2(540,360)),
            FlagNounBlock("testflagNoun", Vector2(510, 420)),
            IsBlock("testIs", Vector2(540, 420)),
            WinVerbBlock("win",Vector2(570,420)),

            WallBlock("wall",Vector2(450, 210)),
            WallBlock("wall", Vector2(450, 180)),
            WallBlock("wall", Vector2(480, 180)),
            WallBlock("wall", Vector2(480, 150)),
            WallBlock("wall", Vector2(480, 120)),

            WallBlock("wall", Vector2(480, 90)),
            WallBlock("wall", Vector2(480, 60)),
            WallBlock("wall", Vector2(510, 60)),
            WallBlock("wall", Vector2(540, 60)),
            WallBlock("wall", Vector2(570, 60)),
            WallBlock("wall", Vector2(600, 60)),
            WallBlock("wall", Vector2(600, 90)),
            DoorNounBlock("doornoun",Vector2(510,90)),
            IsBlock("is",Vector2(540,90)),
            ShutVerbBlock("stop", Vector2(570, 90)),
            WallBlock("wall", Vector2(600, 120)),
            WallBlock("wall", Vector2(600, 150)),
            WallBlock("wall", Vector2(600, 180)),
            WallBlock("wall", Vector2(570, 120)),
            WallBlock("wall", Vector2(540, 120)),
            WallBlock("wall", Vector2(510, 120)),
            DoorNounBlock("doornoun",Vector2(510,150)),
            IsBlock("is", Vector2(540, 150)),
            StopVerbBlock("stop", Vector2(570, 150)),

            WallBlock("wall", Vector2(510, 180)),
            WallBlock("wall", Vector2(540, 180)),
            WallBlock("wall", Vector2(570, 180)),
            WallBlock("wall", Vector2(600, 180)),
            WallBlock("wall", Vector2(630, 180)),
            WallBlock("wall", Vector2(630, 210)),
            WallBlock("wall", Vector2(630, 240)),
            WallBlock("wall", Vector2(630, 270)),
            WallBlock("wall", Vector2(630, 300)),
            WallBlock("wall", Vector2(600, 300)),
            WallBlock("wall", Vector2(570, 300)),
            WallBlock("wall", Vector2(510, 300)),
            WallBlock("wall", Vector2(480, 300)),
            WallBlock("wall", Vector2(450, 300)),
            WallBlock("wall", Vector2(450, 270)),
            WallBlock("wall", Vector2(450, 330)),
            WallBlock("wall", Vector2(450, 360)),
            WallBlock("wall", Vector2(450, 390)),
            WallBlock("wall", Vector2(480, 390)),
            WallBlock("wall", Vector2(480, 420)),
            WallBlock("wall", Vector2(480, 450)),
            WallBlock("wall", Vector2(510, 450)),
            WallBlock("wall", Vector2(540, 450)),
            WallBlock("wall", Vector2(570, 450)),
            WallBlock("wall", Vector2(600, 450)),
            WallBlock("wall", Vector2(600, 420)),
            WallBlock("wall", Vector2(600, 390)),
            WallBlock("wall", Vector2(600, 360)),
            WallBlock("wall", Vector2(600, 330)),

        ]

        return units

    def load_picture(self):
        return "pics/map10.png"


class Map11():
    def load_map(self):
        units = [
            BabaNounBlock("babanoun", Vector2(0, 0)),
            IsBlock("is01", Vector2(30, 0)),
            YouVerbBlock("youverb", Vector2(60, 0)),
            WallBlock("wall", Vector2(90, 0)),
            WallBlock("wall", Vector2(900, 0)),
            WallBlock("wall", Vector2(870, 0)),
            WallBlock("wall", Vector2(840, 0)),
            WallBlock("wall", Vector2(0, 30)),
            WallBlock("wall", Vector2(30, 30)),
            WallBlock("wall", Vector2(60, 30)),
            WallBlock("wall", Vector2(90, 30)),
            WallBlock("wall", Vector2(900, 30)),
            DefeatVerbBlock("defeat", Vector2(870, 30)),
            IsBlock("is02", Vector2(840, 30)),
            KeyNounBlock("keynoun", Vector2(810, 30)),
            DoorNounBlock("doornoun", Vector2(0, 60)),
            IsBlock("is03", Vector2(30, 60)),
            StopVerbBlock("stop", Vector2(60, 60)),
            WallBlock("wall", Vector2(90, 60)),
            WallBlock("wall", Vector2(900, 60)),
            WallBlock("wall", Vector2(870, 60)),
            WallBlock("wall", Vector2(840, 60)),
            WallBlock("wall", Vector2(0, 90)),
            WallBlock("wall", Vector2(30, 90)),
            WallBlock("wall", Vector2(60, 90)),
            WallBlock("wall", Vector2(90, 90)),
            WallBlock("wall", Vector2(900, 90)),
            WallBlock("wall", Vector2(840, 90)),
            WallBlock("wall", Vector2(810, 90)),

            IsBlock("is04", Vector2(390, 180)),
            WinVerbBlock("win", Vector2(450, 180)),

            SkullNounBlock("skullnoun", Vector2(270, 270)),
            IsBlock("is05", Vector2(300, 270)),
            PushVerbBlock("push", Vector2(330, 270)),
            KeyBlock("key", Vector2(330, 360)),
            KeyNounBlock("keynoun", Vector2(300, 420)),
            IsBlock("is07", Vector2(330, 420)),
            OpenVerbBlock("open", Vector2(360, 420)),
            StopVerbBlock("stop", Vector2(540, 270)),
            IsBlock("is06", Vector2(510, 270)),
            WallBlock("wall", Vector2(510, 300)),
            SkullBlock("skull", Vector2(480, 360)),
            BabaBlock("baba", Vector2(450, 420)),
            IsBlock("is08", Vector2(480, 420)),
            ShutVerbBlock("shut", Vector2(510, 420)),
            WallNounBlock("wallnoun", Vector2(480, 270)),

            DoorBlock("door", Vector2(420, 240)),
            WallBlock("l-u", Vector2(240, 240)),
            WallBlock("l-u", Vector2(270, 240)),
            WallBlock("l-u", Vector2(300, 240)),
            WallBlock("l-u", Vector2(330, 240)),
            WallBlock("l-u", Vector2(360, 240)),
            WallBlock("l-u", Vector2(390, 240)),
            # WallBlock("l-u", Vector2(420, 240)),
            WallBlock("l-u", Vector2(450, 240)),
            WallBlock("l-u", Vector2(480, 240)),
            WallBlock("l-u", Vector2(510, 240)),
            WallBlock("l-u", Vector2(540, 240)),
            WallBlock("r-u", Vector2(570, 240)),

            WallBlock("r-b", Vector2(570, 270)),
            WallBlock("r-b", Vector2(570, 300)),
            WallBlock("r-b", Vector2(570, 330)),
            WallBlock("r-b", Vector2(570, 360)),
            WallBlock("r-b", Vector2(570, 390)),
            WallBlock("r-b", Vector2(570, 420)),
            WallBlock("r-b", Vector2(570, 450)),
            WallBlock("r-b", Vector2(570, 480)),
            WallBlock("r-b", Vector2(570, 510)),

            WallBlock("r-b", Vector2(540, 510)),
            WallBlock("r-b", Vector2(510, 510)),
            WallBlock("r-b", Vector2(480, 510)),
            WallBlock("r-b", Vector2(450, 510)),
            WallBlock("r-b", Vector2(420, 510)),
            WallBlock("r-b", Vector2(390, 510)),
            WallBlock("r-b", Vector2(360, 510)),
            WallBlock("r-b", Vector2(330, 510)),
            WallBlock("r-b", Vector2(300, 510)),
            WallBlock("r-b", Vector2(270, 510)),
            WallBlock("l-b", Vector2(240, 510)),

            WallBlock("l-b", Vector2(240, 480)),
            WallBlock("l-b", Vector2(240, 450)),
            WallBlock("l-b", Vector2(240, 420)),
            WallBlock("l-b", Vector2(240, 390)),
            WallBlock("l-b", Vector2(240, 360)),
            WallBlock("l-b", Vector2(240, 330)),
            WallBlock("l-b", Vector2(240, 300)),
            WallBlock("l-b", Vector2(240, 270)),

        ]

        return units

    def load_picture(self):
        return "pics/map11.png"


class MapAbout:
    def load_map(self):
        units = [
            AboutPicture("test", Vector2(160, 70))
        ]

        return units

    def load_picture(self):
        return "pics/mapMain.png"
