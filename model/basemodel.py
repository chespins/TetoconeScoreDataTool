# -*- coding: utf-8 -*-
from constant import distConstant as dico
from db import chartconstitution

class BaseModel():
    
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
    
    def makeModeNamePulldown():
        pulldownList = []
        for modeName in dico.DISPLAYED_MODE_DIST.keys():
            pulldownList.append(modeName)

        return pulldownList

    def getMusicName(chartId):
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

