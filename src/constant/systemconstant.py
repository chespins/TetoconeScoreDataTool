# -*- coding: utf-8 -*-

# データファイル
TETOCONE_DB_NAME = "tetocone.db"

# ログインページ情報
HOST_URL = "mypage2.tetoteconnect.jp"
HTTP_ACCESS_URL = "https://" + HOST_URL + "/mypage-web2"
WEB_LOGIN_URL = HTTP_ACCESS_URL + "/login"
WEB_LOGINED_URL = HTTP_ACCESS_URL + "/?news=1"
API_LOGIN_URL = HTTP_ACCESS_URL + "/api/login"
DATA_GET_URL = HTTP_ACCESS_URL + "/api/user?data=stages&lang=ja_jp"
RANKING_GET_URL = HTTP_ACCESS_URL + "/api/user-rankings/stage-score/{0}/{1}?lang=ja_jp"
RANKING_PAGE_URL = HTTP_ACCESS_URL + "/rankings?category=stageScore&subcategory={1}&id={0}&index=0&genre={2}&page="
DEGREE_GET_URL = HTTP_ACCESS_URL + "/api/user-degree?category={0}&lang=ja_jp"
DEGREE_PAGE_URL = HTTP_ACCESS_URL + "/player/profile?tab=degree&category={0}"

# APIパラメータ
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
DNT = "1"
ACCEPT_LANGUAGE = "ja"
CONTENT_TYPE = "application/json"

# クリア状況確認用
FULL_COMBO = "フルコンボ"
PERFECT = "パーフェクト"

ABUCHMENT_LIST = [
                FULL_COMBO,
                PERFECT
        ]

# DBのバージョン
DB_VERSION_05 = "v0.5"
DB_VERSION_08 = "v0.8"
DB_VERSION_09 = "v0.9"

CURRENT_DB_VERSION = DB_VERSION_09
OLD_DB_VERSION_LIST = [DB_VERSION_05, DB_VERSION_08]

DB_SUCCESS = 0
DB_UPDATE = 1
DB_ERROR_FILE_BREAK = -1
DB_ERROR_UNKNOWN_FILE = -2

# ディレクトリ定義
LIBRARY_LICENSE_DIR = "./lib_license/"
DDL_DIR = "./ddl/"
FONT_DIR = "./fonts"
FONT_FILE_NAME = "Corporate-Mincho-ver2.otf"
KIVY_CURRENT_DIR = "./kvfile/"