# coding:utf-8
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import abuchement


def setup_test():
    testObj = abuchement.abuchmentModel()
    return testObj


def test_empty(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=0)
    fullcombo_return = {"fullcombo_mock": "1"}
    fullcombo_mock = mocker.patch.object(testObj, "fullComboAbuchment", return_value=fullcombo_return)
    parfect_return = {"parfect_mock": "1"}
    parfect_mock = mocker.patch.object(testObj, "parfectAbuchment", return_value=parfect_return)
    makeData_mock = mocker.patch.object(testObj, "makeAbuchmentData", return_value={})
    db_return = ["DBreturns"]
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=db_return)
    assert testObj.searchMusic("フルコンボ", "レベル0", True) == []
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル0")
    db_mock.assert_called_once()
    db_mock.assert_called_with("", 0)
    fullcombo_mock.assert_called_once()
    fullcombo_mock.assert_called_with(db_return, True)
    parfect_mock.assert_not_called()
    makeData_mock.assert_called_once()
    makeData_mock.assert_called_with(fullcombo_return)


def test_one_fullcombo(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=0)
    fullcombo_return = {"fullcombo_mock": "1"}
    fullcombo_mock = mocker.patch.object(testObj, "fullComboAbuchment", return_value=fullcombo_return)
    parfect_return = {"parfect_mock": "1"}
    parfect_mock = mocker.patch.object(testObj, "parfectAbuchment", return_value=parfect_return)
    makeData_mock = mocker.patch.object(testObj, "makeAbuchmentData", return_value={
            "test001_01": {
                    "chartId": "test001_01",
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "perfectCount": 2,
                    "fullComboCount": 4,
                    "playCount": 13,
            },
        })
    db_return = ["DBreturns"]
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=db_return)
    success = [
        {
            "musicName": "テスト楽曲1",
            "levelName": "EXPERT",
            "playCount": "13回",
            "perfectCount": "2回",
            "fullComboCount": "4回",
            "detailsFlg": False,
            "chartId": "test001_01",
        }
    ]
    assert testObj.searchMusic("フルコンボ", "レベル0", False) == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル0")
    db_mock.assert_called_once()
    db_mock.assert_called_with("", 0)
    fullcombo_mock.assert_called_once()
    fullcombo_mock.assert_called_with(db_return, False)
    parfect_mock.assert_not_called()
    makeData_mock.assert_called_once()
    makeData_mock.assert_called_with(fullcombo_return)


def test_one_parfect(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=0)
    fullcombo_return = {"fullcombo_mock": "1"}
    fullcombo_mock = mocker.patch.object(testObj, "fullComboAbuchment", return_value=fullcombo_return)
    parfect_return = {"parfect_mock": "1"}
    parfect_mock = mocker.patch.object(testObj, "parfectAbuchment", return_value=parfect_return)
    makeData_mock = mocker.patch.object(testObj, "makeAbuchmentData", return_value={
            "test001_11": {
                    "chartId": "test001_11",
                    "musicName": "テスト楽曲2",
                    "levelId": 1,
                    "perfectCount": 1,
                    "fullComboCount": 2,
                    "playCount": 3,
            },
        })
    db_return = ["DBreturns"]
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=db_return)
    success = [
        {
            "musicName": "テスト楽曲2",
            "levelName": "STANDARD",
            "playCount": "3回",
            "perfectCount": "1回",
            "fullComboCount": "2回",
            "detailsFlg": False,
            "chartId": "test001_11",
        }
    ]
    assert testObj.searchMusic("パーフェクト", "レベル1", False) == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    db_mock.assert_called_once()
    db_mock.assert_called_with("", 0)
    fullcombo_mock.assert_not_called()
    parfect_mock.assert_called_once()
    parfect_mock.assert_called_with(db_return, False)
    makeData_mock.assert_called_once()
    makeData_mock.assert_called_with(parfect_return)

    
def test_multi_parfect(mocker):
    testObj = setup_test()
    level_mock = mocker.patch("util.tetocone_util.getLevelIdByName", return_value=0)
    fullcombo_return = {"fullcombo_mock": "1"}
    fullcombo_mock = mocker.patch.object(testObj, "fullComboAbuchment", return_value=fullcombo_return)
    parfect_return = {"parfect_mock": "1"}
    parfect_mock = mocker.patch.object(testObj, "parfectAbuchment", return_value=parfect_return)
    makeData_mock = mocker.patch.object(testObj, "makeAbuchmentData", return_value={
            "test001_21": {
                    "chartId": "test001_21",
                    "musicName": "テスト楽曲1",
                    "levelId": 3,
                    "perfectCount": 1,
                    "fullComboCount": 2,
                    "playCount": 3,
            },
            "test002_21": {
                    "chartId": "test002_21",
                    "musicName": "テスト楽曲2",
                    "levelId": 4,
                    "perfectCount": 2,
                    "fullComboCount": 3,
                    "playCount": 4,
            },
            "test003_21": {
                    "chartId": "test003_21",
                    "musicName": "テスト楽曲3",
                    "levelId": 5,
                    "perfectCount": 0,
                    "fullComboCount": 0,
                    "playCount": 0,
            },
        })
    db_return = ["DBreturns"]
    db_mock = mocker.patch("db.highscore.selectHighScore", return_value=db_return)
    success = [
        {
            "musicName": "テスト楽曲1",
            "levelName": "ULTIMATE",
            "playCount": "3回",
            "perfectCount": "1回",
            "fullComboCount": "2回",
            "detailsFlg": False,
            "chartId": "test001_21",
        },
        {
            "musicName": "テスト楽曲2",
            "levelName": "MANIAC",
            "playCount": "4回",
            "perfectCount": "2回",
            "fullComboCount": "3回",
            "detailsFlg": False,
            "chartId": "test002_21",
        },
        {
            "musicName": "テスト楽曲3",
            "levelName": "CONNECT",
            "playCount": "0回",
            "perfectCount": "0回",
            "fullComboCount": "0回",
            "detailsFlg": True,
            "chartId": "test003_21",
        },
    ]
    assert testObj.searchMusic("パーフェクト", "レベル1", False) == success
    level_mock.assert_called_once()
    level_mock.assert_called_with("レベル1")
    db_mock.assert_called_once()
    db_mock.assert_called_with("", 0)
    fullcombo_mock.assert_not_called()
    parfect_mock.assert_called_once()
    parfect_mock.assert_called_with(db_return, False)
    makeData_mock.assert_called_once()
    makeData_mock.assert_called_with(parfect_return)
