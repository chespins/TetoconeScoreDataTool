# coding:utf-8
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from db import degrees


def test_select_none():
    befour_db_name = "test/db/degrees/degrees_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    degrees.TETOCONE_DB_NAME = test_file_name
    success = []
    assert degrees.selectDegrees(category="test0") == success
    

def test_select_category_one():
    befour_db_name = "test/db/degrees/degrees_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    degrees.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "degreesId": "test001",
                    "degreesName": "テスト1",
                    "category": "test1",
                    "missionLabel": "テスト1テスト1",
                    "createdAt": "2023-01-10T20:09:01+00:00",
                    "updatedAt": "2023-01-11T20:09:01+00:00",
        }]
    assert degrees.selectDegrees(category="test1") == success


def test_select_category_two():
    befour_db_name = "test/db/degrees/degrees_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    degrees.TETOCONE_DB_NAME = test_file_name
    success = [
        {
                    "degreesId": "test002",
                    "degreesName": "テスト2",
                    "category": "test2",
                    "missionLabel": "テスト2テスト2",
                    "createdAt": "2023-02-10T20:09:01+00:00",
                    "updatedAt": "2023-02-11T20:09:01+00:00",
        },
        {
                    "degreesId": "test003",
                    "degreesName": "テスト3",
                    "category": "test2",
                    "missionLabel": "テスト3テスト3",
                    "createdAt": "2023-03-10T20:09:01+00:00",
                    "updatedAt": "2023-03-11T20:09:01+00:00",
        }]
    assert degrees.selectDegrees(category="test2") == success


def test_select_missionLabel_one():
    befour_db_name = "test/db/degrees/degrees_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    degrees.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "degreesId": "test002",
                    "degreesName": "テスト2",
                    "category": "test2",
                    "missionLabel": "テスト2テスト2",
                    "createdAt": "2023-02-10T20:09:01+00:00",
                    "updatedAt": "2023-02-11T20:09:01+00:00",
        }]
    assert degrees.selectDegrees(searchMissionLabel="テスト2テスト2") == success


def test_select_missionLabel_three():
    befour_db_name = "test/db/degrees/degrees_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    degrees.TETOCONE_DB_NAME = test_file_name
    success = [
        {
                    "degreesId": "test001",
                    "degreesName": "テスト1",
                    "category": "test1",
                    "missionLabel": "テスト1テスト1",
                    "createdAt": "2023-01-10T20:09:01+00:00",
                    "updatedAt": "2023-01-11T20:09:01+00:00",
        },
        {
                    "degreesId": "test002",
                    "degreesName": "テスト2",
                    "category": "test2",
                    "missionLabel": "テスト2テスト2",
                    "createdAt": "2023-02-10T20:09:01+00:00",
                    "updatedAt": "2023-02-11T20:09:01+00:00",
        },
        {
                    "degreesId": "test003",
                    "degreesName": "テスト3",
                    "category": "test2",
                    "missionLabel": "テスト3テスト3",
                    "createdAt": "2023-03-10T20:09:01+00:00",
                    "updatedAt": "2023-03-11T20:09:01+00:00",
        }]
    assert degrees.selectDegrees(searchMissionLabel="スト") == success


def test_select_no_param():
    befour_db_name = "test/db/degrees/degrees_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    degrees.TETOCONE_DB_NAME = test_file_name
    success = [
        {
                    "degreesId": "test001",
                    "degreesName": "テスト1",
                    "category": "test1",
                    "missionLabel": "テスト1テスト1",
                    "createdAt": "2023-01-10T20:09:01+00:00",
                    "updatedAt": "2023-01-11T20:09:01+00:00",
        },
        {
                    "degreesId": "test002",
                    "degreesName": "テスト2",
                    "category": "test2",
                    "missionLabel": "テスト2テスト2",
                    "createdAt": "2023-02-10T20:09:01+00:00",
                    "updatedAt": "2023-02-11T20:09:01+00:00",
        },
        {
                    "degreesId": "test003",
                    "degreesName": "テスト3",
                    "category": "test2",
                    "missionLabel": "テスト3テスト3",
                    "createdAt": "2023-03-10T20:09:01+00:00",
                    "updatedAt": "2023-03-11T20:09:01+00:00",
        }]
    assert degrees.selectDegrees() == success
