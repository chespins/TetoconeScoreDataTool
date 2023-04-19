# -*- coding: utf-8 -*-
from time import sleep

from exception.loginerror import LoginError
from model import datainserts
from model import mypagedata as myPage
from db import chartconstitution as cha
from db import ranking as ra
from db import character as cra
from util import util
from constant import messeges
from constant.distConstant import DEGREE_CATEGORY_DIST


def getLoginPageData(cardId: str, password: str, scoreGetFlg: bool, 
        rankingGetFlg: bool, standardGetFlg: bool, expertGetFlg: bool,
        ultimateGetFlg: bool, maniacGetFlg: bool, connectGetFlg: bool, 
        degreesGetFlg: bool, characterGetFlg: bool):
    if not (len(cardId) > 0 and len(password) > 0):
        return messeges.DATA_IMPORT_ID_LACK
    
    if not (scoreGetFlg or rankingGetFlg or degreesGetFlg or characterGetFlg):
        return messeges.DATA_IMPORT_NO_GET_DATA

    levelList = []
    if rankingGetFlg:
        if standardGetFlg:
            levelList += [1]

        if expertGetFlg:
            levelList += [2]

        if ultimateGetFlg:
            levelList += [3]

        if maniacGetFlg:
            levelList += [4]

        if connectGetFlg:
            levelList += [5]        

        if len(levelList) == 0:
            return messeges.DATA_IMPORT_NO_LEVEL
        
        if not scoreGetFlg:
            chartList = cha.selectedSingleChart(levelIdList=levelList)
            if len(chartList) == 0:
                return messeges.DATA_INPORT_RANKING_NO_SCORE


    try:
        session = myPage.loginMyPage(cardId, password)
        sleep(3)
        if scoreGetFlg or characterGetFlg:
            myPageData = myPage.getConnectPageData(session)
            if characterGetFlg:
                characters = myPageData["response"]["characters"]
                getCharacterData(session, characters)            
                
            if scoreGetFlg:
                stages = myPageData["response"]["stages"]
                datainserts.InsertMusic(stages)
                if rankingGetFlg:
                    chartList = cha.selectedSingleChart(levelIdList=levelList)
                    if len(chartList) == 0:
                        return messeges.DATA_INPORT_RANKING_NO_SCORE
                    else:
                        sleep(1)            

        if rankingGetFlg:            
            if getScoreRankingData(session, chartList): 
                return messeges.DATA_IMPORT_DATA_UNMATCH
            
        if degreesGetFlg:
            getDegreesData(session)
        
        return messeges.DATA_INPORT_SUCCESS
    except LoginError:
        return messeges.DATA_INPORT_LOGIN_ERROR
    except Exception:
        return messeges.DATA_INPORT_OUTHER_ERROR
    

def getScoreRankingData(session, chartList):
    dataUnmatchFlg = False
    rankingList = []

    for chart in chartList:
        sleep(1)
        ranking = myPage.getRankingData(session, chart["musicId"], chart["chartId"], chart["genreId"])
        rank = ranking.response["response"]["rank"]
        if ranking.response["response"]["score"] == chart["highScore"]:
            ranking = {
                    "chartId": chart["chartId"],
                    "ranking": rank,
                    "getDate": ranking.getDate,
            }
            rankingList.append(ranking)
        else:
            dataUnmatchFlg = True 

    if len(rankingList) > 0:
        ra.insertRanking(rankingList)
    
    return dataUnmatchFlg


def getCharacterData(session, characters):
    characterList = []
    for character in characters:
        characterId = character["characterId"]
        characterInfo = {}
        characterInfo["character"] = character
        dbcharacter = cra.selectCharacter(characterId=characterId)
        if len(dbcharacter) == 0:
            sleep(1)
            responseInfo = myPage.getCharacterData(session, characterId)
            characterInfo["introduction"] = responseInfo["response"][characterId]["introduction"]
        else:
            characterInfo["introduction"] = dbcharacter[0]["introduction"]                                
                    
        if character["isUsed"]:
            sleep(1)
            caracterRanking = myPage.getCharacterRanking(session, characterId)
            characterInfo["rankingDate"] = util.getDateTimeNow()
            characterInfo["ranking"] = caracterRanking["response"]

        characterList.append(characterInfo)

    datainserts.insertCharacter(characterList)


def getDegreesData(session):
    degreesDist = {}
    for category in DEGREE_CATEGORY_DIST.keys():
        sleep(1)
        response = myPage.getDegreesData(session, category)
        degreesDist[category] = response["response"]

    datainserts.insertDegrees(degreesDist)


def getLoginRankingData(cardId, password, chartId):
    if not (len(cardId) > 0 and len(password) > 0):
        return messeges.DATA_IMPORT_ID_LACK

    chartInfoList = cha.selectedSingleChart(chartId=chartId)
    
    if len(chartInfoList) != 1:
        return messeges.DATA_IMPORT_DATA_UNMATCH

    chartInfo = chartInfoList[0]
    chartList = [chartInfo]

    try:
        session = myPage.loginMyPage(cardId, password)
        sleep(3)
        if getScoreRankingData(session, chartList):
            return messeges.DATA_IMPORT_DATA_UNMATCH
        else:
            return messeges.DATA_INPORT_SUCCESS
        
    except LoginError:
        return messeges.DATA_INPORT_LOGIN_ERROR
    except Exception:
        return messeges.DATA_INPORT_OUTHER_ERROR


if __name__ == '__main__':
    pass
