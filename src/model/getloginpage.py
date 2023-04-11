# -*- coding: utf-8 -*-
from time import sleep

from exception.loginerror import LoginError
from model import datainserts
from model import mypagedata as myPage
from db import chartconstitution as cha
from db import ranking as ra
from db import character as cra
from constant import messeges
from constant.distConstant import DEGREE_CATEGORY_DIST
from constant.systemconstant import NO_DATA_STR


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
                characterList = []
                for character in characters:
                    characterId = character["characterId"]
                    characterInfo = {}
                    characterInfo["character"] = character
                    characterInfo["introduction"] = cra.selectIntroductionCharacter(characterId)
                    
                    if characterInfo["introduction"] == NO_DATA_STR:
                        sleep(1)
                        responseInfo = myPage.getCharacterData(session, characterId)
                        characterInfo["introduction"] = responseInfo["response"][characterId]["introduction"]
                    
                    characterList.append(characterInfo)
            
                datainserts.insertCharacter(characterList)

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
            dataUnmatchFlg = False

            for chart in chartList:
                sleep(1)
                ranking = myPage.getRankingData(session, chart["musicId"], chart["chartId"], chart["genreId"])
                rank = ranking.response["response"]["rank"]
                if ranking.response["response"]["score"] == chart["highScore"]:
                    ra.updateRanking(chart["chartId"], rank, ranking.getDate)
                else:
                    dataUnmatchFlg = True                    

            if dataUnmatchFlg: 
                return messeges.DATA_IMPORT_DATA_UNMATCH
            
        if degreesGetFlg:
            degreesDist = {}
            for category in DEGREE_CATEGORY_DIST.keys():
                sleep(1)
                response = myPage.getDegreesData(session, category)
                degreesDist[category] = response["response"]

            datainserts.insertDegrees(degreesDist)

        
        return messeges.DATA_INPORT_SUCCESS
    except LoginError:
        return messeges.DATA_INPORT_LOGIN_ERROR
    except Exception:
        return messeges.DATA_INPORT_OUTHER_ERROR

if __name__ == '__main__':
    pass
