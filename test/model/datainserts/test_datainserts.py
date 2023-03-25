# coding:utf-8
import pytest
import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import datainserts
from util import util

def readFileStr(filename):
    f = open(os.path.join("test", "model", "datainserts", "data", filename), 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    return json.loads(data)


def test_empty(mocker):
    input_data = []
    history_mock = mocker.patch("db.highscorehistory.selectHighScoreHistoryByMode", return_values=[])
    insert_mock = mocker.patch("db.datainserts.dbinserts")
    datainserts.InsertMusic(input_data)
    history_mock.assert_not_called()
    insert_mock.assert_called_once()
    insert_mock.assert_called_with({},{},[],[],[],)


def test_three_data(mocker):
    datas = readFileStr("data_001.json")
    outputs = datas["outputs"]
    history_mock = mocker.patch("db.highscorehistory.selectHighScoreHistoryByMode", return_value=[])
    insert_mock = mocker.patch("db.datainserts.dbinserts")
    datainserts.InsertMusic(datas["inputData"])
    assert history_mock.call_count == 3
    history_mock.assert_has_calls([
            mocker.call("T0001_0", 10),
            mocker.call("T0002_1", 11),
            mocker.call("T0003_2", 12),
        ])
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(
        outputs["musicDist"],
        outputs["chartDist"],
        outputs["highScoreList"],
        outputs["highScoreHistoryList"],
        outputs["rankHistoryList"]
    )


def test_three_one_same_data(mocker):
    datas = readFileStr("data_002.json")
    outputs = datas["outputs"]
    history_mock = mocker.patch("db.highscorehistory.selectHighScoreHistoryByMode", side_effect=datas["DBData"])
    insert_mock = mocker.patch("db.datainserts.dbinserts")
    datainserts.InsertMusic(datas["inputData"])
    assert history_mock.call_count == 3
    history_mock.assert_has_calls([
            mocker.call("T0001_0", 10),
            mocker.call("T0002_1", 11),
            mocker.call("T0003_2", 12),
        ])
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(
        outputs["musicDist"],
        outputs["chartDist"],
        outputs["highScoreList"],
        outputs["highScoreHistoryList"],
        outputs["rankHistoryList"]
    )


def test_three_data_not_play_data(mocker):
    datas = readFileStr("data_003.json")
    outputs = datas["outputs"]
    history_mock = mocker.patch("db.highscorehistory.selectHighScoreHistoryByMode", return_value=[])
    insert_mock = mocker.patch("db.datainserts.dbinserts")
    datainserts.InsertMusic(datas["inputData"])
    assert history_mock.call_count == 2
    history_mock.assert_has_calls([
            mocker.call("T0001_0", 10),
            mocker.call("T0002_1", 11),
        ])
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(
        outputs["musicDist"],
        outputs["chartDist"],
        outputs["highScoreList"],
        outputs["highScoreHistoryList"],
        outputs["rankHistoryList"]
    )

def test_three_data_same_music(mocker):
    datas = readFileStr("data_004.json")
    outputs = datas["outputs"]
    history_mock = mocker.patch("db.highscorehistory.selectHighScoreHistoryByMode", return_value=[])
    insert_mock = mocker.patch("db.datainserts.dbinserts")
    datainserts.InsertMusic(datas["inputData"])
    assert history_mock.call_count == 3
    history_mock.assert_has_calls([
            mocker.call("T0001_0", 10),
            mocker.call("T0001_1", 11),
            mocker.call("T0003_2", 12),
        ])
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(
        outputs["musicDist"],
        outputs["chartDist"],
        outputs["highScoreList"],
        outputs["highScoreHistoryList"],
        outputs["rankHistoryList"]
    )
