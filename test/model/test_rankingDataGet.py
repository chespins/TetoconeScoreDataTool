# coding:utf-8
import pytest
import sys
import os
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from model import rankingDataGet
from model.mypagedata import RankingDate
from exception.loginerror import LoginError

@pytest.mark.freeze_time(datetime.datetime(2022, 11, 20, 19, 10, 10, tzinfo=datetime.timezone.utc))
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

    assert rankingDataGet.getLoginRankingData("1234567890123456", "password1", "test001_01") == "マイページからのデータ取得が成功しました。"
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test001_01")
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with({"test": 12345}, "test001", "test001_01", "GTEST")
    db_ranking_mock.assert_called_once()
    db_ranking_mock.assert_called_with("test001_01", 910, "2022-11-20T10:10:10+00:00")

    
    