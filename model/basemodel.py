# -*- coding: utf-8 -*-
from constant import distConstant as dico
from db import chartconstitution
from db import rankhistory as rakh
from db import ranking as rak
from util import util

class BaseModel():
    
    def makeLavalNamePulldown(self):
        pulldownList = [""]
        for levelName in dico.LEVEL_NAME_DIST.values():
            pulldownList.append(levelName.name)

        return pulldownList

    def makeGenreNamePulldown(self):
        pulldownList = [""]
        for genreName in dico.GANRU_NAME_DIST.values():
            pulldownList.append(genreName)

        return pulldownList
    
    def makeModeNamePulldown(self):
        pulldownList = []
        for modeName in dico.DISPLAYED_MODE_DIST.keys():
            pulldownList.append(modeName)

        return pulldownList

    def getMusicName(self, chartId):
        musicInfo = chartconstitution.selectChartByChartId(chartId)
        displayMusicInfo = {
                "musicName": musicInfo[0]["musicName"],
                "levelName": dico.LEVEL_NAME_DIST[
                        str(musicInfo[0]["levelId"])
                    ].name,
                "genreName": dico.GANRU_NAME_DIST[musicInfo[0]["genreId"]],
                "levelColor": dico.LEVEL_NAME_DIST[str(musicInfo[0]["levelId"])].colorCode,
            }
        return displayMusicInfo

    def isSinglePlay(self, modeString):
        return modeString == self.getSinglePlayName()

    def makeRankingData(self, chartId):
        ranking = rak.selectRankingForChartId(chartId)
        if len(ranking) == 1:
            displayedRanking = {
                    "rankingDisPlayedFlg": True,
                    "ranking": ranking[0]["ranking"] + "位",
                    "getDate": util.changeTimeZone(ranking[0]["getDate"]) + " 現在",
                }
        
        else:
            displayedRanking = {
                    "rankingDisPlayedFlg": False,
                }
        return displayedRanking

    def getrankingDataForDb(self, chartId, modeList):
        margeRankHistoryDist = {}        
        rankHistoryList = rakh.selectChartByChartIdMode(chartId, modeList)

        for rankHistory in rankHistoryList:
            count = rankHistory["count"]
            rank = rankHistory["rank"]
            if rankHistory["rank"] in margeRankHistoryDist.keys():
                count += margeRankHistoryDist[rank]["count"]

            margeRankHistoryDist[rank] = {
                    "rank": rankHistory["rank"],
                    "count": count
                }
        
        return margeRankHistoryDist

    def getSinglePlayName(self):
        return dico.MODE_NAME_DIST["1"]
