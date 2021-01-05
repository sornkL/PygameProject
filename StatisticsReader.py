import datetime
import json


from typing import Union


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

# print(check_last_win_time("Statistics.json", "Map1"))
