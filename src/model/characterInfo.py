# -*- coding: utf-8 -*-

from db import character as cha
from model.basemodel import BaseModel
from util import util
from constant.distConstant import DEGREE_CATEGORY_DIST


class CharacterInfoModel(BaseModel):
    characterInfoDist = {}

    def refreshCharacterData(self):
        characterInfoList = cha.selectCharacter()

        for character in characterInfoList:
            self.characterInfoDist[character["characterId"]] = character

        return
        
    def isEmptyCharacterInfoList(self):
        return len(self.characterInfoDist) > 0
    
    def getCharacterNameList(self):
        characterNameList = []
        for character in list(self.characterInfoDist.values()):
            characterNameList.append(
                {
                "characterId": character["characterId"],
                "characterName": character["characterName"],
                }
            )
        
        return characterNameList
    
    def getCharacterInfo(self, characterId):
        if characterId in list(self.characterInfoDist.keys()):
            return self.makeDisplayedData(self.characterInfoDist[characterId])
        
        return self.preDisplayedCharacterInfo()
        
    def preDisplayedCharacterInfo(self):
        nameList = self.getCharacterNameList()
        if len(nameList) > 0 :
            return self.makeDisplayedData(self.characterInfoDist[nameList[0]["characterId"]])
        
        return self.makeDisplayedData(None)

    def makeDisplayedData(self, dbData):
        dearnessRanking =  "--- 位"
        dearnessRankingDate = "-----"
        
        displayedData = {
            "characterName": "データなし",
            "introduction": "",
            "dearnessRank": "ランク ",
            "dearnessPoint": "ポイント",
            "dearnessRanking": dearnessRanking,
            "dearnessRankingDate": dearnessRankingDate,
            "lastPlayDate": "---",
        }


        if not (dbData is None):
            if not dbData["dearnessRanking"] is None:
                dearnessRanking = str(dbData["dearnessRanking"]) + "位"
                dearnessRankingDate = util.changeTimeZone(dbData["rankingGetDate"]) + " 現在"

            displayedData = {
                    "characterName": dbData["characterName"],
                    "introduction": dbData["introduction"].replace("\n", ""),
                    "dearnessRank": "ランク " + str(dbData["dearnessRank"]),
                    "dearnessPoint": str(dbData["dearnessPoint"]) + "ポイント",
                    "dearnessRanking": dearnessRanking,
                    "dearnessRankingDate": dearnessRankingDate,
                    "lastPlayDate": util.changeTimeZone(dbData["updatedAt"]),
                }
        
        return displayedData


if __name__ == '__main__':
    pass
