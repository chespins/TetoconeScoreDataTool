# coding:utf-8
import pytest
import sys
import os
import datetime
from common_def import readFileStr

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import getloginpage


def input_data_get():
    test_data = readFileStr("success_data_ranking.json")
    return_sesson = test_data["return_sesson"]
    return_chart = test_data["return_chart"]
    return (return_sesson, return_chart)


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_connect_false(mocker):
    (return_sesson, return_chart) = input_data_get()
    
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=False)
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, True, True, True, True, False, False, False)
    assert result == "マイページからのデータ取得が成功しました。"

    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(return_sesson, return_chart)
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4])
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_maniac_false(mocker):
    (return_sesson, return_chart) = input_data_get()
    
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=False)
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, True, True, True, False, True, False, False)
    assert result == "マイページからのデータ取得が成功しました。"

    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(return_sesson, return_chart)
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,5])
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_ultimate_false(mocker):
    (return_sesson, return_chart) = input_data_get()
 
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=False)
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, True, True, False, True, True, False, False)
    assert result == "マイページからのデータ取得が成功しました。"

    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(return_sesson, return_chart)
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,4,5])
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_expert_false(mocker):
    (return_sesson, return_chart) = input_data_get()
 
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=False)
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, True, False, True, True, True, False, False)
    assert result == "マイページからのデータ取得が成功しました。"

    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(return_sesson, return_chart)
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,3,4,5])
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_standard_false(mocker):
    (return_sesson, return_chart) = input_data_get()
 
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=False)
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, False, True, True, True, True, False, False)
    assert result == "マイページからのデータ取得が成功しました。"
    
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(return_sesson, return_chart)
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[2,3,4,5])
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()
