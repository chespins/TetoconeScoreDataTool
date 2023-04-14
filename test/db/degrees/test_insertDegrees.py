# coding:utf-8
import sys
import os
import filecmp

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from db import degrees


def test_insert_new():
    befour_db_name = "test/db/degrees/degrees_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    degrees.TETOCONE_DB_NAME = test_file_name
    degreesList = [
            {
                "degreesId": "test004",
                "degreesName": "テスト4",
                "category": "test4",
                "missionLabel": "テスト4テスト4",
                "createdAt": "2023-04-10T20:09:01+00:00",
                "updatedAt": "2023-04-11T20:09:01+00:00",
            }
        ]
    degrees.insertDegrees(degreesList)
    assert filecmp.cmp(test_file_name, "test/db/degrees/insertDegrees/insert_new.db")


def test_insert_update():
    befour_db_name = "test/db/degrees/degrees_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    degrees.TETOCONE_DB_NAME = test_file_name
    degreesList = [
            {
                "degreesId": "test001",
                "degreesName": "テスト1-1",
                "category": "test1-1",
                "missionLabel": "テスト1テスト1-1",
                "createdAt": "2023-04-10T20:09:01+00:00",
                "updatedAt": "2023-04-11T20:09:01+00:00",
            },
            {
                "degreesId": "test002",
                "degreesName": "テスト2-2",
                "category": "test2-2",
                "missionLabel": "テスト2テスト2-2",
                "createdAt": "2023-05-10T20:09:01+00:00",
                "updatedAt": "2023-05-11T20:09:01+00:00",
            },
            {
                "degreesId": "test003",
                "degreesName": "テスト3-3",
                "category": "test3-3",
                "missionLabel": "テスト3テスト3-3",
                "createdAt": "2023-06-10T20:09:01+00:00",
                "updatedAt": "2023-06-11T20:09:01+00:00",
            },
            {
                "degreesId": "test004",
                "degreesName": "テスト4",
                "category": "test4",
                "missionLabel": None,
                "createdAt": "2023-07-10T20:09:01+00:00",
                "updatedAt": "2023-07-11T20:09:01+00:00",
            }
        ]
    degrees.insertDegrees(degreesList)
    assert filecmp.cmp(test_file_name, "test/db/degrees/insertDegrees/insert_update.db")
