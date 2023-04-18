# coding:utf-8
import pytest
import sys
import os
import datetime
from common_def import readFileStr

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import getloginpage
from model.mypagedata import RankingDate


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_getScoreRankingData_one_false(mocker):
    input_data = readFileStr("rankingData_one.json")
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
    session = input_data["session"]

    assert not getloginpage.getScoreRankingData(session, input_data["chartList"])

    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(session, "test001", "test001_01", "GTEST1")
    db_ranking_mock.assert_called_once()
    db_ranking_mock.assert_called_with("test001_01", 1111, "2022-11-21T10:10:10+00:00")
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(1)


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_getScoreRankingData_one_true(mocker):
    input_data = readFileStr("rankingData_one.json")
    return_ranking = [
        RankingDate({
            "responseCode":200,
            "responseMessage":"OK",
            "response":{
                "score":112,
                "rank":1111
            }
        }),
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    session = input_data["session"]

    assert getloginpage.getScoreRankingData(session, input_data["chartList"])

    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with(session, "test001", "test001_01", "GTEST1")
    db_ranking_mock.assert_not_called()
    sleep_mock.assert_called_once()
    sleep_mock.assert_called_with(1)


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_getScoreRankingData_three_false(mocker):
    input_data = readFileStr("rankingData_three.json")
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
    ]
    ranking_mock = mocker.patch("model.mypagedata.getRankingData", side_effect=return_ranking)
    db_ranking_mock = mocker.patch("db.ranking.updateRanking")
    sleep_mock = mocker.patch("model.getloginpage.sleep")
    session = input_data["session"]

    assert not getloginpage.getScoreRankingData(session, input_data["chartList"])

    assert ranking_mock.call_count == 3
    ranking_mock.assert_has_calls([
            mocker.call(session, "test001", "test001_01", "GTEST1"),
            mocker.call(session, "test002", "test002_01", "GTEST2"),
            mocker.call(session, "test003", "test003_01", "GTEST3"),
    ])
    assert db_ranking_mock.call_count == 3
    db_ranking_mock.assert_has_calls([
            mocker.call("test001_01", 1111, "2022-11-21T10:10:10+00:00"),
            mocker.call("test002_01", 2222, "2022-11-21T10:10:10+00:00"),
            mocker.call("test003_01", 3333, "2022-11-21T10:10:10+00:00"),
    ])
    assert sleep_mock.call_count == 3
    sleep_mock.assert_has_calls([
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
    ])


@pytest.mark.freeze_time(datetime.datetime(2022, 11, 21, 10, 10, 10, tzinfo=datetime.timezone.utc))
def test_getScoreRankingData_three_true(mocker):
    input_data = readFileStr("rankingData_three.json")
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
                "score":221,
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
    session = input_data["session"]

    assert getloginpage.getScoreRankingData(session, input_data["chartList"])

    assert ranking_mock.call_count == 3
    ranking_mock.assert_has_calls([
            mocker.call(session, "test001", "test001_01", "GTEST1"),
            mocker.call(session, "test002", "test002_01", "GTEST2"),
            mocker.call(session, "test003", "test003_01", "GTEST3"),
    ])
    assert db_ranking_mock.call_count == 2
    db_ranking_mock.assert_has_calls([
            mocker.call("test001_01", 1111, "2022-11-21T10:10:10+00:00"),
            mocker.call("test003_01", 3333, "2022-11-21T10:10:10+00:00"),
    ])
    assert sleep_mock.call_count == 3
    sleep_mock.assert_has_calls([
            mocker.call(1),
            mocker.call(1),
            mocker.call(1),
    ])
