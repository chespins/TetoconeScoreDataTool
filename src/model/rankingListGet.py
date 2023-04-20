# -*- coding: utf-8 -*-
from db import highscore
from constant import distConstant as dico
from model.basemodel import BaseModel
from util import tetocone_util as teut

class RankingListGet(BaseModel):
    def searchMusic(self, searchLavalName, searchGenreName):
        searchLevelId = teut.getLevelIdByName(searchLavalName)
        searchGenreId = teut.getGenreIdByName(searchGenreName)
        screenHighScore = []
        dbHighScoreList = highscore.selectHighScore("", searchLevelId, searchGenreId)
        
        for highScoreData in dbHighScoreList:
            if highScoreData["mode"] != 1 or highScoreData["playCount"] == 0:
                continue

            chartId = highScoreData["chartId"]
            rankingData = self.makeRankingData(chartId)

            if rankingData["rankingDisPlayedFlg"]:
                ranking = rankingData["ranking"]
                maxRank = self.getMaxRank(chartId)          
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
