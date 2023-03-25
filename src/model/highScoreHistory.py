# -*- coding: utf-8 -*-
from db import highscorehistory as dbh
from constant import distConstant as dico
from model.basemodel import BaseModel
from util import util


class HighScoreHistory(BaseModel):
    def getHighScoreHistoryByChartId(self, chartId):
        results = dbh.selectHighScoreHistoryBychartId(chartId)
        screenHighScore = []
        for highScoreData in results:
            ScoreHash = {
                "mode": dico.MODE_NAME_DIST[str(highScoreData["mode"])],
                "highScore": str(highScoreData["highScore"]),
                "maxCombo": str(highScoreData["maxCombo"]),
                "updateTime": util.changeTimeZone(highScoreData["updateTime"])
                }
            screenHighScore.append(ScoreHash)

        return screenHighScore
