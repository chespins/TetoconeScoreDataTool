# -*- coding: utf-8 -*-
from time import sleep
import requests
import json

from exception.loginerror import LoginError
from constant import systemconstant as cons


def getConnectPageData(cardId, password):
    session = requests.session()
    session.headers["user-agent"] = cons.USER_AGENT
    session.headers["Accept-Language"] = "ja"
    session.get(cons.WEB_LOGIN_URL)
    sleep(10)
    login_request_data = json.dumps({
            "card_id": cardId,
            "password": password
        })
    session.headers["DNT"] = "1"
    session.headers["Host"] = cons.HOST_URL
    session.headers["Referer"] = cons.WEB_LOGIN_URL
    session.headers["Content-Type"] = "application/json"
    session.headers["Content-Length"] = str(len(login_request_data))
    login = session.post(cons.API_LOGIN_URL, login_request_data)
    if login.status_code != 200:
        raise LoginError("ログイン失敗")

    sleep(5)
    session.headers.pop("Content-Length")
    session.headers["Referer"] = cons.WEB_LOGINED_URL
    result = session.get(cons.DATA_GET_URL)
    data = json.loads(result.text)
    return data


if __name__ == '__main__':
    pass
