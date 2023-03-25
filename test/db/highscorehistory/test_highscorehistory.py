# coding:utf-8
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from db import highscorehistory


def test_selectHighScoreHistoryBychartId_none():
    befour_db_name = "test/db/highscorehistory/highScoreHistory_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscorehistory.TETOCONE_DB_NAME = test_file_name
    success = []
    assert highscorehistory.selectHighScoreHistoryBychartId("test000_00") == success


def test_selectHighScoreHistoryBychartId_one():
    befour_db_name = "test/db/highscorehistory/highScoreHistory_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscorehistory.TETOCONE_DB_NAME = test_file_name
    success = [
            {
                    "chartId": "test004_01",
                    "mode": 2,
                    "highScore": 7234567,
                    "maxCombo": 723,
                    "updateTime": "2019-07-09T15:00:00+00:00"
            }, 
        ]
    assert highscorehistory.selectHighScoreHistoryBychartId("test004_01") == success


def test_selectHighScoreHistoryBychartId_multi():
    befour_db_name = "test/db/highscorehistory/highScoreHistory_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscorehistory.TETOCONE_DB_NAME = test_file_name
    success = [
            {
                    "chartId": "test002_01",
                    "mode": 1,
                    "highScore": 9234567,
                    "maxCombo": 923,
                    "updateTime": "2019-09-09T15:00:00+00:00"
            },
            {
                    "chartId": "test002_01",
                    "mode": 1,
                    "highScore": 8234567,
                    "maxCombo": 823,
                    "updateTime": "2019-08-09T15:00:00+00:00"
            },
            {
                    "chartId": "test002_01",
                    "mode": 2,
                    "highScore": 5234567,
                    "maxCombo": 523,
                    "updateTime": "2019-05-09T15:00:00+00:00"
            },
            {
                    "chartId": "test002_01",
                    "mode": 1,
                    "highScore": 4234567,
                    "maxCombo": 423,
                    "updateTime": "2019-04-09T15:00:00+00:00"
            },
        ]
    assert highscorehistory.selectHighScoreHistoryBychartId("test002_01") == success


def test_selectHighScoreHistoryByMode_none():
    befour_db_name = "test/db/highscorehistory/highScoreHistory_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscorehistory.TETOCONE_DB_NAME = test_file_name
    success = []
    assert highscorehistory.selectHighScoreHistoryByMode("test002_01", 5) == success


def test_selectHighScoreHistoryByMode_one():
    befour_db_name = "test/db/highscorehistory/highScoreHistory_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscorehistory.TETOCONE_DB_NAME = test_file_name
    success = [
            {
                    "chartId": "test002_01",
                    "mode": 2,
                    "highScore": 5234567,
                    "maxCombo": 523,
                    "updateTime": "2019-05-09T15:00:00+00:00"
            },
        ]
    assert highscorehistory.selectHighScoreHistoryByMode("test002_01", 2) == success


def test_selectHighScoreHistoryByMode_multi():
    befour_db_name = "test/db/highscorehistory/highScoreHistory_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    highscorehistory.TETOCONE_DB_NAME = test_file_name
    success = [
            {
                    "chartId": "test002_01",
                    "mode": 1,
                    "highScore": 9234567,
                    "maxCombo": 923,
                    "updateTime": "2019-09-09T15:00:00+00:00"
            },
            {
                    "chartId": "test002_01",
                    "mode": 1,
                    "highScore": 8234567,
                    "maxCombo": 823,
                    "updateTime": "2019-08-09T15:00:00+00:00"
            },
            {
                    "chartId": "test002_01",
                    "mode": 1,
                    "highScore": 4234567,
                    "maxCombo": 423,
                    "updateTime": "2019-04-09T15:00:00+00:00"
            },
        ]
    assert highscorehistory.selectHighScoreHistoryByMode("test002_01", 1) == success
