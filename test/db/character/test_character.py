# coding:utf-8
import sys
import os
import filecmp

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from db import character


def test_select_nodata():
    befour_db_name = "test/db/character/character_no_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    character.TETOCONE_DB_NAME = test_file_name
    success = []
    assert character.selectCharacter() == success


def test_select_noparam():
    befour_db_name = "test/db/character/character_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    character.TETOCONE_DB_NAME = test_file_name
    success = [
        {
            "characterId": "TEST001",
            "characterName": "テストキャラ1",
            "introduction": "テスト1\nテスト1\nテスト1",
            "dearnessRank": 1,
            "dearnessPoint": 1234,
            "isUsed": False,
            "sortIndex": 10,
            "costumeId": "COS_TEST_001",
            "collaboration": False,
            "dearnessRanking": 1000,
            "rankingGetDate": "2023-02-02T05:33:21+00:00",
            "updatedAt": "2023-02-12T05:33:21+00:00",
        },
        {
            "characterId": "TEST002",
            "characterName": "テストキャラ2",
            "introduction": "テスト2\nテスト2\nテスト2",
            "dearnessRank": 2,
            "dearnessPoint": 2234,
            "isUsed": False,
            "sortIndex": 11,
            "costumeId": "COS_TEST_002",
            "collaboration": True,
            "dearnessRanking": 2000,
            "rankingGetDate": "2023-03-02T05:33:21+00:00",
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
            "dearnessRanking": 3000,
            "rankingGetDate": "2023-04-02T05:33:21+00:00",
            "updatedAt": "2023-04-12T05:33:21+00:00",
        },
    ]
    assert character.selectCharacter() == success


def test_select_params_empty():
    befour_db_name = "test/db/character/character_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    character.TETOCONE_DB_NAME = test_file_name
    success = []
    assert character.selectCharacter(characterId="TEST000") == success


def test_select_params():
    befour_db_name = "test/db/character/character_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    character.TETOCONE_DB_NAME = test_file_name
    success = [
        {
            "characterId": "TEST002",
            "characterName": "テストキャラ2",
            "introduction": "テスト2\nテスト2\nテスト2",
            "dearnessRank": 2,
            "dearnessPoint": 2234,
            "isUsed": False,
            "sortIndex": 11,
            "costumeId": "COS_TEST_002",
            "collaboration": True,
            "dearnessRanking": 2000,
            "rankingGetDate": "2023-03-02T05:33:21+00:00",
            "updatedAt": "2023-03-12T05:33:21+00:00",
        },
    ]
    assert character.selectCharacter(characterId="TEST002") == success


def test_insert_new():
    befour_db_name = "test/db/character/character_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    character.TETOCONE_DB_NAME = test_file_name
    characterList = [
            {
            "characterId": "TEST004",
            "characterName": "テストキャラ4",
            "introduction": "テスト4\nテスト4\nテスト4",
            "dearnessRank": 4,
            "dearnessPoint": 4234,
            "isUsed": False,
            "sortIndex": 13,
            "costumeId": "COS_TEST_004",
            "collaboration": False,
            "dearnessRanking": 3000,
            "rankingGetDate": "2023-05-02T05:33:21+00:00",
            "updatedAt": "2023-05-12T05:33:21+00:00",
        },
        ]
    character.insertCharacter(characterList)
    assert filecmp.cmp(test_file_name, "test/db/character/insertCharacter/insert_new.db")


def test_insert_update():
    befour_db_name = "test/db/character/character_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    character.TETOCONE_DB_NAME = test_file_name
    characterList = [
        {
            "characterId": "TEST001",
            "characterName": "テストキャラ1",
            "introduction": "テスト1\nテスト1\nテスト1",
            "dearnessRank": 11,
            "dearnessPoint": 1239,
            "isUsed": True,
            "sortIndex": 10,
            "costumeId": "COS_TEST_101",
            "collaboration": False,
            "dearnessRanking": 1100,
            "rankingGetDate": "2024-02-02T05:33:21+00:00",
            "updatedAt": "2024-02-12T05:33:21+00:00",
        },
        {
            "characterId": "TEST002",
            "characterName": "テストキャラ2",
            "introduction": "テスト2\nテスト2\nテスト2",
            "dearnessRank": 12,
            "dearnessPoint": 2239,
            "isUsed": False,
            "sortIndex": 11,
            "costumeId": "COS_TEST_102",
            "collaboration": False,
            "dearnessRanking": 2200,
            "rankingGetDate": "2024-03-02T05:33:21+00:00",
            "updatedAt": "2024-03-12T05:33:21+00:00",
        },
        {
            "characterId": "TEST003",
            "characterName": "テストキャラ3",
            "introduction": "テスト3\nテスト3\nテスト3",
            "dearnessRank": 13,
            "dearnessPoint": 3239,
            "isUsed": False,
            "sortIndex": 12,
            "costumeId": "COS_TEST_103",
            "collaboration": True,
            "dearnessRanking": 3300,
            "rankingGetDate": "2024-04-02T05:33:21+00:00",
            "updatedAt": "2024-04-12T05:33:21+00:00",
        },
            {
            "characterId": "TEST004",
            "characterName": "テストキャラ4",
            "introduction": "テスト4\nテスト4\nテスト4",
            "dearnessRank": 14,
            "dearnessPoint": 4239,
            "isUsed": False,
            "sortIndex": 13,
            "costumeId": "COS_TEST_104",
            "collaboration": False,
            "dearnessRanking": 4400,
            "rankingGetDate": "2024-05-02T05:33:21+00:00",
            "updatedAt": "2024-05-12T05:33:21+00:00",
        },
        ]
    character.insertCharacter(characterList)
    assert filecmp.cmp(test_file_name, "test/db/character/insertCharacter/insert_update.db")
