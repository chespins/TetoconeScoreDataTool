# -*- coding: utf-8 -*-
from time import sleep

from exception.loginerror import LoginError
from model import datainserts
from model import mypagedata as myPage
from db import chartconstitution as cha
from db import ranking as ra
from constant import messeges


def getLoginPageData(cardId: str, password: str, scoreGetFlg: bool, 
        rankingGetFlg: bool, standardGetFlg: bool, expertGetFlg: bool,
        ultimateGetFlg: bool, maniacGetFlg: bool, connectGetFlg: bool):
    if not (len(cardId) > 0 and len(password) > 0):
        return messeges.DATA_IMPORT_ID_LACK
    
    if not (scoreGetFlg or rankingGetFlg):
        return messeges.DATA_IMPORT_NO_GET_DATA

    levelGetedFlg = standardGetFlg or expertGetFlg or ultimateGetFlg
    levelGetedFlg = levelGetedFlg or maniacGetFlg or connectGetFlg
    dataUnmatchFlg = False

    if rankingGetFlg and (not levelGetedFlg):
        return messeges.DATA_IMPORT_NO_LEVEL

    try:
        session = myPage.loginMyPage(cardId, password)
        sleep(3)
        if scoreGetFlg:
            myPageData = myPage.getConnectPageData(session)
            stages = myPageData["response"]["stages"]
            datainserts.InsertMusic(stages)
            if rankingGetFlg:
                sleep(1)
        
        if rankingGetFlg:
            levelList = []
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

            chartList = cha.selectedSingleChart(levelIdList=levelList)
            if len(chartList) == 0:
                return messeges.DATA_INPORT_RANKING_NO_SCORE

            for chart in chartList:
                sleep(1)
                ranking = myPage.getRankingData(session, chart["musicId"], chart["chartId"], chart["genreId"])
                rank = ranking.response["response"]["rank"]
                if ranking.response["response"]["score"] == chart["highScore"]:
                    ra.updateranking(chart["chartId"], rank, ranking.getDate)
                else:
                    dataUnmatchFlg = True                    

        if dataUnmatchFlg: 
            return messeges.DATA_IMPORT_DATA_UNMATCH
        
        return messeges.DATA_INPORT_SUCCESS
    except LoginError:
        return messeges.DATA_INPORT_LOGIN_ERROR
    # except Exception:
    #     return messeges.DATA_INPORT_OUTHER_ERROR

if __name__ == '__main__':
    pass
