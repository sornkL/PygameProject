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
            # WeakVerbBlock("testWeak", Vector2(600, 450)),
            DefeatVerbBlock("testDefeat", Vector2(600, 510)),
            WeakVerbBlock("test", Vector2(660, 510))
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


class MapHard():
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


class Map3():
    def load_map(self):
        units = [

            #临时墙
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
            #结束墙

            BabaBlock("Baba", Vector2(330, 180)),
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

        ]

        return units