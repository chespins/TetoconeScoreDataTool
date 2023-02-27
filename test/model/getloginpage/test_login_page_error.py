# coding:utf-8
import pytest
import sys
import os
import datetime
from requests import HTTPError

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import getloginpage
from model.mypagedata import RankingDate
from exception.loginerror import LoginError


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_rank_data_unmatch(mocker):
    return_chart = [{
                    "chartId": "test001_01",
                    "musicId": "test001",
                    "levelId": 4,
                    "genreId": "GTEST1",
                    "highScore": 111,
                },
                {
                    "chartId": "test002_01",
                    "musicId": "test002",
                    "levelId": 3,
                    "genreId": "GTEST2",
                    "highScore": 222,
                },
                {
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 3,
                    "genreId": "GTEST3",
                    "highScore": 333,
                },
            ]
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    return_sesson = {"test": 12345}
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    return_ranking = [
        RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":111,
                "rank":1111
            }
        }),
        RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":999,
                "rank":2222
            }
        }),
        RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":333,
                "rank":3333
            }
        }),
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, True, True, True, True, True)
    assert result == "取得済のスコアデータとランキングデータに差異がありました。\nスコアデータを取り直してください。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    assert ranking_mock.call_count == 3
    ranking_mock.assert_has_calls([
            mocker.call(return_sesson, "test001", "test001_01", "GTEST1"),
            mocker.call(return_sesson, "test002", "test002_01", "GTEST2"),
            mocker.call(return_sesson, "test003", "test003_01", "GTEST3"),
        ]
    )
    assert db_ranking_mock.call_count == 2
    db_ranking_mock.assert_has_calls([
            mocker.call("test001_01", 1111, "2022-11-21T10:10:10+00:00"),
            mocker.call("test003_01", 3333, "2022-11-21T10:10:10+00:00"),
        ]
    )
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4,5])
    assert sleep_mock.call_count == 4
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
        ])


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_rank_other_error(mocker):
    return_chart = [{
                    "chartId": "test001_01",
                    "musicId": "test001",
                    "levelId": 4,
                    "genreId": "GTEST1",
                    "highScore": 111,
                },
                {
                    "chartId": "test002_01",
                    "musicId": "test002",
                    "levelId": 3,
                    "genreId": "GTEST2",
                    "highScore": 222,
                },
                {
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 3,
                    "genreId": "GTEST3",
                    "highScore": 333,
                },
            ]
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    return_sesson = {"test": 12345}
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    return_ranking = [
        RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":111,
                "rank":1111
            }
        }),
        HTTPError(),
        RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":333,
                "rank":3333
            }
        }),
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, True, True, True, True, True)
    assert result == "予期せぬエラーが発生しました。時間をおいてやり直してください。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    assert ranking_mock.call_count == 2
    ranking_mock.assert_has_calls([
            mocker.call(return_sesson, "test001", "test001_01", "GTEST1"),
            mocker.call(return_sesson, "test002", "test002_01", "GTEST2"),
        ]
    )
    db_ranking_mock.assert_called_once()
    db_ranking_mock.assert_called_with("test001_01", 1111, "2022-11-21T10:10:10+00:00")
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4,5])
    assert sleep_mock.call_count == 3
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
            mocker.call(1),
        ])
    

def test_rank_chart_empty_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    return_sesson = {"test": 12345}
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    stage_data = [{
                    "test001": "test001"
                }]
    score_return = {
        "responseCode": 200,
        "responseMessage": "OK",
        "response": {
            "id": 123456789,
            "cardId": "1234567890123456",
            "name": "test001",
            "stages": stage_data
        }
    }
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", return_value=score_return)
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=HTTPError())
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True)
    assert result == "指定された難易度を未プレイもしくはスコアデータが本ツールで取得されていません。\nプレイ状況をご確認ください。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(stage_data)
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4,5])
    assert sleep_mock.call_count == 2
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
        ])


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 20, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_score_other_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    return_sesson = {"test": 12345}
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.mypagedata.getRankingData")
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True)
    assert result == "予期せぬエラーが発生しました。時間をおいてやり直してください。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)


def test_login_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.mypagedata.getRankingData")
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True)
    assert result == "ログインに失敗しました。ユーザIDもしくはパスワードが正しいか確認してください。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_not_called()


def test_nolevel_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.mypagedata.getRankingData")
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, False, False, False, False, False)
    assert result == "ランキング情報取得時は取得したい難易度を必ず1つ以上選択してください。"
    login_mock.assert_not_called()
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_not_called()


def test_nogetdata_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.mypagedata.getRankingData")
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, False, True, True, True, True, True)
    assert result == "取得したいデータの種類を必ず1つ以上選択してください。"
    login_mock.assert_not_called()
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_not_called()


def test_loginid_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.mypagedata.getRankingData")
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginPageData("", "password1", True, True, True, True, True, True, True)
    assert result == "ユーザ名およびパスワードは必ず入力してください。"
    login_mock.assert_not_called()
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_not_called()


def test_password_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.mypagedata.getRankingData")
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginPageData("1234567890123456", "", True, True, True, True, True, True, True)
    assert result == "ユーザ名およびパスワードは必ず入力してください。"
    login_mock.assert_not_called()
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_not_called()

