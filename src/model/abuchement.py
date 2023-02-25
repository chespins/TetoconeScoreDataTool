# -*- coding: utf-8 -*-
from operator import xor
from db import highscore as dbhs
from constant import distConstant as dico
from constant import systemconstant
from model.basemodel import BaseModel

class abuchmentModel(BaseModel):
    
    def searchMusic(self, displaydAbuchment, serchLavalName, ungetFlg):
        screenDataDist = {}
        screenDataList = []

        if displaydAbuchment == systemconstant.FULL_COMBO:
            screenDataDist = self.fullComboAbuchment(serchLavalName, ungetFlg)
        elif displaydAbuchment == systemconstant.PERFECT:
            screenDataDist = self.parfectAbuchment(serchLavalName, ungetFlg)

        for abuchment in screenDataDist.values():
            screenDataList.append({
                        "musicName": abuchment["musicName"],
                        "levelName": dico.LEVEL_NAME_DIST[
                            str(abuchment["levelId"])].name,
                        "playCount": str(abuchment["playCount"]) + "回",
                        "perfectCount": str(abuchment["perfectCount"]) + "回",
                        "fullComboCount": str(abuchment["fullComboCount"]) + "回",
                        "detailsFlg": abuchment["playCount"] <= 0,
                        "chartId": abuchment["chartId"],
                })

        return screenDataList

    def parfectAbuchment(self, serchLavalName, ungetFlg):
        parfectedList = []
        chartIdList = []
        highScoreList = self.serchHighScore(serchLavalName)
        for highScore in highScoreList:
            if highScore["perfectCount"] > 0:
                chartIdList.append(highScore["chartId"])

        for highScore in highScoreList:
            if (highScore["chartId"] in chartIdList) != ungetFlg:
                parfectedList.append(highScore)

        return self.makeAbuchmentData(parfectedList)

    def fullComboAbuchment(self, serchLavalName, ungetFlg):
        parfectedList = []
        chartIdList = []
        highScoreList = self.serchHighScore(serchLavalName)
        for highScore in highScoreList:
            if highScore["fullComboCount"] > 0:
                chartIdList.append(highScore["chartId"])


        for highScore in highScoreList:
            if (highScore["chartId"] in chartIdList) != ungetFlg:
                parfectedList.append(highScore)

        return self.makeAbuchmentData(parfectedList)

    def makeAbuchmentData(self, abuchmentList):
        screenDataDist = {}
        for abuchment in abuchmentList:
            perfectCount = abuchment["perfectCount"]
            fullComboCount = abuchment["fullComboCount"]
            playCount = abuchment["playCount"]
            chartId = abuchment["chartId"]
            if chartId in screenDataDist.keys():
                perfectCount += screenDataDist[chartId]["perfectCount"]
                fullComboCount += screenDataDist[chartId]["fullComboCount"]
                playCount += abuchment["playCount"]

            screenDataDist[chartId] = {
                    "chartId": chartId,
                    "musicName": abuchment["musicName"],
                    "levelId": abuchment["levelId"],
                    "perfectCount": perfectCount,
                    "fullComboCount": fullComboCount,
                    "playCount": playCount,
                }

        return screenDataDist

    def serchHighScore(self, serchLavalName):
        serchLevelId = 0
        for levelName in dico.LEVEL_NAME_DIST.values():
            if levelName.name == serchLavalName:
                serchLevelId = levelName.id
                break

        return dbhs.selectHighScore("", serchLevelId)


if __name__ == '__main__':
        pass
