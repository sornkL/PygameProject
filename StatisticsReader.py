import datetime
import json
import pygame


from typing import Union


from Settings import *


def update_win_count(path: str, mapId: str) -> None:
    try:
        with open(path, 'r+') as jsonObject:
            content = json.load(jsonObject)
            content[mapId][1]['winCount'] += 1
            jsonObject.seek(0, 0)
            jsonObject.truncate()
            json.dump(content, jsonObject)
    except Exception as errorMessage:
        print(errorMessage)
    finally:
        jsonObject.close()


def update_lose_count(path: str, mapId: str) -> None:
    try:
        with open(path, 'r+') as jsonObject:
            content = json.load(jsonObject)
            content[mapId][1]['loseCount'] += 1
            jsonObject.seek(0, 0)
            jsonObject.truncate()
            json.dump(content, jsonObject)
    except Exception as errorMessage:
        print(errorMessage)
    finally:
        jsonObject.close()


def check_win_count(path: str) -> list:
    winCountList = []
    try:
        with open(path, 'r') as jsonObject:
            content = json.load(jsonObject)
            for i in range(1, len(content)+1):
                mapId = "Map" + str(i)
                winCount = content[mapId][1]["winCount"]
                winCountList.append(winCount)
    except Exception as errorMessage:
        print(errorMessage)
    finally:
        jsonObject.close()

    return winCountList


def check_lose_count(path: str) -> list:
    loseCountList = []
    try:
        with open(path, 'r') as jsonObject:
            content = json.load(jsonObject)
            for i in range(1, len(content)+1):
                mapId = "Map" + str(i)
                loseCount = content[mapId][1]["loseCount"]
                loseCountList.append(loseCount)
    except Exception as errorMessage:
        print(errorMessage)
    finally:
        jsonObject.close()

    return loseCountList


def update_first_win_time(path: str, mapId: str) -> None:
    try:
        with open(path, 'r+') as jsonObject:
            content = json.load(jsonObject)
            currentTime = str(datetime.datetime.today()).split('.')[0]
            content[mapId][2]["firstWinTime"] = currentTime
            jsonObject.seek(0, 0)
            jsonObject.truncate()
            json.dump(content, jsonObject)
    except Exception as errorMessage:
        print(errorMessage)
    finally:
        jsonObject.close()


def check_first_win_time(path: str, mapId: str) -> Union[str, None]:
    try:
        with open(path, 'r') as jsonObject:
            content = json.load(jsonObject)
            lastWinTime = content[mapId][2]["firstWinTime"]
            if lastWinTime != '':
                return lastWinTime
            else:
                return None
    except Exception as errorMessage:
        print(errorMessage)
    finally:
        jsonObject.close()


def adjust(cnt: int) -> list:
    numberPathList = []
    for num in str(cnt):
        numberPath = "pics/number_" + num + ".png"
        numberPathList.append(numberPath)

    return numberPathList


def statistics_display(window, id: int) -> None:
    winCountList = check_win_count(STATISTICS_FILE_PATH)
    loseCountList = check_lose_count(STATISTICS_FILE_PATH)

    winCount = winCountList[id]
    loseCount = loseCountList[id]
    defaultWinCountLocationX = 150
    defaultLoseCountLocationX = 150
    defaultWinTimeLocationX = 150
    winCountNumberPathList = adjust(winCount)
    loseCountNumberPathList = adjust(loseCount)
    firstWintTimeNumberPathList = []
    for i in range(len(str(winCount))):
        window.blit(pygame.image.load(winCountNumberPathList[i]), Vector2(defaultWinCountLocationX, 0))
        defaultWinCountLocationX += 30
    for i in range(len(str(loseCount))):
        window.blit(pygame.image.load(loseCountNumberPathList[i]), Vector2(defaultLoseCountLocationX, 30))
        defaultLoseCountLocationX += 30

    firstWintTime = check_first_win_time(STATISTICS_FILE_PATH, "Map" + str(id+1))
    if firstWintTime is not None:
        for number in firstWintTime:
            if number == '-':
                firstWintTimeNumberPathList.append("pics/number_hyphen.png")
            elif number == ':':
                firstWintTimeNumberPathList.append("pics/number_colon.png")
            elif number == ' ':
                firstWintTimeNumberPathList.append("pics/number_null.png")
            else:
                firstWintTimeNumberPathList.extend(adjust(int(number)))
        for i in range(len(firstWintTime)):
            window.blit(pygame.image.load(firstWintTimeNumberPathList[i]), Vector2(defaultWinTimeLocationX, 60))
            defaultWinTimeLocationX += 30


