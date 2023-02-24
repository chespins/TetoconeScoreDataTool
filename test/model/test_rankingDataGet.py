# coding:utf-8
import pytest
import sys
import os
import datetime
from requests import HTTPError

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from model import rankingDataGet
from model.mypagedata import RankingDate
from exception.loginerror import LoginError

@pytest.mark.freeze_time(datetime.datetime(2022, 11, 20, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_getLoginRankingData_success(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[{
                    "chartId": "test001_01",
                    "musicId": "test001",
                    "levelId": 2,
                    "genreId": "GTEST",
                    "highScore": 123456,
                }])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value={"test": 12345})
    ranking = RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":123456,
                "rank":910
            }
        })
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", return_value=ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.rankingDataGet.sleep")

    assert rankingDataGet.getLoginRankingData("1234567890123456", "password1", "test001_01") == "マイページからのデータ取得が成功しました。"
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test001_01")
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with({"test": 12345}, "test001", "test001_01", "GTEST")
    db_ranking_mock.assert_called_once()
    db_ranking_mock.assert_called_with("test001_01", 910, "2022-11-20T10:10:10+00:00")
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    

@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_getLoginRankingData_score_unmatch(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[{
                    "chartId": "test002_01",
                    "musicId": "test002",
                    "levelId": 2,
                    "genreId": "GTEST",
                    "highScore": 123456,
                }])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value={"test": 12345})
    ranking = RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":23456,
                "rank":819
            }
        })
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", return_value=ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.rankingDataGet.sleep")

    assert rankingDataGet.getLoginRankingData("1234567890123456", "password1", "test002_01") == "取得済のスコアデータとランキングデータに差異がありました。\nスコアデータを取り直してください。"
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test002_01")
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with({"test": 12345}, "test002", "test002_01", "GTEST")
    db_ranking_mock.assert_not_called()
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)


def test_getLoginRankingData_data_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[{
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 2,
                    "genreId": "GTEST",
                    "highScore": 123456,
                }])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value={"test": 12345})
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=HTTPError())
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.rankingDataGet.sleep")

    assert rankingDataGet.getLoginRankingData("1234567890123456", "password1", "test003_01") == "予期せぬエラーが発生しました。時間をおいてやり直してください。"
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test003_01")
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with({"test": 12345}, "test003", "test003_01", "GTEST")
    db_ranking_mock.assert_not_called()
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)

def test_getLoginRankingData_login_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[{
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 2,
                    "genreId": "GTEST",
                    "highScore": 123456,
                }])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=HTTPError())
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.rankingDataGet.sleep")

    assert rankingDataGet.getLoginRankingData("1234567890123456", "password1", "test003_01") == "ログインに失敗しました。ユーザIDもしくはパスワードが正しいか確認してください。"
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test003_01")
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    sleep_mock.assert_not_called()

def test_getLoginRankingData_chart_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[{
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 2,
                    "genreId": "GTEST",
                    "highScore": 123456,
                },
                {
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 21,
                    "genreId": "GTEST",
                    "highScore": 123456,
                }])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=HTTPError())
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.rankingDataGet.sleep")

    assert rankingDataGet.getLoginRankingData("1234567890123456", "password1", "test003_01") == "取得済のスコアデータとランキングデータに差異がありました。\nスコアデータを取り直してください。"
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test003_01")
    login_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    sleep_mock.assert_not_called()

def test_getLoginRankingData_id_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[{
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 2,
                    "genreId": "GTEST",
                    "highScore": 123456,
                },
                {
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 21,
                    "genreId": "GTEST",
                    "highScore": 123456,
                }])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=HTTPError())
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.rankingDataGet.sleep")

    assert rankingDataGet.getLoginRankingData("", "password1", "test003_01") == "ユーザ名およびパスワードは必ず入力してください。"
    db_chart_mock.assert_not_called()
    login_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    sleep_mock.assert_not_called()


def test_getLoginRankingData_password_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[{
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 2,
                    "genreId": "GTEST",
                    "highScore": 123456,
                },
                {
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 21,
                    "genreId": "GTEST",
                    "highScore": 123456,
                }])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=HTTPError())
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.rankingDataGet.sleep")

    assert rankingDataGet.getLoginRankingData("1234567890123456", "", "test003_01") == "ユーザ名およびパスワードは必ず入力してください。"
    db_chart_mock.assert_not_called()
    login_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    sleep_mock.assert_not_called()
