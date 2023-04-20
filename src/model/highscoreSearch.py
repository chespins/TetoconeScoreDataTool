# -*- coding: utf-8 -*-
from db import highscore
from constant import distConstant as dico
from model.basemodel import BaseModel
from util import tetocone_util as teut

class HighScoreSearch(BaseModel):
    def searchMusic(self, searchName, searchLavalName, searchGenreName, unplayedFlg):
        searchLevelId = teut.getLevelIdByName(searchLavalName)
        searchGenreId = teut.getGenreIdByName(searchGenreName)

        dbHighScoreList = highscore.selectHighScore(searchName, searchLevelId, searchGenreId)
        margedist = {}

        for highScoreData in dbHighScoreList:
            chartId = highScoreData["chartId"]
            if chartId in margedist:
                if margedist[chartId]["highScore"] > highScoreData["highScore"]:
                    margedist[chartId]["playCount"] += highScoreData["playCount"]
                    continue
                highScoreData["playCount"] += margedist[chartId]["playCount"]
            margedist[chartId] = highScoreData

        screenHighScore = []
        for highScoreData in margedist.values():
            if unplayedFlg or highScoreData["playCount"] > 0:
                ScoreHash = {
                        "musicName": highScoreData["musicName"],
                        "levelName": dico.LEVEL_NAME_DIST[
                                str(highScoreData["levelId"])].name,
                        "highScore": str(highScoreData["highScore"]),
                        "playCount": str(highScoreData["playCount"]) + "回",
                        "detailsFlg": highScoreData["playCount"] <= 0,
                        "chartId": highScoreData["chartId"],
                    }
                screenHighScore.append(ScoreHash)

        return screenHighScore


if __name__ == '__main__':
    pass
