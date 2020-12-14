import pygame

from Blocks import *

units = [
    BabaBlock("testBaba", False, False, True, True, Vector2(360, 270), 'pics/baba_0_1.png'),

    WallBlock("test04", False, True, False, False, Vector2(240, 210), 'pics/wall_1_1.png'),
    WallBlock("test04", False, True, False, False, Vector2(270, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(300, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(330, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(360, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(390, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(420, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(450, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(480, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(510, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(540, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(570, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(600, 210), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(630, 210), 'pics/wall_4_1.png'),
    WallBlock("test04", False, True, False, False, Vector2(240, 330), 'pics/wall_1_1.png'),
    WallBlock("test04", False, True, False, False, Vector2(270, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(300, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(330, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(360, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(390, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(420, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(450, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(480, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(510, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(540, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(570, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(600, 330), 'pics/white_test.png'),
    WallBlock("test04", False, True, False, False, Vector2(630, 330), 'pics/wall_4_1.png'),

    RockBlock("testRock1", False, False, True, False, Vector2(510, 300), 'pics/rock_0_1.png'),
    RockBlock("testRock2", False, False, True, False, Vector2(510, 270), 'pics/rock_0_1.png'),
    RockBlock("testRock3", False, False, True, False, Vector2(510, 240), 'pics/rock_0_1.png'),

    FlagBlock("test04", False, False, True, False, Vector2(570, 270), 'pics/flag_0_1.png'),

    BabaNounBlock("testBabaNoun", True, False, True, False, Vector2(270, 150), 'pics/text_baba_0_1.png', 'baba'),
    IsBlock("testIs01", True, False, True, False, Vector2(300, 150), 'pics/text_is_0_1.png', 'is'),
    YouVerbBlock("testYouVerb", True, False, True, False, Vector2(330, 150), 'pics/text_you_0_1.png', 'you'),

    RockNounBlock("testRockNoun", True, False, True, False, Vector2(540, 150), 'pics/text_rock_0_1.png', 'rock'),
    IsBlock("testIs02", True, False, True, False, Vector2(570, 150), 'pics/text_is_0_1.png', 'is'),
    PushVerbBlock("testPushVerb", True, False, True, False, Vector2(600, 150), 'pics/text_push_0_1.png', 'push'),

    WallNounBlock("testWallNoun", True, False, True, False, Vector2(270, 390), 'pics/text_wall_0_1.png', 'wall'),
    IsBlock("testIs03", True, False, True, False, Vector2(300, 390), 'pics/text_is_0_1.png', 'is'),
    StopVerbBlock("testStopVerb", True, False, True, False, Vector2(330, 390), 'pics/text_stop_0_1.png', 'stop'),

    FlagNounBlock("testFlagNoun", True, False, True, False, Vector2(540, 390), 'pics/text_flag_0_1.png', 'flag'),
    IsBlock("testIs04", True, False, True, False, Vector2(570, 390), 'pics/text_is_0_1.png', 'is'),
    WinVerbBlock("testWinVerb", True, False, True, False, Vector2(600, 390), 'pics/text_win_0_1.png', 'win'),
]
