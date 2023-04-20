# coding:utf-8
import pytest
import sys
import os
import datetime
from common_def import readFileStr

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import getloginpage


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 20, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_score_success(mocker):
    test_data = readFileStr("success_data_score.json") 
    return_sesson = test_data["return_sesson"]

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", return_value=test_data["score_return"])
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, False, False, False, False, False, False, False, False)
    assert result == "マイページからのデータ取得が成功しました。"
    
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(test_data["stage_data"])
    ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_rank_sucsess_all_one(mocker):
    test_data = readFileStr("success_data_ranking.json") 
    return_sesson = test_data["return_sesson"]
    return_chart = test_data["return_chart"]
    
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=False)
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, True, True, True, True, True, False, False)
    assert result == "マイページからのデータ取得が成功しました。"

    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(return_sesson, return_chart)
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4,5])
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_degrees_sucsess(mocker):
    return_sesson = {"test": 12345}

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart")
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=False)
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, False, False, False, False, False, False, True, False)
    assert result == "マイページからのデータ取得が成功しました。"
    
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_called_once()
    degrees_mock.assert_called_with(return_sesson)
    character_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_character_sucsess(mocker):
    test_data = readFileStr("success_data_character.json")
    return_sesson = test_data["return_sesson"]

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart")
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", return_value=test_data["score_return"])
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, False, False, False, False, False, False, False, True)
    assert result == "マイページからのデータ取得が成功しました。"

    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(test_data["return_sesson"])
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_called_once()
    character_mock.assert_called_with(return_sesson, test_data["characters_param"])


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_all(mocker):
    test_data = readFileStr("success_data_all.json")
    return_sesson = test_data["return_sesson"]
    return_chart = test_data["return_chart"]

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", return_value=test_data["score_return"])
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=False)
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True, True, True)
    assert result == "マイページからのデータ取得が成功しました。"

    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(test_data["stage_data"])
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(return_sesson, return_chart)
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4,5])
    assert sleep_mock.call_count == 2
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
        ])
    degrees_mock.assert_called_once()
    degrees_mock.assert_called_with(return_sesson)
    character_mock.assert_called_once()
    character_mock.assert_called_with(return_sesson, test_data["characters_param"])
