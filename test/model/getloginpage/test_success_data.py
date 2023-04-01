# coding:utf-8
import pytest
import sys
import os
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import getloginpage
from model.mypagedata import RankingDate


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 20, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_score_success(mocker):
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
    ranking_mock = mocker.patch("model.mypagedata.getRankingData")
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData")
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, False, False, False, False, False, False, False)
    assert result == "マイページからのデータ取得が成功しました。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(stage_data)
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(3)
    degrees_mock.assert_not_called()
    db_degrees_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_rank_sucsess_all_one(mocker):
    return_chart = [{
                    "chartId": "test001_01",
                    "musicId": "test001",
                    "levelId": 0,
                    "genreId": "GTEST1",
                    "highScore": 111,
                },]
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
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData")
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, True, True, True, True, True, True, False)
    assert result == "マイページからのデータ取得が成功しました。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(return_sesson, "test001", "test001_01", "GTEST1")
    db_ranking_mock.assert_called_once()
    db_ranking_mock.assert_called_with("test001_01", 1111, "2022-11-21T10:10:10+00:00")
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4,5])
    assert sleep_mock.call_count == 2
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
        ])
    degrees_mock.assert_not_called()
    db_degrees_mock.assert_not_called()


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_degrees_sucsess(mocker):
    db_chart_mock = mocker.patch("db.chartconstitution.selectedSingleChart", return_value=[])
    return_sesson = {"test": 12345}
    login_mock = mocker.patch("model.mypagedata.loginMyPage", return_value=return_sesson)
    score_get_mock = mocker.patch("model.mypagedata.getConnectPageData")
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    
    insert_mock = mocker.patch("model.datainserts.InsertMusic")
    ranking_mock = mocker.patch("model.mypagedata.getRankingData")
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_return = [
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test001": "test001"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test002": "test002"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test003": "test003"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test004": "test004"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test005": "test005"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test006": "test006"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test007": "test007"
            }]
        },
    ]
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData", side_effect=degrees_return)
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", False, False, False, False, False, False, False, True)
    assert result == "マイページからのデータ取得が成功しました。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_not_called()
    insert_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_ranking_mock.assert_not_called()
    db_chart_mock.assert_not_called()
    assert sleep_mock.call_count == 7
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
        ])
    assert degrees_mock.call_count == 6
    degrees_mock.assert_has_calls([
            mocker.call(return_sesson, "Stage"),
            mocker.call(return_sesson, "Partner"),
            mocker.call(return_sesson, "Accessory"),
            mocker.call(return_sesson, "System"),
            mocker.call(return_sesson, "MultiMode"),
            mocker.call(return_sesson, "Event"),
        ])
    db_degrees_mock.assert_called_once()
    db_degrees_param = {
        "Stage": [{
            "test001": "test001"
        }],
        "Partner": [{
            "test002": "test002"
        }],
        "Accessory": [{
            "test003": "test003"
        }],
        "System": [{
            "test004": "test004"
        }],
        "MultiMode": [{
            "test005": "test005"
        }],
        "Event": [{
            "test006": "test006"
        }]
    }
    db_degrees_mock.assert_called_with(db_degrees_param)


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_all_sucsess_all_five(mocker):
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
                },
                {
                    "chartId": "test003_01",
                    "musicId": "test003",
                    "levelId": 3,
                    "genreId": "GTEST3",
                    "highScore": 333,
                },
                {
                    "chartId": "test004_01",
                    "musicId": "test004",
                    "levelId": 4,
                    "genreId": "GTEST4",
                    "highScore": 444,
                },
                {
                    "chartId": "test005_01",
                    "musicId": "test005",
                    "levelId": 5,
                    "genreId": "GTEST5",
                    "highScore": 555,
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
        RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":333,
                "rank":3333
            }
        }),
        RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":444,
                "rank":4444
            }
        }),
        RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":555,
                "rank":5555
            }
        })
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    degrees_return = [
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test001": "test001"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test002": "test002"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test003": "test003"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test004": "test004"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test005": "test005"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test006": "test006"
            }]
        },
        {
            "responseCode": 200,
            "responseMessage": "OK",
            "response": [{
                "test007": "test007"
            }]
        },
    ]
    degrees_mock = mocker.patch("model.mypagedata.getDegreesData", side_effect=degrees_return)
    db_degrees_mock = mocker.patch("model.datainserts.insertDegrees")

    result = getloginpage.getLoginPageData("1234567890123456", "password1", True, True, True, True, True, True, True, True)
    assert result == "マイページからのデータ取得が成功しました。"
    login_mock.assert_called_once()
    login_mock.assert_called_with("1234567890123456", "password1")
    score_get_mock.assert_called_once()
    score_get_mock.assert_called_with(return_sesson)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(stage_data)
    assert ranking_mock.call_count == 5
    ranking_mock.assert_has_calls([
            mocker.call(return_sesson, "test001", "test001_01", "GTEST1"),
            mocker.call(return_sesson, "test002", "test002_01", "GTEST2"),
            mocker.call(return_sesson, "test003", "test003_01", "GTEST3"),
            mocker.call(return_sesson, "test004", "test004_01", "GTEST4"),
            mocker.call(return_sesson, "test005", "test005_01", "GTEST5"),
        ]
    )
    assert db_ranking_mock.call_count == 5
    db_ranking_mock.assert_has_calls([
            mocker.call("test001_01", 1111, "2022-11-21T10:10:10+00:00"),
            mocker.call("test002_01", 2222, "2022-11-21T10:10:10+00:00"),
            mocker.call("test003_01", 3333, "2022-11-21T10:10:10+00:00"),
            mocker.call("test004_01", 4444, "2022-11-21T10:10:10+00:00"),
            mocker.call("test005_01", 5555, "2022-11-21T10:10:10+00:00"),
        ]
    )
    db_chart_mock.assert_called_once()
    db_chart_mock.assert_called_with(levelIdList=[1,2,3,4,5])
    assert sleep_mock.call_count == 13
    sleep_mock.assert_has_calls([
            mocker.call(3),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
        ])
    assert degrees_mock.call_count == 6
    degrees_mock.assert_has_calls([
            mocker.call(return_sesson, "Stage"),
            mocker.call(return_sesson, "Partner"),
            mocker.call(return_sesson, "Accessory"),
            mocker.call(return_sesson, "System"),
            mocker.call(return_sesson, "MultiMode"),
            mocker.call(return_sesson, "Event"),
        ])
    db_degrees_mock.assert_called_once()
    db_degrees_param = {
        "Stage": [{
            "test001": "test001"
        }],
        "Partner": [{
            "test002": "test002"
        }],
        "Accessory": [{
            "test003": "test003"
        }],
        "System": [{
            "test004": "test004"
        }],
        "MultiMode": [{
            "test005": "test005"
        }],
        "Event": [{
            "test006": "test006"
        }]
    }
    db_degrees_mock.assert_called_with(db_degrees_param)

