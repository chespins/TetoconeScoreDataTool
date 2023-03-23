# coding:utf-8
import json
import sys
import os
import filecmp


sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from db import datainserts


def readFileStr(filename):
    f = open(os.path.join("test", "db", "datainserts", "data", filename), 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    return json.loads(data)


def test_emptydb_insert():
    befour_db_name = "test/db/datainserts/data/empty.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    datainserts.TETOCONE_DB_NAME = test_file_name
    inputData = readFileStr("data_001.json")
    datainserts.dbinserts(
            inputData["musicDist"],
            inputData["chartDist"],
            inputData["highScoreList"],
            inputData["highScoreHistoryList"],
            inputData["rankHistoryList"]
        )
    assert filecmp.cmp(test_file_name, "test/db/datainserts/result/emptydb_insert.db")


def test_add_data_insert():
    befour_db_name = "test/db/datainserts/data/data_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    datainserts.TETOCONE_DB_NAME = test_file_name
    inputData = readFileStr("data_002.json")
    datainserts.dbinserts(
            inputData["musicDist"],
            inputData["chartDist"],
            inputData["highScoreList"],
            inputData["highScoreHistoryList"],
            inputData["rankHistoryList"]
        )
    assert filecmp.cmp(test_file_name, "test/db/datainserts/result/add_data_insert.db")


def test_washing_data():
    befour_db_name = "test/db/datainserts/data/data_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    datainserts.TETOCONE_DB_NAME = test_file_name
    inputData = readFileStr("data_003.json")
    datainserts.dbinserts(
            inputData["musicDist"],
            inputData["chartDist"],
            inputData["highScoreList"],
            inputData["highScoreHistoryList"],
            inputData["rankHistoryList"]
        )
    assert filecmp.cmp(test_file_name, "test/db/datainserts/result/washing_data.db")


def test_highScoreHistory_empty():
    befour_db_name = "test/db/datainserts/data/data_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    datainserts.TETOCONE_DB_NAME = test_file_name
    inputData = readFileStr("data_004.json")
    datainserts.dbinserts(
            inputData["musicDist"],
            inputData["chartDist"],
            inputData["highScoreList"],
            inputData["highScoreHistoryList"],
            inputData["rankHistoryList"]
        )
    assert filecmp.cmp(test_file_name, "test/db/datainserts/result/highScoreHistory_empty.db")
