# coding:utf-8
import pytest
import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model import datainserts


def readFileStr(filename):
    f = open(os.path.join("test", "model", "datainserts", "data", filename), 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    return json.loads(data)


def test_empty(mocker):
    input_data = {}
    insert_mock = mocker.patch("db.degrees.insertDegrees")
    datainserts.insertDegrees(input_data)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with([])


def test_one_data(mocker):
    test_data = readFileStr("degrees_001.json")
    input_data = test_data["inputData"]
    insert_mock = mocker.patch("db.degrees.insertDegrees")
    datainserts.insertDegrees(input_data)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(test_data["outputData"])


def test_three_data(mocker):
    test_data = readFileStr("degrees_002.json")
    input_data = test_data["inputData"]
    insert_mock = mocker.patch("db.degrees.insertDegrees")
    datainserts.insertDegrees(input_data)
    insert_mock.assert_called_once()
    insert_mock.assert_called_with(test_data["outputData"])
