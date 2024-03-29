# -*- coding: utf-8 -*-
from operator import xor
from db import highscore as dbhs
from constant import distConstant as dico
from constant import systemconstant
from model.basemodel import BaseModel
from util import tetocone_util as teut

class abuchmentModel(BaseModel):
    
    def searchMusic(self, displaydAbuchment, serchLavalName, ungetFlg):
        filterList = []
        screenDataList = []
        serchLevelId = teut.getLevelIdByName(serchLavalName)
        highScoreList = dbhs.selectHighScore("", serchLevelId)

        if displaydAbuchment == systemconstant.FULL_COMBO:
            filterList = self.filterScoreData(highScoreList, ungetFlg, "fullComboCount")
        elif displaydAbuchment == systemconstant.PERFECT:
            filterList = self.filterScoreData(highScoreList, ungetFlg, "perfectCount")

        abuchmentList = self.makeAbuchmentData(filterList)

        for abuchment in abuchmentList:
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
    
    def filterScoreData(self, highScoreList, ungetFlg, targetParam):
        filteredList = []
        chartIdList = []
        for highScore in highScoreList:
            if highScore[targetParam] > 0:
                chartIdList.append(highScore["chartId"])

        for highScore in highScoreList:
            if (highScore["chartId"] in chartIdList) != ungetFlg:
                filteredList.append(highScore)

        return filteredList

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
                playCount += screenDataDist[chartId]["playCount"]

            screenDataDist[chartId] = {
                    "chartId": chartId,
                    "musicName": abuchment["musicName"],
                    "levelId": abuchment["levelId"],
                    "perfectCount": perfectCount,
                    "fullComboCount": fullComboCount,
                    "playCount": playCount,
                }

        return list(screenDataDist.values())


if __name__ == '__main__':
        pass
