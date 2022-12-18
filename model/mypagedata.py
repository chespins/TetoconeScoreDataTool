# -*- coding: utf-8 -*-
from time import sleep
import requests
import json

from exception.loginerror import LoginError
from constant import systemconstant as cons


def getConnectPageData(cardId, password):
    session = requests.session()
    session.headers["user-agent"] = cons.USER_AGENT
    session.headers["Accept-Language"] = cons.ACCEPT_LANGUAGE
    loginPage = session.get(cons.WEB_LOGIN_URL)
    sleep(10)
    login_request_data = json.dumps({
            "card_id": cardId,
            "password": password
        })
    session.headers["DNT"] = cons.DNT
    session.headers["Host"] = cons.HOST_URL
    session.headers["Referer"] = cons.WEB_LOGIN_URL
    session.headers["Content-Type"] = cons.CONTENT_TYPE
    session.headers["Content-Length"] = str(len(login_request_data))
    login = session.post(cons.API_LOGIN_URL, login_request_data)
    if login.status_code != 200:
        raise LoginError()

    sleep(5)
    session.headers.pop("Content-Length")
    session.headers["Referer"] = cons.WEB_LOGINED_URL
    result = session.get(cons.DATA_GET_URL)
    return json.loads(result.text)


if __name__ == '__main__':
    pass
