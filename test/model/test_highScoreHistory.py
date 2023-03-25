# coding:utf-8
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from model import highScoreHistory


def setup_test():
    testObj = highScoreHistory.HighScoreHistory()
    return testObj


def test_empty(mocker):
    testObj = setup_test()
    mock = mocker.patch("db.highscorehistory.selectHighScoreHistoryBychartId", return_value=[])
    assert testObj.getHighScoreHistoryByChartId("test001_001") == []
    mock.assert_called_once()
    mock.assert_called_with("test001_001")


def test_one_data(mocker):
    testObj = setup_test()
    results = [
        {
            "chartId": "test001_001",
            "mode": 1,
            "highScore": 1234567, 
            "maxCombo": 123, 
            "updateTime": "2023-01-07T21:09:01+00:00"
        }
    ]
    mock = mocker.patch("db.highscorehistory.selectHighScoreHistoryBychartId", return_value=results)
    success = [
        {
            "mode": "シングルプレイ",
            "highScore": "1234567",
            "maxCombo": "123",
            "updateTime": "2023年1月8日 06:09:01"
        }
    ]
    assert testObj.getHighScoreHistoryByChartId("test001_001") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_001")


def test_three_data(mocker):
    testObj = setup_test()
    results = [
        {
            "chartId": "test001_001",
            "mode": 1,
            "highScore": 1234567, 
            "maxCombo": 123, 
            "updateTime": "2023-01-07T21:09:01+00:00"
        },
        {
            "chartId": "test001_001",
            "mode": 3,
            "highScore": 1234569, 
            "maxCombo": 120, 
            "updateTime": "2023-01-06T21:09:01+00:00"
        },
        {
            "chartId": "test001_001",
            "mode": 1,
            "highScore": 1224567, 
            "maxCombo": 100, 
            "updateTime": "2023-01-05T21:09:01+00:00"
        },
    ]
    mock = mocker.patch("db.highscorehistory.selectHighScoreHistoryBychartId", return_value=results)
    success = [
        {
            "mode": "シングルプレイ",
            "highScore": "1234567",
            "maxCombo": "123",
            "updateTime": "2023年1月8日 06:09:01"
        },
        {
            "mode": "協力プレイ(3人)",
            "highScore": "1234569",
            "maxCombo": "120",
            "updateTime": "2023年1月7日 06:09:01"
        },
        {
            "mode": "シングルプレイ",
            "highScore": "1224567",
            "maxCombo": "100",
            "updateTime": "2023年1月6日 06:09:01"
        },
    ]
    assert testObj.getHighScoreHistoryByChartId("test001_001") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_001")
