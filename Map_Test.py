import pygame

from Blocks import *

units = [
    BabaBlock("baba", False, False, True, True, Vector2(360, 270), 'pics/baba_0_1.png'),

    BabaNounBlock("text_baba", True, False, True, False, Vector2(270, 150), 'pics/text_baba_0_1.png', 'baba'),
    IsBlock("text_is1", True, False, True, False, Vector2(300, 150), 'pics/text_is_0_1.png', 'is'),
    YouVerbBlock("text_you", True, False, True, False, Vector2(330, 150), 'pics/text_you_0_1.png', 'you'),

    RockBlock("rock1", False, False, True, False, Vector2(690, 150), 'pics/rock_0_1.png'),
    RockBlock("rock2", False, False, True, False, Vector2(660, 150), 'pics/rock_0_1.png'),
    RockBlock("rock3", False, False, True, False, Vector2(690, 180), 'pics/rock_0_1.png'),
    RockBlock("rock4", False, False, True, False, Vector2(660, 180), 'pics/rock_0_1.png'),
    RockNounBlock("text_rock", True, False, True, False, Vector2(540, 150), 'pics/text_rock_0_1.png', 'rock'),
    IsBlock("text_is2", True, False, True, False, Vector2(570, 150), 'pics/text_is_0_1.png', 'is'),
    PushVerbBlock("text_push", True, False, True, False, Vector2(600, 150), 'pics/text_push_0_1.png', 'push'),

    WallBlock("wall1", False, False, False, True, Vector2(420, 390), 'pics/wall_1_1.png'),
    WallBlock("wall2", False, False, False, True, Vector2(420, 360), 'pics/wall_4_1.png'),
    WallBlock("wall3", False, False, False, True, Vector2(390, 390), 'pics/wall_1_1.png'),
    WallBlock("wall4", False, False, False, True, Vector2(390, 360), 'pics/wall_4_1.png'),
    WallNounBlock("text_wall", True, False, True, False, Vector2(270, 390), 'pics/text_wall_0_1.png', 'wall'),
    IsBlock("text_is3", True, False, True, False, Vector2(300, 390), 'pics/text_is_0_1.png', 'is'),
    StopVerbBlock("text_stop", True, False, True, False, Vector2(330, 390), 'pics/text_stop_0_1.png', 'stop'),
    FlagBlock("flag1", False, True, True, False, Vector2(660, 390), 'pics/flag_0_1.png'),
    FlagBlock("flag2", False, True, True, False, Vector2(660, 360), 'pics/flag_0_1.png'),
    FlagBlock("flag3", False, True, True, False, Vector2(690, 390), 'pics/flag_0_1.png'),
    FlagBlock("flag4", False, True, True, False, Vector2(690, 360), 'pics/flag_0_1.png'),
    FlagNounBlock("text_flag", True, False, True, False, Vector2(540, 390), 'pics/text_flag_0_1.png', 'flag'),
    IsBlock("text_is4", True, False, True, False, Vector2(570, 390), 'pics/text_is_0_1.png', 'is'),
    WinVerbBlock("text_win", True, False, True, False, Vector2(600, 390), 'pics/text_win_0_1.png', 'win'),
]