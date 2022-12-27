# -*- coding: utf-8 -*-
from db import highscore
from constant import distConstant as dico
from model.basemodel import BaseModel
from util import util


class HighScoreFormusic(BaseModel):
    def getHighScoreByMusic(chartId, displayedMode):
        modeList = dico.DISPLAYED_MODE_DIST[displayedMode].searchedMode
        score = highScoreData()

        for mode in modeList:
            dbresult = highscore.selectHighScoreByAllKey(chartId, mode)
            if len(dbresult) == 1:
                score.setHighScore(dbresult[0])

        return score.makeViewData()

    def makeModeNamePulldown(chartId):
        pulldownList = []
        dataedMode = []
        dbDataList = highscore.selectHighScoreByChartId(chartId)

        for dbData in dbDataList:
            dataedMode.append(dbData["mode"])

        if len(dataedMode) == 1:
            pulldownList.append(dico.MODE_NAME_DIST[str(dataedMode[0])])
        
        else:
            for modeData in dico.DISPLAYED_MODE_DIST.values():
                modeIntersection = set(dataedMode) & modeData.searchedMode
                if len(modeIntersection) > 0:
                    pulldownList.append(modeData.name)

        return pulldownList


class highScoreData():
    def __init__(self):
        self.highscore = 0
        self.maxCombo = 0
        self.playCount = 0
        self.clearedCount = 0
        self.fullComboCount = 0
        self.perfectCount = 0
        self.updateTime = util.minDateTime()

    def setHighScore(self, highScoreData):
        if highScoreData["highScore"] >= self.highscore:
            self.highscore = highScoreData["highScore"]
            self.maxCombo = highScoreData["maxCombo"]

        if util.diffDate(self.updateTime, highScoreData["updateTime"]):
            self.updateTime = highScoreData["updateTime"]
        
        self.playCount += highScoreData["playCount"]
        self.clearedCount += highScoreData["clearedCount"]
        self.fullComboCount += highScoreData["fullComboCount"]
        self.perfectCount += highScoreData["perfectCount"]

    def makeViewData(self):
        viewHash = {
                "highScore": str(self.highscore),
                "maxCombo":  str(self.maxCombo),
                "playCount": str(self.playCount) + "回",
                "clearedCount": str(self.clearedCount) + "回",
                "fullComboCount": str(self.fullComboCount) + "回",
                "perfectCount": str(self.perfectCount) + "回",
                "lastUpdateTime": util.changeTimeZone(self.updateTime)
            }
        
        return viewHash


if __name__ == '__main__':
    pass
