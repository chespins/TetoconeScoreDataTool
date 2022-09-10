# -*- coding: utf-8 -*-
from db import chartconstitution, highscore
from db import highscorehistory as dbh
from constant import distConstant as dico
from util import util


def getMusicName(chartId):
    musicInfo = chartconstitution.selectChartByChartId(chartId)
    displayMusicInfo = {
            "musicName": musicInfo[0]["musicName"],
            "levelName": dico.LEVEL_NAME_DIST[
                    str(musicInfo[0]["levelId"])
                ].name,
        }
    return displayMusicInfo


def getHighScoreByMusic(chartId):
    results = highscore.selectHighScoreByChartId(chartId)
    screenHighScore = []
    for highScoreData in results:
        ScoreHash = {
                "mode": dico.MODE_NAME_DIST[str(highScoreData["mode"])],
                "highScore": str(highScoreData["highScore"]),
                "maxCombo": str(highScoreData["maxCombo"]),
                "playCount": str(highScoreData["playCount"]),
                "clearedCount": str(highScoreData["clearedCount"]),
                "fullComboCount": str(highScoreData["fullComboCount"]),
                "perfectCount": str(highScoreData["perfectCount"]),
                "updateTime": util.changeTimeZone(highScoreData["updateTime"])
            }
        screenHighScore.append(ScoreHash)

    return screenHighScore


def getHighScoreHistoryByChartId(chartId):
    results = dbh.selectHighScoreHistoryBychartId(chartId)
    return makehighScoreHistoryScreenData(results)


def getHighScoreHistoryBySingleMode(chartId):
    results = dbh.selectHighScoreHistoryByMode(chartId, 1)
    return makehighScoreHistoryScreenData(results)


def makehighScoreHistoryScreenData(highscoreList):
    screenHighScore = []
    for highScoreData in highscoreList:
        ScoreHash = {
            "mode": dico.MODE_NAME_DIST[str(highScoreData["mode"])],
            "highScore": str(highScoreData["highScore"]),
            "updateTime": util.changeTimeZone(highScoreData["updateTime"])
            }
        screenHighScore.append(ScoreHash)

    return screenHighScore


if __name__ == '__main__':
    pass
