# coding:utf-8
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from model import highscoreSearch

def setup_test():
    testObj = highscoreSearch.HighScoreSearch()
    return testObj


def test_empty(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=123)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="abcde")
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[])
    assert testObj.searchMusic("あいう", "レベル0", "ジャンル0", True) == []
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル0")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル0")
    db_mock.assert_called_once()
    db_mock.assert_called_with("あいう", 123, "abcde")


def test_one_data(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=456)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="fghij")
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 1234,
                    "clearedCount": 1,
                }])
    success = [{
        "musicName": "テスト楽曲1",
        "levelName": "EXPERT",
        "highScore": "1234567",
        "playCount": "1234回",
        "detailsFlg": False,
        "chartId": "test001_01",
    }]
    assert testObj.searchMusic("かきく", "レベル1", "ジャンル1", False) == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    db_mock.assert_called_once()
    db_mock.assert_called_with("かきく", 456, "fghij")


def test_two_played_data(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=456)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="fghij")
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 1234,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲2",
                    "levelId": 5,
                    "mode": 1,
                    "highScore": 7654321,
                    "chartId": "test002_01",
                    "fullComboCount": 2,
                    "perfectCount": 1,
                    "playCount": 5,
                    "clearedCount": 2,
                }])
    success = [{
        "musicName": "テスト楽曲1",
        "levelName": "EXPERT",
        "highScore": "1234567",
        "playCount": "1234回",
        "detailsFlg": False,
        "chartId": "test001_01",
    },
    {
        "musicName": "テスト楽曲2",
        "levelName": "CONNECT",
        "highScore": "7654321",
        "playCount": "5回",
        "detailsFlg": False,
        "chartId": "test002_01",
    }]
    assert testObj.searchMusic("かきく", "レベル1", "ジャンル1", False) == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    db_mock.assert_called_once()
    db_mock.assert_called_with("かきく", 456, "fghij")


def test_one_played_data(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=456)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="fghij")
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 1234,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲2",
                    "levelId": 3,
                    "mode": 1,
                    "highScore": 0,
                    "chartId": "test002_01",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 0,
                    "clearedCount": 0,
                }])
    success = [{
        "musicName": "テスト楽曲1",
        "levelName": "EXPERT",
        "highScore": "1234567",
        "playCount": "1234回",
        "detailsFlg": False,
        "chartId": "test001_01",
    },
    ]
    assert testObj.searchMusic("かきく", "レベル1", "ジャンル1", False) == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    db_mock.assert_called_once()
    db_mock.assert_called_with("かきく", 456, "fghij")


def test_one_played_data_all(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=456)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="fghij")
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 1234,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲2",
                    "levelId": 3,
                    "mode": 1,
                    "highScore": 0,
                    "chartId": "test002_01",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 0,
                    "clearedCount": 0,
                }])
    success = [{
        "musicName": "テスト楽曲1",
        "levelName": "EXPERT",
        "highScore": "1234567",
        "playCount": "1234回",
        "detailsFlg": False,
        "chartId": "test001_01",
    },
    {
        "musicName": "テスト楽曲2",
        "levelName": "ULTIMATE",
        "highScore": "0",
        "playCount": "0回",
        "detailsFlg": True,
        "chartId": "test002_01",
    }
    ]
    assert testObj.searchMusic("かきく", "レベル1", "ジャンル1", True) == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    db_mock.assert_called_once()
    db_mock.assert_called_with("かきく", 456, "fghij")


def test_highScore_diff1(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=456)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="fghij")
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 1234,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲2",
                    "levelId": 2,
                    "mode": 2,
                    "highScore": 1234566,
                    "chartId": "test001_01",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 2,
                    "clearedCount": 0,
                }])
    success = [{
        "musicName": "テスト楽曲1",
        "levelName": "EXPERT",
        "highScore": "1234567",
        "playCount": "1236回",
        "detailsFlg": False,
        "chartId": "test001_01",
    }
    ]
    assert testObj.searchMusic("かきく", "レベル1", "ジャンル1", True) == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    db_mock.assert_called_once()
    db_mock.assert_called_with("かきく", 456, "fghij")

def test_highScore_diff2(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=456)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="fghij")
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 1234,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 2,
                    "highScore": 1234568,
                    "chartId": "test001_01",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 2,
                    "clearedCount": 0,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 3,
                    "highScore": 1234561,
                    "chartId": "test001_01",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 2,
                    "clearedCount": 0,
                }])
    success = [{
        "musicName": "テスト楽曲1",
        "levelName": "EXPERT",
        "highScore": "1234568",
        "playCount": "1238回",
        "detailsFlg": False,
        "chartId": "test001_01",
    }
    ]
    assert testObj.searchMusic("かきく", "レベル1", "ジャンル1", True) == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    db_mock.assert_called_once()
    db_mock.assert_called_with("かきく", 456, "fghij")

def test_no_play_all_true(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=456)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="fghij")
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 1,
                    "mode": 1,
                    "highScore": 0,
                    "chartId": "test001_00",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 0,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 4,
                    "mode": 2,
                    "highScore": 0,
                    "chartId": "test001_04",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 0,
                    "clearedCount": 0,
                },
                {
                    "musicName": "テスト楽曲2",
                    "levelId": 2,
                    "mode": 3,
                    "highScore": 0,
                    "chartId": "test002_01",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 0,
                    "clearedCount": 0,
                }])
    success = [{
        "musicName": "テスト楽曲1",
        "levelName": "STANDARD",
        "highScore": "0",
        "playCount": "0回",
        "detailsFlg": True,
        "chartId": "test001_00",
    },
    {
        "musicName": "テスト楽曲1",
        "levelName": "MANIAC",
        "highScore": "0",
        "playCount": "0回",
        "detailsFlg": True,
        "chartId": "test001_04",
    },
    {
        "musicName": "テスト楽曲2",
        "levelName": "EXPERT",
        "highScore": "0",
        "playCount": "0回",
        "detailsFlg": True,
        "chartId": "test002_01",
    },
    ]
    assert testObj.searchMusic("かきく", "レベル1", "ジャンル1", True) == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    db_mock.assert_called_once()
    db_mock.assert_called_with("かきく", 456, "fghij")

def test_no_play_all_false(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=456)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="fghij")
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 1,
                    "mode": 1,
                    "highScore": 0,
                    "chartId": "test001_00",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 0,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 4,
                    "mode": 2,
                    "highScore": 0,
                    "chartId": "test001_04",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 0,
                    "clearedCount": 0,
                },
                {
                    "musicName": "テスト楽曲2",
                    "levelId": 2,
                    "mode": 3,
                    "highScore": 0,
                    "chartId": "test002_01",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 0,
                    "clearedCount": 0,
                }])
    assert testObj.searchMusic("かきく", "レベル1", "ジャンル1", False) == []
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    db_mock.assert_called_once()
    db_mock.assert_called_with("かきく", 456, "fghij")
