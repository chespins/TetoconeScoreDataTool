# coding:utf-8
import pytest
import sys
import os
import datetime
from requests import HTTPError
from common_def import readFileStr

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import getloginpage
from model.mypagedata import RankingDate
from exception.loginerror import LoginError

def getTestData():
    params = readFileStr("rankingDataGet.json")
    return (params["chart_return"], params["session"])


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 20, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_success(mocker):
    (chart_return, session) = getTestData()

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=chart_return)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=session)
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=False)
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginRankingData("1234567890123456", "password1", "test001_01")
    assert result  == "マイページからのデータ取得が成功しました。"

    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test001_01")
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(session, chart_return)
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    

@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_score_unmatch(mocker):
    (chart_return, session) = getTestData()

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=chart_return)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=session)
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=True)
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginRankingData("1234567890123456", "password1", "test001_01")
    assert result == "取得済のスコアデータとランキングデータに差異がありました。\nスコアデータを取り直してください。"
    
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test001_01")
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(session, chart_return)
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)


def test_data_error(mocker):
    (chart_return, session) = getTestData()

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=chart_return)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=session)
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", side_effect=HTTPError())
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginRankingData("1234567890123456", "password1", "test001_01")
    assert result == "予期せぬエラーが発生しました。時間をおいてやり直してください。"
    
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test001_01")
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(session, chart_return)
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)


def test_login_error(mocker):
    (chart_return, session) = getTestData()
    
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=chart_return)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", side_effect=HTTPError())
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginRankingData("1234567890123456", "password1", "test001_01")
    assert result == "ログインに失敗しました。ユーザIDもしくはパスワードが正しいか確認してください。"
    
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test001_01")
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    ranking_mock.assert_not_called()
    sleep_mock.assert_not_called()


def test_chart_error(mocker):
    params = readFileStr("rankingDataGet.json")

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=params["chart_error_return"])
    login_mock = mocker.patch("model.mypagedata.loginMyPage")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result =  getloginpage.getLoginRankingData("1234567890123456", "password1", "test003_01")
    assert result == "取得済のスコアデータとランキングデータに差異がありました。\nスコアデータを取り直してください。"

    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(chartId="test003_01")
    login_mock.assert_not_called()
    ranking_mock.assert_not_called()
    sleep_mock.assert_not_called()


def test_id_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart")
    login_mock = mocker.patch("model.mypagedata.loginMyPage")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginRankingData("", "password1", "test003_01")
    assert result == "ユーザ名およびパスワードは必ず入力してください。"
    
    db_chart_mock.assert_not_called()
    login_mock.assert_not_called()
    ranking_mock.assert_not_called()
    sleep_mock.assert_not_called()


def test_password_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart")
    login_mock = mocker.patch("model.mypagedata.loginMyPage")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")

    result = getloginpage.getLoginRankingData("1234567890123456", "", "test003_01")
    assert result == "ユーザ名およびパスワードは必ず入力してください。"
    
    db_chart_mock.assert_not_called()
    login_mock.assert_not_called()
    ranking_mock.assert_not_called()
    sleep_mock.assert_not_called()
