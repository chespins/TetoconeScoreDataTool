# -*- coding: utf-8 -*-
from db import highscore
from constant import distConstant as dico


def serchMusic(serchName, serchLavalName):
    serchLevelId = 0
    for levelName in dico.LEVEL_NAME_DIST.values():
        if levelName.name == serchLavalName:
            serchLevelId = levelName.id

    dbHighScoreList = highscore.selectHighScore(serchName, serchLevelId)
    margedist = {}

    for highScoreData in dbHighScoreList:
        chartId = highScoreData["chartId"]
        if chartId in margedist:
            if margedist[chartId]["highScore"] > highScoreData["highScore"]:
                continue
        margedist[chartId] = highScoreData

    return makeScreenData(margedist.values())


def makeScreenData(dbHighScoreList):
    screenHighScore = []
    for highScoreData in dbHighScoreList:
        ScoreHash = {
                "musicName": highScoreData["musicName"],
                "levelName": dico.LEVEL_NAME_DIST[
                        str(highScoreData["levelId"])].name,
                "highScore": str(highScoreData["highScore"]),
                "chartId": highScoreData["chartId"]
            }
        screenHighScore.append(ScoreHash)

    return screenHighScore


def makeLavalNamePulldown():
    pulldownList = [""]
    for levelName in dico.LEVEL_NAME_DIST.values():
        pulldownList.append(levelName.name)

    return pulldownList


if __name__ == '__main__':
    pass
