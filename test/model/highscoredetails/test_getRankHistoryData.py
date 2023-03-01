# coding:utf-8
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import highscoredetails


def setup_test_obj():
    testObj = highscoredetails.HighScoreFormusic()
    return testObj


def test_empty(mocker):
    testObj = setup_test_obj()
    mock = mocker.patch.object(testObj, "getRankData", return_value={})
    assert testObj.getRankHistoryDataForChartId("test001_001", "全て") == []
    mock.assert_called_once()
    mock.assert_called_with("test001_001", {1, 2, 3, 4, 5, 6})


def test_one_data(mocker):
    testObj = setup_test_obj()
    return_value = {
        "SSS": {
            "rank": "SSS",
            "count": 5
        },
    }
    mock = mocker.patch.object(testObj, "getRankData", return_value=return_value)
    success = [
        {
            "rank": "SS+",
            "count": "5回"
        }
    ]
    assert testObj.getRankHistoryDataForChartId("test001_001", "協力プレイ(全て)") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_001", {2, 3, 4})


def test_three_data(mocker):
    testObj = setup_test_obj()
    return_value = {
        "AAA": {
            "rank": "AAA",
            "count": 3
        },
        "S": {
            "rank": "S",
            "count": 2
        },
        "BBB": {
            "rank": "BBB",
            "count": 4
        },
    }
    mock = mocker.patch.object(testObj, "getRankData", return_value=return_value)
    success = [
        {
            "rank": "S",
            "count": "2回"
        },
        {
            "rank": "AA+",
            "count": "3回"
        },
        {
            "rank": "BB+",
            "count": "4回"
        },
    ]
    assert testObj.getRankHistoryDataForChartId("test001_001", "対戦プレイ(2人)") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_001", {5})
