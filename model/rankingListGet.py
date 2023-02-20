# -*- coding: utf-8 -*-
from db import highscore
from constant import distConstant as dico
from model.basemodel import BaseModel

class RankingListGet(BaseModel):

    def searchMusic(self, searchLavalName, searchGenreName):
        searchLevelId = 0
        searchGenreId = ""
        screenHighScore = []

        for levelName in dico.LEVEL_NAME_DIST.values():
            if levelName.name == searchLavalName:
                searchLevelId = levelName.id
                break

        for genreId in dico.GANRU_NAME_DIST.keys():
            if dico.GANRU_NAME_DIST[genreId] == searchGenreName:
                searchGenreId = genreId
                break

        dbHighScoreList = highscore.selectHighScore("", searchLevelId, searchGenreId)

        
        for highScoreData in dbHighScoreList:
            if highScoreData["mode"] != 1 or highScoreData["playCount"] == 0:
                continue

            chartId = highScoreData["chartId"]
            maxRank = self.getMaxRank(chartId)
            rankingData = self.makeRankingData(chartId)

            if rankingData["rankingDisPlayedFlg"]:
                ranking = rankingData["ranking"]            
                ScoreHash = {
                            "musicName": highScoreData["musicName"],
                            "levelName": dico.LEVEL_NAME_DIST[
                                    str(highScoreData["levelId"])].name,
                            "highScore": str(highScoreData["highScore"]),
                            "maxRank": maxRank,
                            "ranking": ranking,
                            "chartId": highScoreData["chartId"],
                    }
            
                screenHighScore.append(ScoreHash)

        return screenHighScore

    def getMaxRank(self, chartId):
        modeList = dico.DISPLAYED_MODE_DIST[self.getSinglePlayName()].searchedMode
        margeRankHistoryDist = self.getRankData(chartId, modeList)

        for rank in dico.RANK_DIST.values():
            if rank.apiLank in margeRankHistoryDist.keys():
                return rank.gameLank

        return "---"


if __name__ == '__main__':
    pass
