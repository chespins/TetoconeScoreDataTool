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
    mock = mocker.patch("db.highscore.selectHighScoreByChartId", return_value=[])
    success = {
        "highScore": "0",
        "maxCombo":  "0",
        "playCount": "0回",
        "clearedCount": "0回",
        "fullComboCount": "0回",
        "perfectCount": "0回",
        "lastUpdateTime": "2000年1月1日 09:00:00"
    }
    assert testObj.getHighScoreByMusic("test001_001", "協力プレイ(2人)") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_001")


def test_one_data(mocker):
    testObj = setup_test_obj()
    return_value = [
        {
            "chartId": "test001_01",
            "mode": 1,
            "musicId": "test001",
            "highScore": 1234567,
            "maxCombo": 123,
            "playCount": 4,
            "clearedCount": 3,
            "fullComboCount": 2,
            "perfectCount": 1,
            "updateTime": "2020-01-03T12:00:00+00:00"
        },
    ]
    mock = mocker.patch("db.highscore.selectHighScoreByChartId", return_value=return_value)
    success = {
        "highScore": "1234567",
        "maxCombo":  "123",
        "playCount": "4回",
        "clearedCount": "3回",
        "fullComboCount": "2回",
        "perfectCount": "1回",
        "lastUpdateTime": "2020年1月3日 21:00:00"
    }
    assert testObj.getHighScoreByMusic("test001_001", "シングルプレイ") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_001")


def test_two_data(mocker):
    testObj = setup_test_obj()
    return_value = [
        {
            "chartId": "test001_01",
            "mode": 3,
            "musicId": "test001",
            "highScore": 1234567,
            "maxCombo": 123,
            "playCount": 4,
            "clearedCount": 3,
            "fullComboCount": 2,
            "perfectCount": 1,
            "updateTime": "2020-01-03T12:00:00+00:00"
        },
        {
            "chartId": "test001_01",
            "mode": 4,
            "musicId": "test001",
            "highScore": 2234567,
            "maxCombo": 222,
            "playCount": 1,
            "clearedCount": 1,
            "fullComboCount": 1,
            "perfectCount": 1,
            "updateTime": "2021-01-03T12:00:00+00:00"
        },
    ]
    mock = mocker.patch("db.highscore.selectHighScoreByChartId", return_value=return_value)
    success = {
        "highScore": "2234567",
        "maxCombo":  "222",
        "playCount": "5回",
        "clearedCount": "4回",
        "fullComboCount": "3回",
        "perfectCount": "2回",
        "lastUpdateTime": "2021年1月3日 21:00:00"
    }
    assert testObj.getHighScoreByMusic("test001_001", "全て") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_001")


def test_unmatch_data(mocker):
    testObj = setup_test_obj()
    return_value = [
        {
            "chartId": "test001_01",
            "mode": 1,
            "musicId": "test001",
            "highScore": 1234567,
            "maxCombo": 123,
            "playCount": 4,
            "clearedCount": 3,
            "fullComboCount": 2,
            "perfectCount": 1,
            "updateTime": "2020-01-03T12:00:00+00:00"
        },
        {
            "chartId": "test001_01",
            "mode": 2,
            "musicId": "test001",
            "highScore": 2234567,
            "maxCombo": 222,
            "playCount": 1,
            "clearedCount": 1,
            "fullComboCount": 1,
            "perfectCount": 1,
            "updateTime": "2021-01-03T12:00:00+00:00"
        },
    ]
    mock = mocker.patch("db.highscore.selectHighScoreByChartId", return_value=return_value)
    success = {
        "highScore": "1234567",
        "maxCombo":  "123",
        "playCount": "4回",
        "clearedCount": "3回",
        "fullComboCount": "2回",
        "perfectCount": "1回",
        "lastUpdateTime": "2020年1月3日 21:00:00"
    }
    assert testObj.getHighScoreByMusic("test001_001", "シングルプレイ") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_001")
