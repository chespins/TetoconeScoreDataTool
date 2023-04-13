# coding:utf-8
import pytest
import sys
import os
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import getloginpage
from model.mypagedata import RankingDate


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_connect_false(mocker):
    return_chart = [{
                    "chartId": "test001_01",
                    "musicId": "test001",
                    "levelId": 1,
                    "genreId": "GTEST1",
                    "highScore": 111,
                },]
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
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
                "score":222,
                "rank":2222
            }
        }),
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData")
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")
    character_mock = mocker.patch("model.mypagedata.getCharacterData")
    character_ranking_mock = mocker.patch("model.mypagedata.getCharacterRanking")
    db_character_mock = mocker.patch("model.datainserts.insertCharacter")
    db_introduction_mock = mocker.patch("db.character.selectCharacter")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, False, False, False)
    assert result == "マイページからのデータ取得が成功しました。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(stage_data)
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(return_sesson, "test001", "test001_01", "GTEST1"),
    db_ranking_mock.assert_called_once()
    db_ranking_mock.assert_called_with("test001_01", 1111, "2022-11-21T10:10:10+00:00")
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4])
    assert sleep_mock.call_count == 3
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
            mocker.call(1),
        ])
    degrees_mock.assert_not_called()
    db_degrees_mock.assert_not_called()
    character_mock.assert_not_called()
    character_ranking_mock.assert_not_called()
    db_character_mock.assert_not_called()
    db_introduction_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_maniac_false(mocker):
    return_chart = [{
                    "chartId": "test001_01",
                    "musicId": "test001",
                    "levelId": 1,
                    "genreId": "GTEST1",
                    "highScore": 111,
                },
                {
                    "chartId": "test002_01",
                    "musicId": "test002",
                    "levelId": 2,
                    "genreId": "GTEST2",
                    "highScore": 222,
                },]
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
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
                "score":222,
                "rank":2222
            }
        }),
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData")
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")
    character_mock = mocker.patch("model.mypagedata.getCharacterData")
    character_ranking_mock = mocker.patch("model.mypagedata.getCharacterRanking")
    db_character_mock = mocker.patch("model.datainserts.insertCharacter")
    db_introduction_mock = mocker.patch("db.character.selectCharacter")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, False, True, False, False)
    assert result == "マイページからのデータ取得が成功しました。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(stage_data)
    assert ranking_mock.call_count == 2
    ranking_mock.assert_has_calls([
            mocker.call(return_sesson, "test001", "test001_01", "GTEST1"),
            mocker.call(return_sesson, "test002", "test002_01", "GTEST2"),
        ]
    )
    assert db_ranking_mock.call_count == 2
    db_ranking_mock.assert_has_calls([
            mocker.call("test001_01", 1111, "2022-11-21T10:10:10+00:00"),
            mocker.call("test002_01", 2222, "2022-11-21T10:10:10+00:00"),
        ]
    )
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,5])
    assert sleep_mock.call_count == 4
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
        ])
    degrees_mock.assert_not_called()
    db_degrees_mock.assert_not_called()
    character_mock.assert_not_called()
    character_ranking_mock.assert_not_called()
    db_character_mock.assert_not_called()
    db_introduction_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_ultimate_false(mocker):
    return_chart = [{
                    "chartId": "test001_01",
                    "musicId": "test001",
                    "levelId": 1,
                    "genreId": "GTEST1",
                    "highScore": 111,
                },
                {
                    "chartId": "test002_01",
                    "musicId": "test002",
                    "levelId": 2,
                    "genreId": "GTEST2",
                    "highScore": 222,
                },]
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
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
                "score":222,
                "rank":2222
            }
        }),
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData")
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")
    character_mock = mocker.patch("model.mypagedata.getCharacterData")
    character_ranking_mock = mocker.patch("model.mypagedata.getCharacterRanking")
    db_character_mock = mocker.patch("model.datainserts.insertCharacter")
    db_introduction_mock = mocker.patch("db.character.selectCharacter")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, False, True, True, False, False)
    assert result == "マイページからのデータ取得が成功しました。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(stage_data)
    assert ranking_mock.call_count == 2
    ranking_mock.assert_has_calls([
            mocker.call(return_sesson, "test001", "test001_01", "GTEST1"),
            mocker.call(return_sesson, "test002", "test002_01", "GTEST2"),
        ]
    )
    assert db_ranking_mock.call_count == 2
    db_ranking_mock.assert_has_calls([
            mocker.call("test001_01", 1111, "2022-11-21T10:10:10+00:00"),
            mocker.call("test002_01", 2222, "2022-11-21T10:10:10+00:00"),
        ]
    )
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,4,5])
    assert sleep_mock.call_count == 4
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
        ])
    degrees_mock.assert_not_called()
    db_degrees_mock.assert_not_called()
    character_mock.assert_not_called()
    character_ranking_mock.assert_not_called()
    db_character_mock.assert_not_called()
    db_introduction_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_expert_false(mocker):
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
                },]
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
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
                "score":222,
                "rank":2222
            }
        }),
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData")
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")
    character_mock = mocker.patch("model.mypagedata.getCharacterData")
    character_ranking_mock = mocker.patch("model.mypagedata.getCharacterRanking")
    db_character_mock = mocker.patch("model.datainserts.insertCharacter")
    db_introduction_mock = mocker.patch("db.character.selectCharacter")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, False, True, True, True, False, False)
    assert result == "マイページからのデータ取得が成功しました。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(stage_data)
    assert ranking_mock.call_count == 2
    ranking_mock.assert_has_calls([
            mocker.call(return_sesson, "test001", "test001_01", "GTEST1"),
            mocker.call(return_sesson, "test002", "test002_01", "GTEST2"),
        ]
    )
    assert db_ranking_mock.call_count == 2
    db_ranking_mock.assert_has_calls([
            mocker.call("test001_01", 1111, "2022-11-21T10:10:10+00:00"),
            mocker.call("test002_01", 2222, "2022-11-21T10:10:10+00:00"),
        ]
    )
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,3,4,5])
    assert sleep_mock.call_count == 4
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
        ])
    degrees_mock.assert_not_called()
    db_degrees_mock.assert_not_called()
    character_mock.assert_not_called()
    character_ranking_mock.assert_not_called()
    db_character_mock.assert_not_called()
    db_introduction_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_standard_false(mocker):
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
                },]
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=return_chart)
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
                "score":222,
                "rank":2222
            }
        }),
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData")
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")
    character_mock = mocker.patch("model.mypagedata.getCharacterData")
    character_ranking_mock = mocker.patch("model.mypagedata.getCharacterRanking")
    db_character_mock = mocker.patch("model.datainserts.insertCharacter")
    db_introduction_mock = mocker.patch("db.character.selectCharacter")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, False, True, True, True, True, False, False)
    assert result == "マイページからのデータ取得が成功しました。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(stage_data)
    assert ranking_mock.call_count == 2
    ranking_mock.assert_has_calls([
            mocker.call(return_sesson, "test001", "test001_01", "GTEST1"),
            mocker.call(return_sesson, "test002", "test002_01", "GTEST2"),
        ]
    )
    assert db_ranking_mock.call_count == 2
    db_ranking_mock.assert_has_calls([
            mocker.call("test001_01", 1111, "2022-11-21T10:10:10+00:00"),
            mocker.call("test002_01", 2222, "2022-11-21T10:10:10+00:00"),
        ]
    )
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[2,3,4,5])
    assert sleep_mock.call_count == 4
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
        ])
    degrees_mock.assert_not_called()
    db_degrees_mock.assert_not_called()
    character_mock.assert_not_called()
    character_ranking_mock.assert_not_called()
    db_character_mock.assert_not_called()
    db_introduction_mock.assert_not_called()
