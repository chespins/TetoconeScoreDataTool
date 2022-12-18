# -*- coding: utf-8 -*-
from db import highscore
from constant import distConstant as dico


def searchMusic(searchName, searchLavalName, searchGenreName, unplayedFlg):
    searchLevelId = 0
    searchGenreId = ""
    for levelName in dico.LEVEL_NAME_DIST.values():
        if levelName.name == searchLavalName:
            searchLevelId = levelName.id
            break

    for genreId in dico.GANRU_NAME_DIST.keys():
        if dico.GANRU_NAME_DIST[genreId] == searchGenreName:
            searchGenreId = genreId
            break


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

    return makeScreenData(margedist.values(), unplayedFlg)


def makeScreenData(dbHighScoreList, unplayedFlg):
    screenHighScore = []
    for highScoreData in dbHighScoreList:
        if unplayedFlg or highScoreData["playCount"] > 0:
            ScoreHash = {
                    "musicName": highScoreData["musicName"],
                    "levelName": dico.LEVEL_NAME_DIST[
                            str(highScoreData["levelId"])].name,
                    "highScore": str(highScoreData["highScore"]),
                    "playCount": str(highScoreData["playCount"]),
                    "chartId": highScoreData["chartId"],
                }
            screenHighScore.append(ScoreHash)

    return screenHighScore


def makeLavalNamePulldown():
    pulldownList = [""]
    for levelName in dico.LEVEL_NAME_DIST.values():
        pulldownList.append(levelName.name)

    return pulldownList

def makeGenreNamePulldown():
    pulldownList = [""]
    for genreName in dico.GANRU_NAME_DIST.values():
        pulldownList.append(genreName)

    return pulldownList

if __name__ == '__main__':
    pass
