# -*- coding: utf-8 -*-
from time import sleep

from exception.loginerror import LoginError
from model import mypagedata as myPage
from db import ranking as ra
from db import chartconstitution as ch
from constant import messeges


def getLoginRankingData(cardId, password, chartId):
    if not (len(cardId) > 0 and len(password) > 0):
        return messeges.DATA_IMPORT_ID_LACK

    chartInfoList = ch.selectedSingleChart(chartId=chartId)
    
    if len(chartInfoList) != 1:
        return messeges.DATA_IMPORT_DATA_UNMATCH

    chartInfo = chartInfoList[0]

    try:
        session = myPage.loginMyPage(cardId, password)
        sleep(3)
        ranking = myPage.getRankingData(session, chartInfo["musicId"], chartId, chartInfo["genreId"])
        rank = ranking.response["response"]["rank"]
        if ranking.response["response"]["score"] == chartInfo["highScore"]:
            ra.updateRanking(chartId, rank, ranking.getDate)
        else:
            return messeges.DATA_IMPORT_DATA_UNMATCH
        
        return messeges.DATA_INPORT_SUCCESS
    except LoginError:
        return messeges.DATA_INPORT_LOGIN_ERROR
    except Exception:
        return messeges.DATA_INPORT_OUTHER_ERROR


if __name__ == '__main__':
    pass
