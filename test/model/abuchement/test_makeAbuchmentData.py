# coding:utf-8
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import abuchement


def setup_test():
    testObj = abuchement.abuchmentModel()
    return testObj


def test_empty():
    testObj = setup_test()
    assert testObj.makeAbuchmentData({}) == {}


def test_onedata():
    testObj = setup_test()
    input = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 12,
                    "clearedCount": 1,
                }]
    success = {
            "test001_01": {
                    "chartId": "test001_01",
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "perfectCount": 0,
                    "fullComboCount": 1,
                    "playCount": 12,
            }
        }
    assert testObj.makeAbuchmentData(input) == success


def test_two_chart():
    testObj = setup_test()
    input = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 12,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲2",
                    "levelId": 3,
                    "mode": 2,
                    "highScore": 7654321,
                    "chartId": "test002_01",
                    "fullComboCount": 3,
                    "perfectCount": 2,
                    "playCount": 1,
                    "clearedCount": 0,
                }]
    success = {
            "test001_01": {
                    "chartId": "test001_01",
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "perfectCount": 0,
                    "fullComboCount": 1,
                    "playCount": 12,
            },
            "test002_01": {
                    "chartId": "test002_01",
                    "musicName": "テスト楽曲2",
                    "levelId": 3,
                    "perfectCount": 2,
                    "fullComboCount": 3,
                    "playCount": 1,
            },
        }
    assert testObj.makeAbuchmentData(input) == success


def test_two_marge():
    testObj = setup_test()
    input = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001_01",
                    "fullComboCount": 1,
                    "perfectCount": 0,
                    "playCount": 12,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 2,
                    "highScore": 7654321,
                    "chartId": "test001_01",
                    "fullComboCount": 3,
                    "perfectCount": 2,
                    "playCount": 1,
                    "clearedCount": 0,
                }]
    success = {
            "test001_01": {
                    "chartId": "test001_01",
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "perfectCount": 2,
                    "fullComboCount": 4,
                    "playCount": 13,
            },
        }
    assert testObj.makeAbuchmentData(input) == success
