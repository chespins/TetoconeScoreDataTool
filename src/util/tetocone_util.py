# -*- coding: utf-8 -*-
from constant import distConstant as dsc


def getLevelIdByName(searchedName) -> int:
    searchLevelId = 0
    for levelName in dsc.LEVEL_NAME_DIST.values():
            if levelName.name == searchedName:
                searchLevelId = levelName.id
                break
    
    return searchLevelId


def getGenreIdByName(searchGenreName) -> str:
    searchGenreId = ""
    for genreId in dsc.GANRU_NAME_DIST.keys():
        if dsc.GANRU_NAME_DIST[genreId] == searchGenreName:
            searchGenreId = genreId
            break
    
    return searchGenreId


def makeRankDict(rankHistoryList, margeFlg=False):
    rankHistoryDict = {}
    for rankHistory in rankHistoryList:
        listKey = rankHistory["chartId"]
        if not margeFlg:
            listKey += "_" + str(rankHistory["mode"])
        
        chartHistoryDict = {}
        if listKey in rankHistoryDict:
            chartHistoryDict = rankHistoryDict[listKey]

        count = rankHistory["count"]
        if rankHistory["rank"] in chartHistoryDict:
            count += chartHistoryDict[rankHistory["rank"]]["count"]

        chartHistoryDict[rankHistory["rank"]] = {
                "rank": rankHistory["rank"],
                "count": count,
        }
        rankHistoryDict[listKey] = chartHistoryDict

    return rankHistoryDict


if __name__ == '__main__':
    pass
