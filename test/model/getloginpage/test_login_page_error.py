# coding:utf-8
import pytest
import sys
import os
import datetime
from requests import HTTPError
from common_def import readFileStr

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import getloginpage
from exception.loginerror import LoginError


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_rank_data_unmatch(mocker):
    test_data = readFileStr("success_data_ranking.json") 
    return_sesson = test_data["return_sesson"]
    return_chart = test_data["return_chart"]
    
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=True)
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, True, True, True, True, True, True, False)
    assert result == "取得済のスコアデータとランキングデータに差異がありました。\nスコアデータを取り直してください。"
    
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
    

def test_all_chart_empty_error(mocker):
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

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True, True, False)
    assert result == "指定された難易度を未プレイもしくはスコアデータが本ツールで取得されていません。\nプレイ状況をご確認ください。"
    
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(test_data["stage_data"])
    ranking_mock.assert_not_called()
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4,5])
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


def test_rank_chart_empty_error(mocker):
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

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, True, True, True, True, True, True, False)
    assert result == "指定された難易度を未プレイもしくはスコアデータが本ツールで取得されていません。\nプレイ状況をご確認ください。"

    login_mock.assert_not_called()
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4,5])
    sleep_mock.assert_not_called()
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 20, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_score_other_error(mocker):
    test_data = readFileStr("success_data_score.json") 
    return_sesson = test_data["return_sesson"]

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True, True, True)
    assert result == "予期せぬエラーが発生しました。時間をおいてやり直してください。"

    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 20, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_character_other_error(mocker):
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
    character_mock = mocker.patch("model.getloginpage.getCharacterData", side_effect=HTTPError())

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True, True, True)
    assert result == "予期せぬエラーが発生しました。時間をおいてやり直してください。"

    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    character_mock.assert_called_once()
    character_mock.assert_called_with(return_sesson, test_data["characters_param"])


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 20, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_ranking_other_error(mocker):
    test_data = readFileStr("success_data_all.json")
    return_sesson = test_data["return_sesson"]
    return_chart = test_data["return_chart"]

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", return_value=test_data["score_return"])
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", side_effect=HTTPError())
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True, True, True)
    assert result == "予期せぬエラーが発生しました。時間をおいてやり直してください。"

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
    degrees_mock.assert_not_called()
    character_mock.assert_called_once()
    character_mock.assert_called_with(return_sesson, test_data["characters_param"])


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 20, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_degrees_other_error(mocker):
    test_data = readFileStr("success_data_all.json")
    return_sesson = test_data["return_sesson"]
    return_chart = test_data["return_chart"]

    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", return_value=test_data["score_return"])
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData", return_value=False)
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData", side_effect=HTTPError())
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True, True, True)
    assert result == "予期せぬエラーが発生しました。時間をおいてやり直してください。"

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


def test_login_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True, True, True)
    assert result == "ログインに失敗しました。ユーザIDもしくはパスワードが正しいか確認してください。"

    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_not_called()
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


def test_nolevel_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, False, False, False, False, False, True, True)
    assert result == "ランキング情報取得時は取得したい難易度を必ず1つ以上選択してください。"
    login_mock.assert_not_called()
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_not_called()
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


def test_nogetdata_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, False, True, True, True, True, True, False, False)
    assert result == "取得したいデータの種類を必ず1つ以上選択してください。"
    login_mock.assert_not_called()
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_not_called()
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


def test_loginid_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("", "password1", True, True, True, True, True, True, True, True, True)
    assert result == "ユーザ名およびパスワードは必ず入力してください。"
    login_mock.assert_not_called()
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_not_called()
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()


def test_password_error(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    login_mock = mocker.patch("model.mypagedata.loginMyPage", side_effect=LoginError())
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData", side_effect=HTTPError())
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.getloginpage.getScoreRankingData")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.getloginpage.getDegreesData")
    character_mock = mocker.patch("model.getloginpage.getCharacterData")

    result = getloginpage.getLoginPageData("1234567890123456", "", True, True, True, True, True, True, True, True, True)
    assert result == "ユーザ名およびパスワードは必ず入力してください。"
    login_mock.assert_not_called()
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_not_called()
    degrees_mock.assert_not_called()
    character_mock.assert_not_called()
