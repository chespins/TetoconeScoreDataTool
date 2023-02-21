# coding:utf-8
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from model import basemodel

def setup_test():
    testObj = basemodel.BaseModel()
    return testObj

def test_makeLavalNamePulldown():
    success = [
        "",
        "STANDARD",
        "EXPERT",
        "ULTIMATE",
        "MANIAC",
        "CONNECT",
    ]
    testObj = setup_test()
    assert success == testObj.makeLavalNamePulldown()


def test_getMusicName(mocker):
    mock = mocker.patch("db.chartconstitution.selectChartByChartId", return_value=[{
                    "chartId": "test001",
                    "musicId": "test01",
                    "levelId": 1,
                    "musicName": "テスト楽曲名1",
                    "genreId": "G000",
                }])
    success = {
                "musicName": "テスト楽曲名1",
                "levelName": "STANDARD",
                "genreName": "アニメ・ポップス",
                "levelColor": [0.212, 0.51, 0.894, 1],
            }
    testObj = setup_test()
    assert success == testObj.getMusicName("test001")
    mock.assert_called_once()
    mock.assert_called_with("test001")


def test_getMusicName2(mocker):
    mock = mocker.patch("db.chartconstitution.selectChartByChartId", return_value=[{
                    "chartId": "test002",
                    "musicId": "test02",
                    "levelId": 3,
                    "musicName": "テスト楽曲名2",
                    "genreId": "G003",
                }])
    success = {
                "musicName": "テスト楽曲名2",
                "levelName": "ULTIMATE",
                "genreName": "ゲーム",
                "levelColor": [0.612, 0.239, 0.8, 1],
            }
    testObj = setup_test()
    assert success == testObj.getMusicName("test002")
    mock.assert_called_once()
    mock.assert_called_with("test002")


def test_makeGenreNamePulldown():
    success = [
        "",
        "アニメ・ポップス",
        "バーチャル",
        "東方アレンジ",
        "ゲーム",
        "オリジナル",
        "バラエティー",
    ]
    testObj = setup_test()
    assert success == testObj.makeGenreNamePulldown()


def test_makeModeNamePulldown():
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
    testObj = setup_test()
    assert success == testObj.makeModeNamePulldown()


def test_isSinglePlay_true():
    testObj = setup_test()
    assert testObj.isSinglePlay("シングルプレイ")


def test_isSinglePlay_false_all():
    testObj = setup_test()
    assert not testObj.isSinglePlay("全て")


def test_isSinglePlay_false_battle():
    testObj = setup_test()
    assert not testObj.isSinglePlay("協力プレイ(2人)")  

def test_makeRankingData_false_none(mocker):
    mock = mocker.patch("db.ranking.selectRankingForChartId", return_value=[])
    success = {
                    "rankingDisPlayedFlg": False,
        }
    testObj = setup_test()
    assert success == testObj.makeRankingData("test001")
    mock.assert_called_once()
    mock.assert_called_with("test001")

def test_makeRankingData_false_one(mocker):
    mock = mocker.patch("db.ranking.selectRankingForChartId", return_value=[{
                "chartId": "test002",
                "ranking": "789",
                "getDate": "2023-01-07T21:09:01+00:00",
            }])
    success = {
                    "rankingDisPlayedFlg": True,
                    "ranking": "789位",
                    "getDate": "2023年1月8日 06:09:01 現在"
        }
    testObj = setup_test()
    assert success == testObj.makeRankingData("test002")
    mock.assert_called_once()
    mock.assert_called_with("test002")

def test_makeRankingData_false_two(mocker):
    mock = mocker.patch("db.ranking.selectRankingForChartId", return_value=[{
                "chartId": "test003",
                "ranking": "123",
                "getDate": "2023-01-07T21:09:01+00:00",
            },
            {
                "chartId": "test003",
                "ranking": "345",
                "getDate": "2023-01-08T21:09:01+00:00",
            }])
    success = {
                    "rankingDisPlayedFlg": False,
        }
    testObj = setup_test()
    assert success == testObj.makeRankingData("test003")
    mock.assert_called_once()
    mock.assert_called_with("test003")


def test_getRankData(mocker):
    mock = mocker.patch("db.rankhistory.selectChartByChartIdMode", return_value=[{
                    "chartId": "Test001",
                    "mode": 1,
                    "rank": "SS",
                    "count": 4
                }])
    success = {"SS": {
                    "rank": "SS",
                    "count": 4
                }}
    testObj = setup_test()
    assert success == testObj.getRankData("Test001", (1))
    mock.assert_called_once()
    mock.assert_called_with("Test001", (1))


def test_getRankData2(mocker):
    mock = mocker.patch("db.rankhistory.selectChartByChartIdMode", return_value=[{
                    "chartId": "Test002",
                    "mode": 1,
                    "rank": "SS",
                    "count": 4
                },
                {
                    "chartId": "Test002",
                    "mode": 2,
                    "rank": "SS",
                    "count": 1
                },
                {
                    "chartId": "Test002",
                    "mode": 3,
                    "rank": "S",
                    "count": 1
                }])
    success = {"SS": {
                    "rank": "SS",
                    "count": 5
                },
                "S": {
                    "rank": "S",
                    "count": 1
                }}
    testObj = setup_test()
    assert success == testObj.getRankData("Test002", (1,2,3,4,5,6))
    mock.assert_called_once()
    mock.assert_called_with("Test002", (1,2,3,4,5,6))

def test_getSinglePlayName():
    testObj = setup_test()
    assert "シングルプレイ" == testObj.getSinglePlayName() 
