# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import requests
import json

from exception.loginerror import LoginError
from constant.systemconstant import LOGIN_URL


def getConnectPageData(cardId, password):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.use_chromium = True
    driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            chrome_options=options
        )

    try:
        driver.get(LOGIN_URL + "/login")
        sleep(3)
        driver.find_element("id", "cardId").send_keys(cardId)
        sleep(1)
        driver.find_element("id", "password").send_keys(password)
        sleep(1)
        driver.find_element("id", "loginButton").click()
        sleep(5)
        if driver.current_url == LOGIN_URL + "/login":
            raise LoginError("ログイン失敗")

        session = requests.session()

        # セッションの受け渡し
        for cookie in driver.get_cookies():
            session.cookies.set(cookie["name"], cookie["value"])

        result = session.get(LOGIN_URL + "/api/user?data=stages")
        data = json.loads(result.text)
        return data

    finally:
        driver.quit()


if __name__ == '__main__':
    pass
