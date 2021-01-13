
This is a repository for the final assignment of "Introduction to Computer Science".<br />

Todo lists: <br />
1. （已实现） transform 的具体实现，以实现Noun-is-Noun的复杂谓词分析并转换方块的属性; <br />
2. （已实现）其余动词(Settings.py中的VERB_WORD_BANK)的具体实现; <br />
3. （已实现） 方块的动画效果，包括颜色、贴图转换等; <br />
4. （已实现）游戏界面与关卡设计 <br />

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
**11. 2020-12-23** <br />
更新 选关界面与游戏操作的提示; <br />
**12. 2020-12-24** <br />
修复 方块可能被推出游戏界面的错误; <br />
**13. 2020-12-29** <br />
新增 数据统计文件Statistics.json，现在支持每个关卡胜利次数和失败次数的统计，以及每个关卡首次通关的时间统计; <br />
**14. 2021-01-05** <br />
新增 3张地图Map8, Map9, Map10; <br/>
新增 open与shut属性，现在支持使用具有open属性的方块打开具有shut属性的方块，二者在接触时会同时消失; <br />
更新 move()函数以支持新增的open与shut属性; <br />
更新 Statistics.json以支持新增地图的数据统计; <br />
修复 move()函数在没有玩家键盘输入的情况下仍然被调用可能产生的错误; <br />
**15. 2021-01-07** <br />
更新 open, shut, key, door的贴图与动画效果; <br />
更新 背景音乐，主菜单、游戏关卡与About界面具备不同的音乐; <br />
重构 main.py，现在移除了冗余的代码; <br />
**16. 2021-01-10** <br />
新增 关卡开始时的过场动画，现在支持按下任意键跳过动画; <br />
修复 在控制方块时BaBa可能不能被正确显示透明度的问题; <br />
**17. 2021-01-11** <br />
新增 statistics_display()函数以支持游戏统计数据的显示，现在每关过场动画处会显示游戏统计数据; <br />
更新 主界面选关，现在一共支持11个关卡的选择; <br />
修复 可能导致贴图材质层叠问题的错误; <br />

Important Notes:
**这是本项目的最后一次更新，从2021年1月13日起将停止维护！**