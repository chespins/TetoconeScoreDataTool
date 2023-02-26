# coding:utf-8
import pytest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import rankingListGet

def setup_test():
    testObj = rankingListGet.RankingListGet()
    return testObj


def test_empty(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=0)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="")
    rank_mock = mocker.patch.object(testObj, "getMaxRank", return_value="SS")
    ranking_mock = mocker.patch.object(testObj, "makeRankingData", return_value={})
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[])
    assert testObj.searchMusic("レベル0", "ジャンル0") == []
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル0")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル0")
    rank_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_mock.assert_called_once()
    db_mock.assert_called_with("", 0, "")


def test_one(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=101)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="GTEST")
    rank_mock = mocker.patch.object(testObj, "getMaxRank", return_value="SS")
    ranking_mock = mocker.patch.object(testObj, "makeRankingData", return_value={
                    "rankingDisPlayedFlg": True,
                    "ranking": "1234位",
                    "getDate": "2023年1月8日 06:09:01 現在"
        })
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 1,
                    "clearedCount": 1,
                }])
    success = [{
            "musicName": "テスト楽曲1",
            "levelName": "EXPERT",
            "highScore": "1234567",
            "maxRank": "SS",
            "ranking": "1234位",
            "chartId": "test001",
        }
    ]
    assert testObj.searchMusic("レベル1", "ジャンル1") == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    rank_mock.assert_called_once()
    rank_mock.assert_called_with("test001")
    ranking_mock.assert_called_once()
    ranking_mock.assert_called_with("test001")
    db_mock.assert_called_once()
    db_mock.assert_called_with("", 101, "GTEST")


def test_two(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=101)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="GTEST")
    rank_mock = mocker.patch.object(testObj, "getMaxRank", side_effect=["SS", "AA+"])
    ranking_mock = mocker.patch.object(testObj, "makeRankingData", side_effect=[{
                    "rankingDisPlayedFlg": True,
                    "ranking": "1234位",
                    "getDate": "2023年1月8日 06:09:01 現在"
        },
        {
                    "rankingDisPlayedFlg": True,
                    "ranking": "4321位",
                    "getDate": "2023年1月9日 06:09:01 現在"
        }])
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 1,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 3,
                    "mode": 1,
                    "highScore": 2234567,
                    "chartId": "test001_02",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 3,
                    "clearedCount": 1,
                }])
    success = [{
            "musicName": "テスト楽曲1",
            "levelName": "EXPERT",
            "highScore": "1234567",
            "maxRank": "SS",
            "ranking": "1234位",
            "chartId": "test001_01",
        },
        {
            "musicName": "テスト楽曲1",
            "levelName": "ULTIMATE",
            "highScore": "2234567",
            "maxRank": "AA+",
            "ranking": "4321位",
            "chartId": "test001_02",
        }
    ]
    assert testObj.searchMusic("レベル1", "ジャンル1") == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    assert rank_mock.call_count == 2
    rank_mock.assert_has_calls(
        [mocker.call("test001_01"),
         mocker.call("test001_02")]
    )
    assert ranking_mock.call_count == 2
    ranking_mock.assert_has_calls(
        [mocker.call("test001_01"),
         mocker.call("test001_02")]
    )
    db_mock.assert_called_once()
    db_mock.assert_called_with("", 101, "GTEST")


def test_two_no_ranking(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=101)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="GTEST")
    rank_mock = mocker.patch.object(testObj, "getMaxRank", side_effect=["SS", "AA+"])
    ranking_mock = mocker.patch.object(testObj, "makeRankingData", side_effect=[{
                    "rankingDisPlayedFlg": True,
                    "ranking": "1234位",
                    "getDate": "2023年1月8日 06:09:01 現在"
        },
        {"rankingDisPlayedFlg": False}])
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 1,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 3,
                    "mode": 1,
                    "highScore": 2234567,
                    "chartId": "test001_02",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 3,
                    "clearedCount": 1,
                }])
    success = [{
            "musicName": "テスト楽曲1",
            "levelName": "EXPERT",
            "highScore": "1234567",
            "maxRank": "SS",
            "ranking": "1234位",
            "chartId": "test001_01",
        }
    ]
    assert testObj.searchMusic("レベル1", "ジャンル1") == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    rank_mock.assert_called_once()
    rank_mock.assert_called_with("test001_01")
    assert ranking_mock.call_count == 2
    ranking_mock.assert_has_calls(
        [mocker.call("test001_01"),
         mocker.call("test001_02")]
    )
    db_mock.assert_called_once()
    db_mock.assert_called_with("", 101, "GTEST")


def test_not_single(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=101)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="GTEST")
    rank_mock = mocker.patch.object(testObj, "getMaxRank", return_value="SS")
    ranking_mock = mocker.patch.object(testObj, "makeRankingData", return_value={})
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 3,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 1,
                    "clearedCount": 1,
                }])
    assert testObj.searchMusic("レベル1", "ジャンル1") == []
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    rank_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_mock.assert_called_once()
    db_mock.assert_called_with("", 101, "GTEST")
    

def test_not_play(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=101)
    genre_mock = mocker.patch("util.tetocone_util.getGenreIdByName", return_value="GTEST")
    rank_mock = mocker.patch.object(testObj, "getMaxRank", return_value="SS")
    ranking_mock = mocker.patch.object(testObj, "makeRankingData", return_value={})
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=[{
                    "musicName": "テスト楽曲1",
                    "levelId": 1,
                    "mode": 4,
                    "highScore": 0,
                    "chartId": "test001",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 0,
                    "clearedCount": 0,
                }])
    assert testObj.searchMusic("レベル1", "ジャンル1") == []
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    genre_mock.assert_called_once()
    genre_mock.assert_called_with("ジャンル1")
    rank_mock.assert_not_called()
    ranking_mock.assert_not_called()
    db_mock.assert_called_once()
    db_mock.assert_called_with("", 101, "GTEST")
