
This is a repository for the final assignment of "Introduction to Computer Science".<br />

Todo lists: <br />
1. （已实现） transform 的具体实现，以实现Noun-is-Noun的复杂谓词分析并转换方块的属性; <br />
2. （已实现）其余动词(Settings.py中的VERB_WORD_BANK)的具体实现; <br />
3. （已实现） 方块的动画效果，包括颜色、贴图转换等; <br />
4. （实现中）游戏界面与关卡设计 <br />

Update logs: <br />
**1. 2020-12-04** <br />
更新 README.md<br />
**2. 2020-12-06** <br />
更新 测试贴图（pics/），重写 update()用于支持碰撞检测，重写 BaseBlock以继承pygame.sprite.Sprite的属性<br />
**3. 2020-12-07** <br />
更新 GameRule，实现获取特定方块四个方向上的方块信息<br />
**4. 2020-12-08** <br />
重构 碰撞检测，包括BaseBlock在内的所有方块不再继承pygame.sprite.Sprite，重构后的碰撞检测可以处理带条件的复杂功能，重构后的碰撞检测可以被用来进行复杂的词法（谓词）分析;<br />
更新 Blocks类;<br />
更新 WorldMap地图;<br />
更新 GameRuleObserver()以部分实现词法分析与胜利条件判定 <br />
**5. 2020-12-09** <br />
新增 贴图测试集（pics_test/），所有贴图大小调整至30x30<br />
**6. 2020-12-14** <br />
分离 WorldMap.py的各模块（拆分成WorldMap/UserInterface, Map1, GameState等模块）; <br />
新增 BaseBlock基类的passable属性，表示方块是否能被穿过; <br />
重构 碰撞检测，以根据passable属性判断并实现方块的穿越; <br />
更新 GameRuleObserver()以实现对特定语法方块(stop, push, you)的谓词分析(_is_grammar_valid())与属性赋予（endow()）;<br />
更新 碰撞检测，更新 GameRuleObserver()以实现胜利条件的复杂判定; <br />
修复 状态流更新(_update_state())可能导致的bug <br />
**7. 2020-12-15** <br />
新增 Map2作为第二张地图，现在所有地图置于MapLoader中; <br />
新增 动画/贴图效果，贴图可以由属性值而改变其透明度，BaBa在移动时可以由方向而改变贴图; <br />
重构 BaseBlock, Blocks以支持复杂的动画/贴图效果; <br />
更新 is_win()函数用于胜利条件的检测，返回值将修改gameState中的playerState; <br />
更新 WorldMap/UserInterface，构造UserInterface()时现在需要传入地图方块的参数用于地图的加载; <br />
更新 GameRuleObserver()以实现名词方块的转换（transform()）; <br />
更新 _is_noun_grammar_valid()以实现Noun-is-Noun的谓词分析，现在_is_grammar_valid()更名为_is_verb_grammar_valid()以实现Noun-is-Verb的谓词分析; <br />
修复 碰撞检测时方块无法被推越passable=True的方块的bug <br />
**8. 2020-12-16** <br />
新增 is_lose()函数用于死亡条件的检测，返回值将修改gameState中的aliveState; <br />
更新 GameRuleObserver()以实现对特定语法方块(weak, defeat)的属性赋予(_endow_is_weak(), _endow_is_defeat(), endow())，现在weak方块可以使该方块在被碰触时消失，defeat方块可以使触碰者消失; <br />
更新 weak属性(VERB_WORD_BANK中)与WeakVerbBlock(Blocks中)以支持weak的判定; <br />
更新 defeat属性(VERB_WORD_BANK中)以支持defeat的判定; <br />
更新 SkullBlock, WallBlock, 语法方块（暂不包含Weak和Defeat）动画/贴图效果; <br />
修复 transform()无法变换不在场方块的错误; <br />
**9. 2020-12-17** <br />
分离 UserInterface（WorldMap现在更名为UserInterface），现在程序的主入口被置于main.py中; <br />
新增 Map3、Map4、Map5、MapHard、MapHell地图; <br />
新增 JellyBlock及其语法方块; <br />
修复 RockBlock, SkullBlock的passable初始属性，现在都为True; <br />
修复 多个方块具有同样属性时可能导致赋予部分方块属性时失效的错误; <br />
修复 transform()无法变换从未出现过的方块时会产生的错误; <br />
**10. 2020-12-21** <br />
重构 main.py，现在支持简单的选关操作和游戏退出操作; <br />
新增 R键重新开始当前关卡，空格(Space)键回到选关主界面; <br />
更新 GameRuleObserver()的_is_verb_grammar_valid()与_is_noun_grammar_valid()函数，现在支持当语法方块满足词法后会变成高亮显示，反之则添加透明度表示词法不成立; <br />
修复 多个函数（is_win(), _is_defeat(), _is_weak()等）参数接口调用错误可能导致语法方块高亮失效的错误; <br />
