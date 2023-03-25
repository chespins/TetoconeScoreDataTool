# coding:utf-8
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import highscoredetails


def setup_test_obj():
    testObj = highscoredetails.highScoreData()
    return testObj


def setup_test(highscore, maxCombo, playCount, clearedCount, fullComboCount, perfectCount, updateTime):
    testObj = setup_test_obj()
    testObj.highscore = highscore
    testObj.maxCombo = maxCombo
    testObj.playCount = playCount
    testObj.clearedCount = clearedCount
    testObj.fullComboCount = fullComboCount
    testObj.perfectCount = perfectCount
    testObj.updateTime = updateTime
    return testObj


def test_init():
    testObj = setup_test_obj()
    assert testObj.highscore == 0
    assert testObj.maxCombo == 0
    assert testObj.playCount == 0
    assert testObj.clearedCount == 0
    assert testObj.fullComboCount == 0
    assert testObj.perfectCount == 0
    assert testObj.updateTime == "2000-01-01T00:00:00+00:00"


def test_setHighScore_low():
    testObj = setup_test(1000, 111, 12, 11, 3, 1, "2020-11-21T12:11:20+00:00")
    input_param = {
                    "chartId": "test001_01",
                    "mode": 1,
                    "musicId": "test001",
                    "highScore": 999,
                    "maxCombo": 115,
                    "playCount": 2,
                    "clearedCount": 2,
                    "fullComboCount": 2,
                    "perfectCount": 2,
                    "updateTime": "2020-10-21T12:11:20+00:00"
                }
    testObj.setHighScore(input_param)
    assert testObj.highscore == 1000
    assert testObj.maxCombo == 111
    assert testObj.playCount == 14
    assert testObj.clearedCount == 13
    assert testObj.fullComboCount == 5
    assert testObj.perfectCount == 3
    assert testObj.updateTime == "2020-11-21T12:11:20+00:00"


def test_setHighScore_high():
    testObj = setup_test(1000, 111, 5, 4, 3, 2, "2020-11-21T12:11:20+00:00")
    input_param = {
                    "chartId": "test001_01",
                    "mode": 1,
                    "musicId": "test001",
                    "highScore": 1001,
                    "maxCombo": 115,
                    "playCount": 9,
                    "clearedCount": 8,
                    "fullComboCount": 7,
                    "perfectCount": 6,
                    "updateTime": "2020-10-21T12:11:20+00:00"
                }
    testObj.setHighScore(input_param)
    assert testObj.highscore == 1001
    assert testObj.maxCombo == 115
    assert testObj.playCount == 14
    assert testObj.clearedCount == 12
    assert testObj.fullComboCount == 10
    assert testObj.perfectCount == 8
    assert testObj.updateTime == "2020-11-21T12:11:20+00:00"


def test_setHighScore_new():
    testObj = setup_test(1000, 111, 12, 11, 3, 1, "2020-11-21T12:11:20+00:00")
    input_param = {
                    "chartId": "test001_01",
                    "mode": 1,
                    "musicId": "test001",
                    "highScore": 999,
                    "maxCombo": 115,
                    "playCount": 2,
                    "clearedCount": 2,
                    "fullComboCount": 2,
                    "perfectCount": 2,
                    "updateTime": "2020-12-21T12:11:20+00:00"
                }
    testObj.setHighScore(input_param)
    assert testObj.highscore == 1000
    assert testObj.maxCombo == 111
    assert testObj.playCount == 14
    assert testObj.clearedCount == 13
    assert testObj.fullComboCount == 5
    assert testObj.perfectCount == 3
    assert testObj.updateTime == "2020-12-21T12:11:20+00:00"


def test_makeViewData():
    testObj = setup_test(1000, 111, 12, 11, 3, 1, "2020-11-21T12:11:20+00:00")
    success = {
                "highScore": "1000",
                "maxCombo":  "111",
                "playCount": "12回",
                "clearedCount": "11回",
                "fullComboCount": "3回",
                "perfectCount": "1回",
                "lastUpdateTime": "2020年11月21日 21:11:20"
            }
    assert testObj.makeViewData() == success
