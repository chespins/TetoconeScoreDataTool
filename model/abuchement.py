# -*- coding: utf-8 -*-
from operator import xor
from db import highscore as dbhs
from constant import distConstant as dico
from constant import systemconstant


def serchMusic(displaydAbuchment, serchLavalName, ungetFlg):
    screenDataDist = {}
    screenDataList = []

    if displaydAbuchment == systemconstant.FULL_COMBO:
        screenDataDist = fullComboAbuchment(serchLavalName, ungetFlg)
    elif displaydAbuchment == systemconstant.PERFECT:
        screenDataDist = parfectAbuchment(serchLavalName, ungetFlg)

    for abuchment in screenDataDist.values():
        screenDataList.append({
                    "musicName": abuchment["musicName"],
                    "levelName": dico.LEVEL_NAME_DIST[
                        str(abuchment["levelId"])].name,
                    "perfectCount": str(abuchment["perfectCount"]) + "回",
                    "fullComboCount": str(abuchment["fullComboCount"]) + "回"
            })

    return screenDataList


def parfectAbuchment(serchLavalName, ungetFlg):
    parfectedList = []
    chartIdList = []
    highScoreList = serchHighScore(serchLavalName)
    for highScore in highScoreList:
        if highScore["perfectCount"] > 0:
            chartIdList.append(highScore["chartId"])

    for highScore in highScoreList:
        if (highScore["chartId"] in chartIdList) != ungetFlg:
            parfectedList.append(highScore)

    return makeAbuchmentData(parfectedList)


def fullComboAbuchment(serchLavalName, ungetFlg):
    parfectedList = []
    chartIdList = []
    highScoreList = serchHighScore(serchLavalName)
    for highScore in highScoreList:
        if highScore["fullComboCount"] > 0:
            chartIdList.append(highScore["chartId"])


    for highScore in highScoreList:
        if (highScore["chartId"] in chartIdList) != ungetFlg:
            parfectedList.append(highScore)

    return makeAbuchmentData(parfectedList)


def makeAbuchmentData(abuchmentList):
    screenDataDist = {}
    for abuchment in abuchmentList:
        perfectCount = abuchment["perfectCount"]
        fullComboCount = abuchment["fullComboCount"]
        chartId = abuchment["chartId"]
        if chartId in screenDataDist.keys():
            perfectCount += screenDataDist[chartId]["perfectCount"]
            fullComboCount += screenDataDist[chartId]["fullComboCount"]

        screenDataDist[chartId] = {
                "musicName": abuchment["musicName"],
                "levelId": abuchment["levelId"],
                "perfectCount": perfectCount,
                "fullComboCount": fullComboCount
            }

    return screenDataDist


def serchHighScore(serchLavalName):
    serchLevelId = 0
    for levelName in dico.LEVEL_NAME_DIST.values():
        if levelName.name == serchLavalName:
            serchLevelId = levelName.id
            break

    return dbhs.selectHighScore("", serchLevelId)

def makeLavalNamePulldown():
    pulldownList = [""]
    for levelName in dico.LEVEL_NAME_DIST.values():
        pulldownList.append(levelName.name)

    return pulldownList

if __name__ == '__main__':
    pass
