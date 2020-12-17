import copy
import pygame

import MapLoader

from typing import Union
from pygame.math import Vector2

from Blocks import *
from GameState import *

stopStateStream = {}
pushStateStream = {}
youStateStream = {}
winStateStream = {}
weakStateStream = {}
defeatStateStream = {}


class GameRuleObserver():
    def __init__(self, gameState):
        self._gameState = gameState

    def _is_inside_map(self, coordinate: Vector2) -> bool:
        """
        :param coordinate: 方块的坐标，Vector2类型
        :return: 返回方块是否在地图的范围内
        """
        if coordinate.x < 0 or coordinate.x >= WORLD_MAX_X*CELL_SIZE_X \
                or coordinate.y < 0 or coordinate.y >= WORLD_MAX_Y*CELL_SIZE_Y:
            return False
        else:
            return True

    def _is_exist(self, objectBlock: Union[GeneralBlock], direction: Vector2) -> Union[None, GeneralBlock]:
        """
        :param objectBlock: 某个特定的方块
        :param direction: 紧挨着object的方向
        :return: 返回object的direction方向是否有其他方块
                 除非返回None，否则返回一个特定block类型的数据，表示object在direction方向的方块信息
        """

        if direction != Vector2(0, 0):
            _newLocation = objectBlock.location + direction
            for unit in self._gameState.units:
                if unit.location == _newLocation and not unit.is_pass():
                    return unit
                else:
                    continue

    def _is_exist_line(self, objectBlock, direction) -> list:
        """
        :param objectBlock: 某个特定的方块
        :param direction: 紧挨着object的方向
        :return: 返回一个列表，元素依次表示方块沿direction方向的所有连续方块数据
        """

        nextBlock = self._is_exist(objectBlock, direction)
        lineBlockList = []
        while nextBlock is not None and not nextBlock.is_pass():
            lineBlockList.append(nextBlock)
            nextBlock = self._is_exist(nextBlock, direction)

        return lineBlockList

    def _observe(self, objectBlock: Union[GeneralBlock]) -> Union[list]:
        """
        :param objectBlock: 某个特定的方块
        :return: 按照"上下左右"的顺序返回被观察的方块四个方向上的方块数据，若某个方向上没有方块，则为None
        """

        blocksAroundList = []
        for direction in DIRECTION:
            blocksAroundList.append(self._is_exist(objectBlock, direction))

        return blocksAroundList

    def _is_collide(self, objectBlock, direction: Vector2) -> bool:
        """
        :param objectBlock: 某个特定的方块
        :param direction: 移动的方向
        :return: 返回True表示有碰撞
        """

        blockDirection = self._is_exist(objectBlock, direction)
        if blockDirection is not None and not blockDirection.is_move() and not blockDirection.is_pass():
            return True
        else:
            return False

    def _push(self, objectBlock, direction: Vector2):
        """
        当方块沿某个特定方向准备移动时，如果方向上有moveable=True的方块，则调用此函数进行移动
        :param objectBlock: 某个特定的方块
        :param direction: 移动方向
        :return: 无返回值，直接修改gameState中的方块位置
        """
        nextBlockLine = self._is_exist_line(objectBlock, direction)
        isPushSign = True

        for block in nextBlockLine:
            if not self._is_inside_map(block.location) or not block.is_move():
                isPushSign = False
                break

        if isPushSign:
            objectBlock.location += direction
            for block in nextBlockLine:
                block.location += direction

    def move(self, objectBlock: Union[GeneralBlock], direction: Vector2):
        """
        :param objectBlock: 某个特定的方块
        :param direction: 移动的方向
        :return: 无返回值，直接修改gameState中的方块位置
        """
        if objectBlock.is_move() and objectBlock.is_control():
            _newLocation = objectBlock.location + direction
            if type(objectBlock) == BabaBlock:
                objectBlock.change_direction(direction)

            if self._is_inside_map(_newLocation):
                nextBlock = self._is_exist(objectBlock, direction)
                if nextBlock is None or nextBlock.is_pass():
                    objectBlock.location = _newLocation
                else:
                    if not self._is_collide(objectBlock, direction):
                        self._push(objectBlock, direction)

    def _is_verb_grammar_valid(self, objectBlock: Union[GeneralBlock]) -> list:
        """
        :param objectBlock: is方块（IsBlock）
        :return: 如果谓词分析后，上-is-下（或左-is-右）合法（Noun. + is + Verb.），则返回前后方块的信息，否则返回None
        """

        _isGrammarValid = [None] * 4
        _blocksAroundList = self._observe(objectBlock)
        for i in range(0, len(_blocksAroundList), 2):
            _firstBlock = _blocksAroundList[i]
            _secondBlock = _blocksAroundList[i+1]
            if _firstBlock is not None and _secondBlock is not None:
                if _firstBlock._text and _secondBlock._text:
                    if _firstBlock.word in NOUN_WORD_BANK and _secondBlock.word in VERB_WORD_BANK:
                        _isGrammarValid[i] = _firstBlock
                        _isGrammarValid[i+1] = _secondBlock

        return _isGrammarValid

    def _is_noun_grammar_valid(self, objectBlock: Union[GeneralBlock]) -> list:
        """
        谓词分析：对谓词"is"的四个方向进行检测，上-is-下（或左-is-右）可以继续进行谓词分析
        :return:
        """
        _isGrammarValid = [None] * 4
        _blocksAroundList = self._observe(objectBlock)
        for i in range(0, len(_blocksAroundList), 2):
            _firstBlock = _blocksAroundList[i]
            _secondBlock = _blocksAroundList[i + 1]
            if _firstBlock is not None and _secondBlock is not None:
                if _firstBlock._text and _secondBlock._text:
                    if _firstBlock.word in NOUN_WORD_BANK and _secondBlock.word in NOUN_WORD_BANK:
                        _isGrammarValid[i] = _firstBlock
                        _isGrammarValid[i + 1] = _secondBlock

        return _isGrammarValid

    def is_win(self, objectBlockList: list) -> bool:
        """
        其中一种胜利判定方式，即"xx is win", "xx is you"时xx的方块类型一致；
        另一种胜利判定方法，接触时即做判定（2020-12-15Update，从move()中移除，改写至is_win()中）
        :param objectBlockList: 所有待判断的方块，一般是GameState().units
        :return: True表示获得胜利，游戏状态playerState变为False
        """

        _winSign = "win"
        _youSign = "you"
        _compareList = []
        _controllableBlockLocationList = []
        _controllableBlockNameList = []

        for isBlock in objectBlockList:
            _isGrammarValid = self._is_verb_grammar_valid(isBlock)
            for i in range(0, len(_isGrammarValid), 2):
                if _isGrammarValid[i] is None:
                    continue
                else:
                    if _winSign == _isGrammarValid[i+1].word or _youSign == _isGrammarValid[i+1].word:
                        _compareList.append(_isGrammarValid[i])

        if len(_compareList):
            if len(_compareList) == 2 and _compareList[0].word == _compareList[1].word:
                return True
            else:
                for unit in self._gameState.units:
                    if unit.is_control():
                        _controllableBlockLocationList.append(unit.location)
                        if type(unit).__name__ not in _controllableBlockNameList:
                            _controllableBlockNameList.append(type(unit).__name__)

                for unit in self._gameState.units:
                    if unit.location in _controllableBlockLocationList and type(unit) not in _controllableBlockNameList:
                        for blockNounName in winStateStream:
                            if winStateStream[blockNounName]:
                                targetBlockName = "".join(blockNounName.split('Noun'))
                                if type(unit).__name__ == targetBlockName:
                                    return True

    def is_lose(self, objectBlockList: list) -> bool:
        """
        当且仅当场上没有任何方块可以被控制时判定游戏失败
        :param objectBlockList: 所有待判断的方块，一般是GameState().units
        :return: True表示失败，控制状态aliveState变为False
        """

        _isLose = True

        for unit in objectBlockList:
            if unit.is_control():
                _isLose = False

        return _isLose

    def _is_weak(self, objectBlockList: list) -> Union[bool, tuple]:
        """
        :param objectBlockList: 所有待判断的方块，一般是GameState().units
        :return: True表示方块weak，额外返回一个list表示待移除的方块列表
        """

        _defeatSign = "weak"
        _youSign = "you"
        _compareList = []
        _controllableBlockLocationList = []
        _controllableBlockNameList = []
        _removeBlockList = []

        for isBlock in objectBlockList:
            _isGrammarValid = self._is_verb_grammar_valid(isBlock)
            for i in range(0, len(_isGrammarValid), 2):
                if _isGrammarValid[i] is None:
                    continue
                else:
                    if _defeatSign == _isGrammarValid[i+1].word or _youSign == _isGrammarValid[i+1].word:
                        _compareList.append(_isGrammarValid[i])

        if len(_compareList):
            if len(_compareList) == 2 and _compareList[0].word == _compareList[1].word:
                removeBlockNounName = type(_compareList[0]).__name__
                removeBlockName = "".join(removeBlockNounName.split('Noun'))
                for unit in self._gameState.units:
                    if type(unit).__name__ == removeBlockName:
                        _removeBlockList.append(unit)
                return True, _removeBlockList
            else:
                for unit in self._gameState.units:
                    if unit.is_control():
                        _controllableBlockLocationList.append(unit.location)
                        if type(unit).__name__ not in _controllableBlockNameList:
                            _controllableBlockNameList.append(type(unit).__name__)

                for unit in self._gameState.units:
                    if unit.location in _controllableBlockLocationList and type(unit) not in _controllableBlockNameList:
                        for blockNounName in weakStateStream:
                            if weakStateStream[blockNounName]:
                                targetBlockName = "".join(blockNounName.split('Noun'))
                                if type(unit).__name__ == targetBlockName:
                                    _removeBlockList.append(unit)
                return True, _removeBlockList
        else:
            return False, _removeBlockList

    def _is_defeat(self, objectBlockList: list) -> Union[bool, tuple]:
        """
        :param objectBlockList: 所有待判断的方块，一般是GameState().units
        :return: True表示方块weak，额外返回一个list表示待移除的方块列表
        """

        _defeatSign = "defeat"
        _youSign = "you"
        _compareList = []
        _defeatBlockLocationList = []
        _removeBlockList = []
        _targetDefeatBlockName = ""

        for isBlock in objectBlockList:
            _isGrammarValid = self._is_verb_grammar_valid(isBlock)
            for i in range(0, len(_isGrammarValid), 2):
                if _isGrammarValid[i] is None:
                    continue
                else:
                    if _defeatSign == _isGrammarValid[i+1].word or _youSign == _isGrammarValid[i+1].word:
                        _compareList.append(_isGrammarValid[i])

        if len(_compareList):
            if len(_compareList) == 2 and _compareList[0].word == _compareList[1].word:
                for unit in self._gameState.units:
                    targetSubjectBlockName = "".join(type(_compareList[0]).__name__.split('Noun'))
                    if type(unit).__name__ == targetSubjectBlockName:
                        _removeBlockList.append(unit)
                return True, _removeBlockList
            else:
                for blockNounName in defeatStateStream:
                    if defeatStateStream[blockNounName]:
                        targetBlockName = "".join(blockNounName.split('Noun'))
                        _targetDefeatBlockName = targetBlockName
                        for unit in self._gameState.units:
                            if type(unit).__name__ == targetBlockName:
                                _defeatBlockLocationList.append(unit.location)
                for unit in self._gameState.units:
                    if unit.location in _defeatBlockLocationList and type(unit).__name__ != _targetDefeatBlockName:
                        _removeBlockList.append(unit)

                return True, _removeBlockList
        else:
            return False, _compareList

    def _update_state(self, stateStream: dict, objectBlockList: list, targetWord: str) -> None:
        """
        更新当前所有语法方块的状态，Python dict的key值表示方块名字，value值（bool）表示当前方块是否有某个状态
        :param stateStream: 状态流（dict）
        :param objectBlockList: 所有is方块构成的list
        :param targetWord: 待检测的目标动词
        :return: 无返回值，直接更新state stream
        """

        allGrammarBlocksList = []

        for isBlock in objectBlockList:
            _isGrammarValid = self._is_verb_grammar_valid(isBlock)
            for i in range(0, len(_isGrammarValid), 2):
                if _isGrammarValid[i] is None:
                    continue
                else:
                    allGrammarBlocksList.append(type(_isGrammarValid[i]).__name__)
                    allGrammarBlocksList.append(_isGrammarValid[i+1])

        for i in range(0, len(allGrammarBlocksList), 2):  # 为stateStream初始化，默认都是False状态
            stateStream[allGrammarBlocksList[i]] = False

        for i in range(0, len(allGrammarBlocksList), 2):
            if allGrammarBlocksList[i+1].word == targetWord:  # 当匹配到状态时，调整为True
                stateStream[allGrammarBlocksList[i]] = True  #! Possible Bug: 下一行可能需要一个break语句
        for blockNounName in stateStream:
            if blockNounName not in allGrammarBlocksList:  # 当状态流里的状态不存在时，调整为False
                stateStream[blockNounName] = False

    def endow(self, objectBlockList: list) -> None:
        """
        根据语法规则判断是否需要赋予（修改）方块某些属性，若符合语法规则，则直接赋予属性
        :param objectBlockList: 所有is方块构成的list
        :return: 无返回值，直接在gameState中修改方块的状态
        """

        isWeakSign = False
        isDefeatSign = False
        _removeWeakBlockList = []
        _removeDefeatBlockList = []

        self._update_state(stopStateStream, objectBlockList, 'stop')
        self._update_state(pushStateStream, objectBlockList, 'push')
        self._update_state(youStateStream, objectBlockList, 'you')
        self._update_state(winStateStream, objectBlockList, 'win')
        self._update_state(weakStateStream, objectBlockList, 'weak')
        self._update_state(defeatStateStream, objectBlockList, 'defeat')

        for blockNounName in stopStateStream:
            targetBlockName = "".join(blockNounName.split('Noun'))
            _removeWeakBlockList = self._is_weak(self._gameState.units)[1]
            _removeDefeatBlockList = self._is_defeat(self._gameState.units)[1]
            if len(_removeWeakBlockList):
                isWeakSign = True
            if len(_removeDefeatBlockList):
                isDefeatSign = True
            if youStateStream[blockNounName]:  # 更新具有you状态的方块属性
                for unit in self._gameState.units:
                    if type(unit).__name__ == targetBlockName:
                        unit._controllable = True
                        unit._moveable = True
            else:
                for unit in self._gameState.units:
                    if type(unit).__name__ == targetBlockName:
                        unit._controllable = False

            if not stopStateStream[blockNounName] and not pushStateStream[blockNounName]:  # 更新具有stop和push状态的方块属性
                for unit in self._gameState.units:
                    if type(unit).__name__ == targetBlockName and not unit.is_control():
                        unit._passable = True
                        unit._moveable = False
            elif stopStateStream[blockNounName] and not pushStateStream[blockNounName]:
                for unit in self._gameState.units:
                    if type(unit).__name__ == targetBlockName and not unit.is_control():
                        unit._passable = False
                        unit._moveable = False
            elif not stopStateStream[blockNounName] and pushStateStream[blockNounName]:
                for unit in self._gameState.units:
                    if type(unit).__name__ == targetBlockName and not unit.is_control():
                        unit._passable = False
                        unit._moveable = True
            else:
                for unit in self._gameState.units:
                    if type(unit).__name__ == targetBlockName and not unit.is_control():
                        unit._passable = False
                        unit._moveable = False

        if isWeakSign:
            for removeWeakBlock in _removeWeakBlockList:
                self._gameState.units.remove(removeWeakBlock)
        if isDefeatSign:
            for removeDefeatBlock in _removeDefeatBlockList:
                if removeDefeatBlock.is_control():
                    self._gameState.units.remove(removeDefeatBlock)

    def transform(self, objectBlockList: list) -> None:
        """
        根据语法规则判断是否变换方块的类型，若符合语法规则，则将全部满足条件的方块变换类型
        :param objectBlockList: 所有is方块构成的list
        :return: 无返回值，直接在gameState中修改方块的状态
        """

        subjectBlockList = self._gameState.subjectBlockList
        for isBlock in objectBlockList:
            blockAround = self._is_noun_grammar_valid(isBlock)
            for i in range(0, len(blockAround), 2):
                if blockAround[i] is not None:
                    # 当语法成立且宾语不为you时，定为方块转换关系，分别得到主语宾语的类名，
                    subjectBlockTypeName = type(blockAround[i]).__name__
                    subjectTargetBlockTypeName = "".join(subjectBlockTypeName.split("Noun"))
                    objectBlockTypeName1 = type(blockAround[i + 1]).__name__
                    objectTargetBlockTypeName = "".join(objectBlockTypeName1.split("Noun"))
                    # 遍历所有与主语类名相同的方块，将主语类名变为宾语类名，主语属性变为宾语属性
                    for unit in subjectBlockList:
                        if type(unit).__name__ == objectTargetBlockTypeName:
                            objectTargetBlock = unit
                            break
                    for j in range(len(self._gameState.units)):
                        if type(self._gameState.units[j]).__name__ == subjectTargetBlockTypeName:
                            templocation = self._gameState.units[j].location
                            self._gameState.units[j] = copy.copy(objectTargetBlock)
                            self._gameState.units[j].location = templocation
