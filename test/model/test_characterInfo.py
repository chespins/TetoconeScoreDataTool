# coding:utf-8
import sys
import os
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from model import characterInfo

def setup_test(mocker):
    dbData =  [
        {
            "characterId": "TEST001",
            "characterName": "テストキャラ1",
            "introduction": "テスト1\nテスト1\nテスト1",
            "dearnessRank": 1,
            "dearnessPoint": 1234,
            "isUsed": True,
            "sortIndex": 10,
            "costumeId": "COS_TEST_001",
            "collaboration": False,
            "dearnessRanking": 100,
            "rankingGetDate": "2022-11-11T04:51:57+00:00",
            "updatedAt": "2023-02-12T05:33:21+00:00",
        },
        {
            "characterId": "TEST002",
            "characterName": "テストキャラ2",
            "introduction": "テスト2\nテスト2\nテスト2",
            "dearnessRank": 2,
            "dearnessPoint": 2234,
            "isUsed": True,
            "sortIndex": 11,
            "costumeId": "COS_TEST_002",
            "collaboration": True,
            "dearnessRanking": 200,
            "rankingGetDate": "2022-11-12T04:51:57+00:00",
            "updatedAt": "2023-03-12T05:33:21+00:00",
        },
        {
            "characterId": "TEST003",
            "characterName": "テストキャラ3",
            "introduction": "テスト3\nテスト3\nテスト3",
            "dearnessRank": 3,
            "dearnessPoint": 3234,
            "isUsed": True,
            "sortIndex": 12,
            "costumeId": "COS_TEST_003",
            "collaboration": False,
            "dearnessRanking": 300,
            "rankingGetDate": "2022-11-13T04:51:57+00:00",
            "updatedAt": "2023-04-12T05:33:21+00:00",
        },
    ]
    mocker.patch("db.character.selectCharacter", return_value=dbData)
    testObj = characterInfo.CharacterInfoModel()
    testObj.refreshCharacterData()
    return testObj


def test_init():
    testObj = characterInfo.CharacterInfoModel()
    assert testObj.characterInfoDist == {}


def test_reflash(mocker):
    success = {
        "TEST001": {
            "characterId": "TEST001",
            "characterName": "テストキャラ1",
            "introduction": "テスト1\nテスト1\nテスト1",
            "dearnessRank": 1,
            "dearnessPoint": 1234,
            "isUsed": True,
            "sortIndex": 10,
            "costumeId": "COS_TEST_001",
            "collaboration": False,
            "dearnessRanking": 100,
            "rankingGetDate": "2022-11-11T04:51:57+00:00",
            "updatedAt": "2023-02-12T05:33:21+00:00",
        },
        "TEST002": {
            "characterId": "TEST002",
            "characterName": "テストキャラ2",
            "introduction": "テスト2\nテスト2\nテスト2",
            "dearnessRank": 2,
            "dearnessPoint": 2234,
            "isUsed": True,
            "sortIndex": 11,
            "costumeId": "COS_TEST_002",
            "collaboration": True,
            "dearnessRanking": 200,
            "rankingGetDate": "2022-11-12T04:51:57+00:00",
            "updatedAt": "2023-03-12T05:33:21+00:00",
        },
        "TEST003": {
            "characterId": "TEST003",
            "characterName": "テストキャラ3",
            "introduction": "テスト3\nテスト3\nテスト3",
            "dearnessRank": 3,
            "dearnessPoint": 3234,
            "isUsed": True,
            "sortIndex": 12,
            "costumeId": "COS_TEST_003",
            "collaboration": False,
            "dearnessRanking": 300,
            "rankingGetDate": "2022-11-13T04:51:57+00:00",
            "updatedAt": "2023-04-12T05:33:21+00:00",
        },
    }
    dbData =  [
        {
            "characterId": "TEST001",
            "characterName": "テストキャラ1",
            "introduction": "テスト1\nテスト1\nテスト1",
            "dearnessRank": 1,
            "dearnessPoint": 1234,
            "isUsed": True,
            "sortIndex": 10,
            "costumeId": "COS_TEST_001",
            "collaboration": False,
            "dearnessRanking": 100,
            "rankingGetDate": "2022-11-11T04:51:57+00:00",
            "updatedAt": "2023-02-12T05:33:21+00:00",
        },
        {
            "characterId": "TEST002",
            "characterName": "テストキャラ2",
            "introduction": "テスト2\nテスト2\nテスト2",
            "dearnessRank": 2,
            "dearnessPoint": 2234,
            "isUsed": True,
            "sortIndex": 11,
            "costumeId": "COS_TEST_002",
            "collaboration": True,
            "dearnessRanking": 200,
            "rankingGetDate": "2022-11-12T04:51:57+00:00",
            "updatedAt": "2023-03-12T05:33:21+00:00",
        },
        {
            "characterId": "TEST003",
            "characterName": "テストキャラ3",
            "introduction": "テスト3\nテスト3\nテスト3",
            "dearnessRank": 3,
            "dearnessPoint": 3234,
            "isUsed": True,
            "sortIndex": 12,
            "costumeId": "COS_TEST_003",
            "collaboration": False,
            "dearnessRanking": 300,
            "rankingGetDate": "2022-11-13T04:51:57+00:00",
            "updatedAt": "2023-04-12T05:33:21+00:00",
        },
    ]
    db_mock = mocker.patch("db.character.selectCharacter", return_value=dbData)
    testObj = characterInfo.CharacterInfoModel()
    testObj.refreshCharacterData()
    assert testObj.characterInfoDist == success
    db_mock.assert_called_once()
    db_mock.assert_called_with()


def test_isEmptyCharacterInfoList_false(mocker):
    testObj = setup_test(mocker)
    testObj.characterInfoDist = {}
    assert not testObj.isEmptyCharacterInfoList()


def test_isEmptyCharacterInfoList_true(mocker):
    testObj = setup_test(mocker)
    assert testObj.isEmptyCharacterInfoList()


def test_getCharacterNameList(mocker):
    testObj = setup_test(mocker)
    success = [
        {
            "characterId": "TEST001",
            "characterName": "テストキャラ1",
        },
        {
            "characterId": "TEST002",
            "characterName": "テストキャラ2",
        },
        {
            "characterId": "TEST003",
            "characterName": "テストキャラ3",
        },
    ]
    assert testObj.getCharacterNameList() == success


def test_getCharacterNameList_empty(mocker):
    testObj = setup_test(mocker)
    testObj.characterInfoDist = {}
    success = []
    assert testObj.getCharacterNameList() == success


def test_getCharacterInfo(mocker):
    testObj = setup_test(mocker)
    info_return = {
        "test001": "テスト1",
        "test002": "テスト2",
    }
    info_mock = mocker.patch.object(testObj, "makeDisplayedData", return_value=info_return)
    pre_mock = mocker.patch.object(testObj, "preDisplayedCharacterInfo")
    assert testObj.getCharacterInfo("TEST002") == info_return
    info_mock.assert_called_once()
    info_param = {
            "characterId": "TEST002",
            "characterName": "テストキャラ2",
            "introduction": "テスト2\nテスト2\nテスト2",
            "dearnessRank": 2,
            "dearnessPoint": 2234,
            "isUsed": True,
            "sortIndex": 11,
            "costumeId": "COS_TEST_002",
            "collaboration": True,
            "dearnessRanking": 200,
            "rankingGetDate": "2022-11-12T04:51:57+00:00",
            "updatedAt": "2023-03-12T05:33:21+00:00",
        }
    info_mock.assert_called_with(info_param)
    pre_mock.assert_not_called()


def test_getCharacterInfo_none(mocker):
    testObj = setup_test(mocker)
    info_return = {
        "test003": "テスト1",
        "test004": "テスト2",
    }
    info_mock = mocker.patch.object(testObj, "makeDisplayedData")
    pre_mock = mocker.patch.object(testObj, "preDisplayedCharacterInfo", return_value=info_return)
    assert testObj.getCharacterInfo("") == info_return
    info_mock.assert_not_called()
    pre_mock.assert_called_once()
    pre_mock.assert_called_with()


def test_preDisplayedCharacterInfo(mocker):
    testObj = setup_test(mocker)
    info_return = {
        "test005": "テスト1",
        "test006": "テスト2",
    }
    info_mock = mocker.patch.object(testObj, "makeDisplayedData", return_value=info_return)
    list_return = [
        {"characterId": "TEST001"},
        {"characterId": "TEST002"},
        {"characterId": "TEST003"},
    ]
    list_mock = mocker.patch.object(testObj, "getCharacterNameList", return_value=list_return)
    assert testObj.preDisplayedCharacterInfo() == info_return
    info_mock.assert_called_once()
    info_param = {
            "characterId": "TEST001",
            "characterName": "テストキャラ1",
            "introduction": "テスト1\nテスト1\nテスト1",
            "dearnessRank": 1,
            "dearnessPoint": 1234,
            "isUsed": True,
            "sortIndex": 10,
            "costumeId": "COS_TEST_001",
            "collaboration": False,
            "dearnessRanking": 100,
            "rankingGetDate": "2022-11-11T04:51:57+00:00",
            "updatedAt": "2023-02-12T05:33:21+00:00",
        }
    info_mock.assert_called_with(info_param)
    list_mock.assert_called_once()
    list_mock.assert_called_with()


def test_preDisplayedCharacterInfo_none(mocker):
    testObj = setup_test(mocker)
    info_return = {
        "test007": "テスト1",
        "test008": "テスト2",
    }
    info_mock = mocker.patch.object(testObj, "makeDisplayedData", return_value=info_return)
    list_return = []
    list_mock = mocker.patch.object(testObj, "getCharacterNameList", return_value=list_return)
    assert testObj.preDisplayedCharacterInfo() == info_return
    info_mock.assert_called_once()
    info_param = None
    info_mock.assert_called_with(info_param)
    list_mock.assert_called_once()
    list_mock.assert_called_with()


def test_makeDisplayedData_isUsed_True(mocker):
    testObj = setup_test(mocker)
    character = {
            "characterId": "TEST001",
            "characterName": "テストキャラ1",
            "introduction": "テスト1\nテスト1\nテスト1",
            "dearnessRank": 3,
            "dearnessPoint": 1234,
            "isUsed": True,
            "sortIndex": 10,
            "costumeId": "COS_TEST_001",
            "collaboration": False,
            "dearnessRanking": 100,
            "rankingGetDate": "2022-11-11T04:51:57+00:00",
            "updatedAt": "2023-02-12T05:33:21+00:00",
        }
    success = {
            "characterName": "テストキャラ1",
            "introduction": "テスト1テスト1テスト1",
            "dearnessRank": "ランク 3",
            "dearnessPoint": "1234ポイント",
            "dearnessRanking": "100位",
            "dearnessRankingDate": "2022年11月11日 13:51:57 現在",
            "lastPlayDate": "2023年2月12日 14:33:21",
        }
    assert testObj.makeDisplayedData(character) == success


def test_makeDisplayedData_isUsed_False(mocker):
    testObj = setup_test(mocker)
    character = {
            "characterId": "TEST001",
            "characterName": "テストキャラ1",
            "introduction": "テスト1\nテスト1\nテスト1",
            "dearnessRank": 4,
            "dearnessPoint": 1235,
            "isUsed": False,
            "sortIndex": 10,
            "costumeId": "COS_TEST_001",
            "collaboration": False,
            "dearnessRanking": None,
            "rankingGetDate": None,
            "updatedAt": "2024-02-12T05:33:21+00:00",
        }
    success = {
            "characterName": "テストキャラ1",
            "introduction": "テスト1テスト1テスト1",
            "dearnessRank": "ランク 4",
            "dearnessPoint": "1235ポイント",
            "dearnessRanking": "--- 位",
            "dearnessRankingDate": "-----",
            "lastPlayDate": "2024年2月12日 14:33:21",
        }
    assert testObj.makeDisplayedData(character) == success


def test_makeDisplayedData_None(mocker):
    testObj = setup_test(mocker)
    success = {
            "characterName": "データなし",
            "introduction": "",
            "dearnessRank": "ランク ",
            "dearnessPoint": "ポイント",
            "dearnessRanking": "--- 位",
            "dearnessRankingDate": "-----",
            "lastPlayDate": "---",
        }
    assert testObj.makeDisplayedData(None) == success
