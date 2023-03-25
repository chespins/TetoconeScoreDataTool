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
    input_list = []
    assert testObj.filterScoreData(input_list, False, "fullComboCount") == []


def test_one_data_false():
    testObj = setup_test()
    input_list = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                }]
    success = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                }]
    assert testObj.filterScoreData(input_list, False, "fullComboCount") == success


def test_one_data_perfect():
    testObj = setup_test()
    input_list = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                }]
    success = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                }]
    assert testObj.filterScoreData(input_list, False, "perfectCount") == success


def test_one_data_unmatch_false():
    testObj = setup_test()
    input_list = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 1,
                    "clearedCount": 1,
                }]
    assert testObj.filterScoreData(input_list, False, "fullComboCount") == []


def test_one_data_true():
    testObj = setup_test()
    input_list = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 1,
                    "clearedCount": 1,
                }]
    success = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 0,
                    "perfectCount": 0,
                    "playCount": 1,
                    "clearedCount": 1,
                }]
    assert testObj.filterScoreData(input_list, True, "fullComboCount") == success


def test_one_unmatch_data_true():
    testObj = setup_test()
    input_list = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                }]
    assert testObj.filterScoreData(input_list, True, "fullComboCount") == []


def test_three_mode_data_false():
    testObj = setup_test()
    input_list = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 2,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 0,
                    "perfectCount": 3,
                    "playCount": 5,
                    "clearedCount": 2,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 3,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 2,
                    "perfectCount": 0,
                    "playCount": 10,
                    "clearedCount": 10,
                }]
    success = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 2,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 0,
                    "perfectCount": 3,
                    "playCount": 5,
                    "clearedCount": 2,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 3,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 2,
                    "perfectCount": 0,
                    "playCount": 10,
                    "clearedCount": 10,
                }]
    assert testObj.filterScoreData(input_list, False, "fullComboCount") == success


def test_three_mode_data_true():
    testObj = setup_test()
    input_list = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 2,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 0,
                    "perfectCount": 3,
                    "playCount": 5,
                    "clearedCount": 2,
                },
                {
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 3,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 2,
                    "perfectCount": 0,
                    "playCount": 10,
                    "clearedCount": 10,
                }]
    assert testObj.filterScoreData(input_list, True, "fullComboCount") == []


def test_three_music_data_false():
    testObj = setup_test()
    input_list = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲2",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234568,
                    "chartId": "test002",
                    "fullComboCount": 0,
                    "perfectCount": 1,
                    "playCount": 5,
                    "clearedCount": 2,
                },
                {
                    "musicName": "テスト楽曲3",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234569,
                    "chartId": "test003",
                    "fullComboCount": 2,
                    "perfectCount": 0,
                    "playCount": 10,
                    "clearedCount": 10,
                }]
    assert testObj.filterScoreData(input_list, True, "fullComboCount") == []


def test_three_music_data_false():
    testObj = setup_test()
    input_list = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲2",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234568,
                    "chartId": "test002",
                    "fullComboCount": 0,
                    "perfectCount": 1,
                    "playCount": 5,
                    "clearedCount": 2,
                },
                {
                    "musicName": "テスト楽曲3",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234569,
                    "chartId": "test003",
                    "fullComboCount": 2,
                    "perfectCount": 0,
                    "playCount": 10,
                    "clearedCount": 10,
                }]
    success = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲3",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234569,
                    "chartId": "test003",
                    "fullComboCount": 2,
                    "perfectCount": 0,
                    "playCount": 10,
                    "clearedCount": 10,
                }]
    assert testObj.filterScoreData(input_list, False, "fullComboCount") == success

def test_three_music_data_true():
    testObj = setup_test()
    input_list = [{
                    "musicName": "テスト楽曲1",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234567,
                    "chartId": "test001",
                    "fullComboCount": 1,
                    "perfectCount": 1,
                    "playCount": 1,
                    "clearedCount": 1,
                },
                {
                    "musicName": "テスト楽曲2",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234568,
                    "chartId": "test002",
                    "fullComboCount": 0,
                    "perfectCount": 1,
                    "playCount": 5,
                    "clearedCount": 2,
                },
                {
                    "musicName": "テスト楽曲3",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234569,
                    "chartId": "test003",
                    "fullComboCount": 2,
                    "perfectCount": 0,
                    "playCount": 10,
                    "clearedCount": 10,
                }]
    success = [{
                    "musicName": "テスト楽曲2",
                    "levelId": 2,
                    "mode": 1,
                    "highScore": 1234568,
                    "chartId": "test002",
                    "fullComboCount": 0,
                    "perfectCount": 1,
                    "playCount": 5,
                    "clearedCount": 2,
                }]
    assert testObj.filterScoreData(input_list, True, "fullComboCount") == success
