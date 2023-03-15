# coding:utf-8
import sys
import os
import filecmp

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from db import ranking


def test_updateRanking_nodata():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    ranking.updateRanking("test000_00", 9012, "2023-01-10T20:09:01+00:00")
    assert filecmp.cmp(test_file_name, "test/db/ranking/updateRanking/result_nodata.db")


def test_updateRanking_dataUpdate():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    ranking.updateRanking("test001_01", 1234, "2020-02-10T20:09:01+00:00")
    assert filecmp.cmp(test_file_name, "test/db/ranking/updateRanking/result_update.db")


def test_selectRankingForChartId_nodata():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    success = []
    assert ranking.selectRankingForChartId("test000_01") == success


def test_selectRankingForChartId():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test001_00",
        "ranking": "4321",
        "getDate": "2023-02-10T20:09:01+00:00",
    }]
    assert ranking.selectRankingForChartId("test001_00") == success


def test_selectRankingList_none_level():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    success = []
    assert ranking.selectRankingList(levelId=4) == success


def test_selectRankingList_none_genre():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    success = []
    assert ranking.selectRankingList(searchGenreId="P001") == success


def test_selectRankingList_one_level():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test001_00",
        "ranking": "4321",
        "getDate": "2023-02-10T20:09:01+00:00",
        "musicName": "テスト1",
        "levelId": 1,
    }]
    assert ranking.selectRankingList(levelId=1) == success


def test_selectRankingList_one_genru():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test002_01",
        "ranking": "123",
        "getDate": "2023-01-08T20:09:01+00:00",
        "musicName": "テスト2",
        "levelId": 2,
    }]
    assert ranking.selectRankingList(searchGenreId="G002") == success


def test_selectRankingList_one_all():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test001_01",
        "ranking": "1234",
        "getDate": "2023-02-11T20:09:01+00:00",
        "musicName": "テスト1",
        "levelId": 2,
    }]
    assert ranking.selectRankingList(levelId=2, searchGenreId="G001") == success


def test_selectRankingList_three():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test001_01",
        "ranking": "1234",
        "getDate": "2023-02-11T20:09:01+00:00",
        "musicName": "テスト1",
        "levelId": 2,
        },
        {
        "chartId": "test002_01",
        "ranking": "123",
        "getDate": "2023-01-08T20:09:01+00:00",
        "musicName": "テスト2",
        "levelId": 2,
        },
        {
        "chartId": "test003_01",
        "ranking": "456",
        "getDate": "2022-01-08T20:09:01+00:00",
        "musicName": "テスト3",
        "levelId": 2,
        },
    ]
    assert ranking.selectRankingList(levelId=2) == success


def test_selectRankingList_noparam():
    befour_db_name = "test/db/ranking/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    ranking.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test001_00",
        "ranking": "4321",
        "getDate": "2023-02-10T20:09:01+00:00",
        "musicName": "テスト1",
        "levelId": 1,
        },
        {
        "chartId": "test001_01",
        "ranking": "1234",
        "getDate": "2023-02-11T20:09:01+00:00",
        "musicName": "テスト1",
        "levelId": 2,
        },
        {
        "chartId": "test001_02",
        "ranking": "5678",
        "getDate": "2023-02-08T20:09:01+00:00",
        "musicName": "テスト1",
        "levelId": 3,
        },
        {
        "chartId": "test002_01",
        "ranking": "123",
        "getDate": "2023-01-08T20:09:01+00:00",
        "musicName": "テスト2",
        "levelId": 2,
        },
        {
        "chartId": "test003_01",
        "ranking": "456",
        "getDate": "2022-01-08T20:09:01+00:00",
        "musicName": "テスト3",
        "levelId": 2,
        },
    ]
    assert ranking.selectRankingList() == success
