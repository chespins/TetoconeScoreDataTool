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
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

# クリア状況確認用
FULL_COMBO = "フルコンボ"
PERFECT = "パーフェクト"

ABUCHMENT_LIST = [
                FULL_COMBO,
                PERFECT
        ]

# DBのバージョン
CURRENT_DB_VERSION = "v0.5"
