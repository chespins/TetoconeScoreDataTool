# coding:utf-8
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from db import highscore


def test_selectHighScoreByChartId_none():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscore.TETOCONE_DB_NAME = test_file_name
    success = []
    assert highscore.selectHighScoreByChartId("test000_00") == success


def test_selectHighScoreByChartId_one():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscore.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "chartId": "test004_01",
                    "mode": 2,
                    "musicId": "test004",
                    "highScore": 7234567,
                    "maxCombo": 723,
                    "playCount": 72,
                    "clearedCount": 73,
                    "fullComboCount": 71,
                    "perfectCount": 7,
                    "updateTime": "2019-07-09T15:00:00+00:00",
                }]
    assert highscore.selectHighScoreByChartId("test004_01") == success


def test_selectHighScoreByChartId_two():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscore.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "chartId": "test002_01",
                    "mode": 1,
                    "musicId": "test002",
                    "highScore": 4234567,
                    "maxCombo": 423,
                    "playCount": 42,
                    "clearedCount": 43,
                    "fullComboCount": 41,
                    "perfectCount": 4,
                    "updateTime": "2019-04-09T15:00:00+00:00",
                },
                {
                    "chartId": "test002_01",
                    "mode": 2,
                    "musicId": "test002",
                    "highScore": 5234567,
                    "maxCombo": 523,
                    "playCount": 52,
                    "clearedCount": 53,
                    "fullComboCount": 51,
                    "perfectCount": 5,
                    "updateTime": "2019-05-09T15:00:00+00:00",
                },
            ]
    assert highscore.selectHighScoreByChartId("test002_01") == success


def test_selectHighScore_none():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscore.TETOCONE_DB_NAME = test_file_name
    success = []
    assert highscore.selectHighScore("あいうえお") == success


def test_selectHighScore_musicName_all():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscore.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "musicName": "テスト3",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 6234567,
                    "chartId": "test003_01",
                    "fullComboCount": 61,
                    "perfectCount": 6,
                    "playCount": 62,
                    "clearedCount": 63,
                    "maxCombo": 623,
                    "updateTime": "2019-06-09T15:00:00+00:00",
                    "genreId": "G003",
                }]
    assert highscore.selectHighScore("テスト3") == success


def test_selectHighScore_musicName_split():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscore.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "musicName": "テスト3",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 6234567,
                    "chartId": "test003_01",
                    "fullComboCount": 61,
                    "perfectCount": 6,
                    "playCount": 62,
                    "clearedCount": 63,
                    "maxCombo": 623,
                    "updateTime": "2019-06-09T15:00:00+00:00",
                    "genreId": "G003",
                }]
    assert highscore.selectHighScore("3") == success


def test_selectHighScore_genreId():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscore.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "musicName": "テスト4",
                    "levelId": 2,
                    "mode": 2,
                    "highScore": 7234567,
                    "chartId": "test004_01",
                    "fullComboCount": 71,
                    "perfectCount": 7,
                    "playCount": 72,
                    "clearedCount": 73,
                    "maxCombo": 723,
                    "updateTime": "2019-07-09T15:00:00+00:00",
                    "genreId": "G004",
                }]
    assert highscore.selectHighScore("", searchGenreId="G004") == success


def test_selectHighScore_levelId():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscore.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "musicName": "テスト1",
                    "levelId": 3,
                    "mode": 1,
                    "highScore": 3234567,
                    "chartId": "test001_02",
                    "fullComboCount": 31,
                    "perfectCount": 3,
                    "playCount": 32,
                    "clearedCount": 33,
                    "maxCombo": 323,
                    "updateTime": "2019-03-09T15:00:00+00:00",
                    "genreId": "G001",
                }]
    assert highscore.selectHighScore("", levelId=3) == success


def test_selectHighScore_all_param():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscore.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "musicName": "テスト2",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 4234567,
                    "chartId": "test002_01",
                    "fullComboCount": 41,
                    "perfectCount": 4,
                    "playCount": 42,
                    "clearedCount": 43,
                    "maxCombo": 423,
                    "updateTime": "2019-04-09T15:00:00+00:00",
                    "genreId": "G002",
            },
            {
                    "musicName": "テスト2",
                    "levelId": 2,
                    "mode": 2,
                    "highScore": 5234567,
                    "chartId": "test002_01",
                    "fullComboCount": 51,
                    "perfectCount": 5,
                    "playCount": 52,
                    "clearedCount": 53,
                    "maxCombo": 523,
                    "updateTime": "2019-05-09T15:00:00+00:00",
                    "genreId": "G002",
            },]
    assert highscore.selectHighScore("テスト", levelId=2, searchGenreId="G002") == success


def test_selectHighScore_param_empty():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscore.TETOCONE_DB_NAME = test_file_name
    success = [
            {
                    "musicName": "テスト1",
                    "levelId": 1,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_00",
                    "fullComboCount": 11,
                    "perfectCount": 1,
                    "playCount": 12,
                    "clearedCount": 13,
                    "maxCombo": 123,
                    "updateTime": "2019-01-09T15:00:00+00:00",
                    "genreId": "G001",
            },
            {
                    "musicName": "テスト1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 2234567,
                    "chartId": "test001_01",
                    "fullComboCount": 21,
                    "perfectCount": 2,
                    "playCount": 22,
                    "clearedCount": 23,
                    "maxCombo": 223,
                    "updateTime": "2019-02-09T15:00:00+00:00",
                    "genreId": "G001",
            },
            {
                    "musicName": "テスト1",
                    "levelId": 3,
                    "mode": 1,
                    "highScore": 3234567,
                    "chartId": "test001_02",
                    "fullComboCount": 31,
                    "perfectCount": 3,
                    "playCount": 32,
                    "clearedCount": 33,
                    "maxCombo": 323,
                    "updateTime": "2019-03-09T15:00:00+00:00",
                    "genreId": "G001",
            },
            {
                    "musicName": "テスト2",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 4234567,
                    "chartId": "test002_01",
                    "fullComboCount": 41,
                    "perfectCount": 4,
                    "playCount": 42,
                    "clearedCount": 43,
                    "maxCombo": 423,
                    "updateTime": "2019-04-09T15:00:00+00:00",
                    "genreId": "G002",
            },
            {
                    "musicName": "テスト2",
                    "levelId": 2,
                    "mode": 2,
                    "highScore": 5234567,
                    "chartId": "test002_01",
                    "fullComboCount": 51,
                    "perfectCount": 5,
                    "playCount": 52,
                    "clearedCount": 53,
                    "maxCombo": 523,
                    "updateTime": "2019-05-09T15:00:00+00:00",
                    "genreId": "G002",
            },
            {
                    "musicName": "テスト3",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 6234567,
                    "chartId": "test003_01",
                    "fullComboCount": 61,
                    "perfectCount": 6,
                    "playCount": 62,
                    "clearedCount": 63,
                    "maxCombo": 623,
                    "updateTime": "2019-06-09T15:00:00+00:00",
                    "genreId": "G003",
            },
            {
                    "musicName": "テスト4",
                    "levelId": 2,
                    "mode": 2,
                    "highScore": 7234567,
                    "chartId": "test004_01",
                    "fullComboCount": 71,
                    "perfectCount": 7,
                    "playCount": 72,
                    "clearedCount": 73,
                    "maxCombo": 723,
                    "updateTime": "2019-07-09T15:00:00+00:00",
                    "genreId": "G004",
            },
            ]
    assert highscore.selectHighScore("") == success
