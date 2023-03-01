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
    assert testObj.makeModeNamePulldown("test001_01") == []
    mock.assert_called_once()
    mock.assert_called_with("test001_01")


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
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
    ]
    mock = mocker.patch("db.highscore.selectHighScoreByChartId", return_value=return_value)
    assert testObj.makeModeNamePulldown("test001_01") == ["シングルプレイ"]
    mock.assert_called_once()
    mock.assert_called_with("test001_01")


def test_three_data_1(mocker):
    testObj = setup_test_obj()
    return_value = [
        {
            "chartId": "test001_01",
            "mode": 2,
            "musicId": "test001",
            "highScore": 1234567,
            "maxCombo": 123,
            "playCount": 4,
            "clearedCount": 3,
            "fullComboCount": 2,
            "perfectCount": 1,
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
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
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
        {
            "chartId": "test001_01",
            "mode": 4,
            "musicId": "test001",
            "highScore": 1234567,
            "maxCombo": 123,
            "playCount": 4,
            "clearedCount": 3,
            "fullComboCount": 2,
            "perfectCount": 1,
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
    ]
    mock = mocker.patch("db.highscore.selectHighScoreByChartId", return_value=return_value)
    success = [
        "全て",
        "協力プレイ(全て)",
        "協力プレイ(2人)",
        "協力プレイ(3人)",
        "協力プレイ(4人)"
    ]
    assert testObj.makeModeNamePulldown("test001_01") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_01")


def test_three_data_2(mocker):
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
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
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
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
        {
            "chartId": "test001_01",
            "mode": 6,
            "musicId": "test001",
            "highScore": 1234567,
            "maxCombo": 123,
            "playCount": 4,
            "clearedCount": 3,
            "fullComboCount": 2,
            "perfectCount": 1,
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
    ]
    mock = mocker.patch("db.highscore.selectHighScoreByChartId", return_value=return_value)
    success = [
        "全て",
        "シングルプレイ",
        "協力プレイ(全て)",
        "協力プレイ(3人)",
        "対戦プレイ(全て)",
        "対戦プレイ(4人)"
    ]
    assert testObj.makeModeNamePulldown("test001_01") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_01")


def test_all_data(mocker):
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
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
        {
            "chartId": "test001_01",
            "mode": 2,
            "musicId": "test001",
            "highScore": 1234567,
            "maxCombo": 123,
            "playCount": 4,
            "clearedCount": 3,
            "fullComboCount": 2,
            "perfectCount": 1,
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
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
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
        {
            "chartId": "test001_01",
            "mode": 4,
            "musicId": "test001",
            "highScore": 1234567,
            "maxCombo": 123,
            "playCount": 4,
            "clearedCount": 3,
            "fullComboCount": 2,
            "perfectCount": 1,
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
        {
            "chartId": "test001_01",
            "mode": 5,
            "musicId": "test001",
            "highScore": 1234567,
            "maxCombo": 123,
            "playCount": 4,
            "clearedCount": 3,
            "fullComboCount": 2,
            "perfectCount": 1,
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
        {
            "chartId": "test001_01",
            "mode": 6,
            "musicId": "test001",
            "highScore": 1234567,
            "maxCombo": 123,
            "playCount": 4,
            "clearedCount": 3,
            "fullComboCount": 2,
            "perfectCount": 1,
            "updateTime": "2000-01-01T00:00:00+00:00"
        },
    ]
    mock = mocker.patch("db.highscore.selectHighScoreByChartId", return_value=return_value)
    success = [
        "全て",
        "シングルプレイ",
        "協力プレイ(全て)",
        "協力プレイ(2人)",
        "協力プレイ(3人)",
        "協力プレイ(4人)",
        "対戦プレイ(全て)",
        "対戦プレイ(2人)",
        "対戦プレイ(4人)",
    ]
    assert testObj.makeModeNamePulldown("test001_01") == success
    mock.assert_called_once()
    mock.assert_called_with("test001_01")

