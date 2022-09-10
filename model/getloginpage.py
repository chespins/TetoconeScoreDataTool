# -*- coding: utf-8 -*-
from exception.loginerror import LoginError
from model import datainserts
from model import mypagedata as myPage
from constant import messeges


def getLoginPageData(cardId, password):
    message = ""
    if not (len(cardId) > 0 and len(password) > 0):
        return messeges.DATA_IMPORT_ID_LACK

    try:
        myPageData = myPage.getConnectPageData(cardId, password)
        stages = myPageData["response"]["stages"]
        datainserts.InsertMusic(stages)
        message = messeges.DATA_INPORT_SUCCESS
    except LoginError:
        message = messeges.DATA_INPORT_LOGIN_ERROR
    except Exception:
        message = messeges.DATA_INPORT_OUTHER_ERROR

    return message


if __name__ == '__main__':
    pass
