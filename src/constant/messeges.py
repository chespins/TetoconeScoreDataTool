# -*- coding: utf-8 -*-
# マイページデータ取得関連
DATA_INPORT_START = "データ取得には最大で5分程度時間がかかります。"
DATA_INPORT_RANKING_START = "データ取得には最大で30秒程度時間がかかります。"
DATA_INPORT_PROCESS = "データ取得中。しばらくお待ちください。"
DATA_INPORT_SUCCESS = "マイページからのデータ取得が成功しました。"
DATA_IMPORT_ID_LACK = "ユーザ名およびパスワードは必ず入力してください。"
DATA_INPORT_LOGIN_ERROR = "ログインに失敗しました。ユーザIDもしくはパスワードが正しいか確認してください。"
DATA_INPORT_OUTHER_ERROR = "予期せぬエラーが発生しました。時間をおいてやり直してください。"
DATA_IMPORT_NO_GET_DATA = "取得したいデータの種類を必ず1つ以上選択してください。"
DATA_IMPORT_NO_LEVEL = "ランキング情報取得時は取得したい難易度を必ず1つ以上選択してください。"
DATA_IMPORT_DATA_UNMATCH = "取得済のスコアデータとランキングデータに差異がありました。\nスコアデータを取り直してください。"
DATA_INPORT_RANKING_NO_SCORE = "指定された難易度を未プレイもしくはスコアデータが本ツールで取得されていません。\nプレイ状況をご確認ください。"

# データファイル系
DATA_FILE_UPDATE = "旧バージョンのデータファイルが読み込まれました。データファイルを更新してよろしいでしょうか。\n更新後は旧バージョンのツールではデータ取得ができなくなります。"
DATA_FILE_ERROR = "データファイルの内容が不正です。データファイルを再作成しますがよろしいでしょうか。\n既存ファイルの内容は全て削除されます。"
DATA_FILE_VERSION_ERROR = "データファイルの内容がツールが想定しているバージョンと異なります。\n読み取り専用で起動します。"

# 固定文言系
TITLE_DIR_SELECT = "フォルダ選択"

# CSV出力関係
CSV_HIGH_SCORE_SUCCESS = "ハイスコアデータの作成に成功しました。"
CSV_NO_HIGH_SCORE = "ハイスコアデータが存在しません。マイページ取得からハイスコアデータを取得してからもう一度お試しください。"
CSV_FILE_OUTPUT_ERROR = "指定したファイル名でCSVファイルの出力に失敗しました。"


if __name__ == '__main__':
    pass
