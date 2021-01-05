from pygame.math import Vector2

VERSION = "1.1.1"  # 游戏版本号
GAME_TITLE = "BaBa is You 2077"  # 游戏标题

WORLD_MAX_X = 30  # 地图x轴边界方块个数
WORLD_MAX_Y = 20  # 地图y轴边界方块个数

CELL_SIZE_X = 30  # 每个方块长度
CELL_SIZE_Y = 30  # 每个方块宽度

BACKGROUND_COLOR = (0, 0, 0)  # 背景颜色，黑色
ALPHA = 120  # 不透明度，越低越透明
NO_ALPHA = 255  # 不透明时的ALPHA值
WALL_COLOR = 'black'  # 墙的默认颜色

LEFT_DIRECTION = Vector2(-CELL_SIZE_X, 0)  # 左侧
TOP_DIRECTION = Vector2(0, -CELL_SIZE_Y)  # 上侧
RIGHT_DIRECTION = Vector2(CELL_SIZE_X, 0)  # 右侧
BOTTOM_DIRECTION = Vector2(0, CELL_SIZE_Y)  # 下侧
DIRECTION = [TOP_DIRECTION, BOTTOM_DIRECTION, LEFT_DIRECTION, RIGHT_DIRECTION]  # 四个方向，按照"上下左右"的顺序存放

VERB_WORD_BANK = ['defeat', 'hot', 'is', 'open', 'push', 'shut', 'stop', 'weak', 'win', 'you']  # 动词词库
NOUN_WORD_BANK = ['baba', 'door', 'flag', 'jelly', 'key', 'lava', 'rock', 'skull', 'wall']  # 名词词库

STATISTICS_FILE_PATH = "Statistics.json"  # 数据统计文件的相对路径
