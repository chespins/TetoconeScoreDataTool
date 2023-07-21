# -*- coding: utf-8 -*-
from model.basemodel import BaseModel
from model import makeCsvFile as mcf
from db import highscore as hs
from db import rankhistory as rh
from util import tetocone_util as teut
from util import util
from constant import messeges as ms


class OutputCsvModel(BaseModel):
    def outputCsvFile(self, fileName, rankFlg, margeFlg):
        highScoreList = hs.selectHighScore("")
        highScoreList = list(filter(lambda x: x["playCount"] > 0, highScoreList))
        if len(highScoreList) <= 0:
            return ms.CSV_NO_HIGH_SCORE
        
        if margeFlg:
            highScoreDict = {}
            for highScoreData in highScoreList:
                chartId = highScoreData["chartId"]
                if chartId in highScoreDict:
                    if highScoreDict[chartId]["highScore"] > highScoreData["highScore"]:
                        highScoreDict[chartId]["playCount"] += highScoreData["playCount"]
                        highScoreDict[chartId]["clearedCount"] += highScoreData["clearedCount"]
                        highScoreDict[chartId]["fullComboCount"] += highScoreData["fullComboCount"]
                        highScoreDict[chartId]["perfectCount"] += highScoreData["perfectCount"]
                        if util.diffDate(highScoreDict[chartId]["updateTime"], highScoreData["updateTime"]):
                            highScoreDict[chartId]["updateTime"] = highScoreData["updateTime"]

                        continue

                    else:
                        highScoreData["playCount"] += highScoreDict[chartId]["playCount"]
                        highScoreData["clearedCount"] += highScoreDict[chartId]["clearedCount"]
                        highScoreData["fullComboCount"] += highScoreDict[chartId]["fullComboCount"]
                        highScoreData["perfectCount"] += highScoreDict[chartId]["perfectCount"]
                        if util.diffDate(highScoreData["updateTime"], highScoreDict[chartId]["updateTime"]):
                            highScoreData["updateTime"] = highScoreDict[chartId]["updateTime"] 
                
                highScoreDict[chartId] = highScoreData

            highScoreList = list(highScoreDict.values())

        
        rankhistoryDict = {}
        if rankFlg:
            rankhistoryList = rh.selectAllRankData()
            rankhistoryDict = teut.makeRankDict(rankhistoryList, margeFlg)

        return mcf.makeScoreCsvFile(highScoreList, fileName, rankFlg, rankhistoryDict, margeFlg)
