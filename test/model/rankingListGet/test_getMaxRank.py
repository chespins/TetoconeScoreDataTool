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


def test_getMaxRank_none(mocker):
    testObj = setup_test()
    mock = mocker.patch.object(testObj, "getRankData", return_value={})
    
    assert "---" == testObj.getMaxRank("test001")
    mock.assert_called_once()
    mock.assert_called_with("test001", {1})


def test_getMaxRank_one(mocker):
    testObj = setup_test()
    mock = mocker.patch.object(testObj, "getRankData", return_value={
                "SS": {
                    "rank": "SS",
                    "count": 5
                }})
    
    assert testObj.getMaxRank("test002") == "SS"
    mock.assert_called_once()
    mock.assert_called_with("test002", {1})


def test_getMaxRank_two(mocker):
    testObj = setup_test()
    mock = mocker.patch.object(testObj, "getRankData", return_value={
                "SSS": {
                    "rank": "SSS",
                    "count": 5
                },
                "SS": {
                    "rank": "SS",
                    "count": 2
                }})
    
    assert testObj.getMaxRank("test003") == "SS+"
    mock.assert_called_once()
    mock.assert_called_with("test003", {1})


def test_getMaxRank_three(mocker):
    testObj = setup_test()
    mock = mocker.patch.object(testObj, "getRankData", return_value={
                "AAA": {
                    "rank": "AAA",
                    "count": 5
                },
                "AA": {
                    "rank": "AA",
                    "count": 2
                },
                "BBB": {
                    "rank": "BBB",
                    "count": 2
                }})
    
    assert testObj.getMaxRank("test004") == "AA+"
    mock.assert_called_once()
    mock.assert_called_with("test004", {1})


def test_getMaxRank_BBB(mocker):
    testObj = setup_test()
    mock = mocker.patch.object(testObj, "getRankData", return_value={
                "BBB": {
                    "rank": "BBB",
                    "count": 1
                }})
    
    assert testObj.getMaxRank("test005") == "BB+"
    mock.assert_called_once()
    mock.assert_called_with("test005", {1})


def test_getMaxRank_Unexpected(mocker):
    testObj = setup_test()
    mock = mocker.patch.object(testObj, "getRankData", return_value={
                "ABC": {
                    "rank": "ABC",
                    "count": 1
                }})
    
    assert testObj.getMaxRank("test006") == "---"
    mock.assert_called_once()
    mock.assert_called_with("test006", {1})
