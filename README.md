
This is a repository for the final assignment of "Introduction to Computer Science".<br />

Update logs:
1. 2020-12-04 更新 README.md
2. 2020-12-06 更新 测试贴图（pics/），重写 update()用于支持碰撞检测，重写 BaseBlock以继承pygame.sprite.Sprite的属性
3. 2020-12-07 更新 GameRule，实现获取特定方块四个方向上的方块信息
4. 2020-12-08 重构碰撞检测，包括BaseBlock在内的所有方块不再继承pygame.sprite.Sprite，重构后的碰撞检测可以处理带条件的复杂功能；
重构后的碰撞检测可以被用来进行复杂的词法（谓词）分析；
更新 Blocks类；
更新 WorldMap地图；
更新 GameRuleObserver()以部分实现词法分析与胜利条件判定
5. 2020-12-09 新增 贴图测试集（pics_test/），所有贴图大小调整至30x30