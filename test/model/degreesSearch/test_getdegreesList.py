# coding:utf-8
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from model.degreesSearch import DegreesSearch

def setup_test():
    testObj = DegreesSearch()
    return testObj


def test_getdegreesList_none(mocker):
    testObj = setup_test()
    db_data = []
    db_mock = mocker.patch("db.degrees.selectDegrees", return_value=db_data)
    success = []
    assert testObj.getdegreesList("楽曲", "test000") == success
    db_mock.assert_called_once()
    db_mock.assert_called_with(category="Stage", searchMissionLabel="test000")


def test_getdegreesList_one(mocker):
    testObj = setup_test()
    db_data = [
        {
            "degreesId": "test001",
            "degreesName": "テスト1",
            "category": "Partner",
            "missionLabel": "条件1",
            "createdAt": "2022-01-10T20:09:01+00:00",
            "updatedAt": "2022-01-11T20:09:01+00:00",
        },
    ]
    db_mock = mocker.patch("db.degrees.selectDegrees", return_value=db_data)
    success = [
        {
            "degreesId": "test001",
            "degreesName": "テスト1",
            "categoryName": "パートナー",
            "missionLabel": "条件1",
            "getDate": "2022年1月11日 05:09:01",
        },
    ]
    assert testObj.getdegreesList("パートナー", "test001") == success
    db_mock.assert_called_once()
    db_mock.assert_called_with(category="Partner", searchMissionLabel="test001")


def test_getdegreesList_three(mocker):
    testObj = setup_test()
    db_data = [
        {
            "degreesId": "test001",
            "degreesName": "テスト1",
            "category": "System",
            "missionLabel": "条件1",
            "createdAt": "2022-01-10T20:09:01+00:00",
            "updatedAt": "2022-01-11T20:09:01+00:00",
        },
        {
            "degreesId": "test002",
            "degreesName": "テスト2",
            "category": "Event",
            "missionLabel": "条件2",
            "createdAt": "2022-02-10T20:09:01+00:00",
            "updatedAt": "2022-02-11T20:09:01+00:00",
        },
        {
            "degreesId": "test003",
            "degreesName": "テスト3",
            "category": "Ctest",
            "missionLabel": None,
            "createdAt": "2022-03-10T20:09:01+00:00",
            "updatedAt": "2022-03-11T20:09:01+00:00",
        },
    ]
    db_mock = mocker.patch("db.degrees.selectDegrees", return_value=db_data)
    success = [
        {
            "degreesId": "test001",
            "degreesName": "テスト1",
            "categoryName": "システム",
            "missionLabel": "条件1",
            "getDate": "2022年1月11日 05:09:01",
        },
        {
            "degreesId": "test002",
            "degreesName": "テスト2",
            "categoryName": "イベント",
            "missionLabel": "条件2",
            "getDate": "2022年2月11日 05:09:01",
        },
        {
            "degreesId": "test003",
            "degreesName": "テスト3",
            "categoryName": "Ctest",
            "missionLabel": "",
            "getDate": "2022年3月11日 05:09:01",
        },
    ]
    assert testObj.getdegreesList("", "") == success
    db_mock.assert_called_once()
    db_mock.assert_called_with(category="", searchMissionLabel="")
