
This is a repository for the final assignment of "Introduction to Computer Science".<br />

Todo lists:
1. <u>实现中</u> transform 的具体实现，以实现Noun-is-Noun的复杂谓词分析并转换方块的属性; <br />
2. 其余动词(Settings.py中的VERB_WORD_BANK)的具体实现; <br />
3. <u>实现中</u> 方块的动画效果，包括颜色、贴图转换等; <br />

Update logs:
1. 2020-12-04 更新 README.md
2. 2020-12-06 更新 测试贴图（pics/），重写 update()用于支持碰撞检测，重写 BaseBlock以继承pygame.sprite.Sprite的属性
3. 2020-12-07 更新 GameRule，实现获取特定方块四个方向上的方块信息
4. 2020-12-08 重构碰撞检测，包括BaseBlock在内的所有方块不再继承pygame.sprite.Sprite，重构后的碰撞检测可以处理带条件的复杂功能；<br />
重构后的碰撞检测可以被用来进行复杂的词法（谓词）分析；<br />
更新 Blocks类；<br />
更新 WorldMap地图；<br />
更新 GameRuleObserver()以部分实现词法分析与胜利条件判定 <br />
5. 2020-12-09 新增 贴图测试集（pics_test/），所有贴图大小调整至30x30
6. 2020-12-14 分离 WorldMap.py的各模块（拆分成WorldMap/UserInterface, Map1, GameState等模块）; <br />
新增 BaseBlock基类的passable属性，表示方块是否能被穿过; <br />
重构 碰撞检测，以根据passable属性判断并实现方块的穿越; <br />
更新 GameRuleObserver()以实现对特定语法方块(stop, push, you)的谓词分析(_is_grammar_valid())与属性赋予（endow()）<br />
更新碰撞检测，更新 GameRuleObserver()以实现胜利条件的复杂判定 <br />
