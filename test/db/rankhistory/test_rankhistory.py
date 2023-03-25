# coding:utf-8
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\src\\'))
from db import rankhistory


def test_rank_none_chart():
    befour_db_name = "test/db/rankhistory/test001_3_4.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    rankhistory.TETOCONE_DB_NAME = test_file_name
    success = []
    assert rankhistory.selectChartByChartIdMode("test000", {3, 4}) == success


def test_rank_none_mode():
    befour_db_name = "test/db/rankhistory/test001_3_4.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    rankhistory.TETOCONE_DB_NAME = test_file_name
    success = []
    assert rankhistory.selectChartByChartIdMode("test001", {1}) == success


def test_rank_one_data():
    befour_db_name = "test/db/rankhistory/test001_3_4.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    rankhistory.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "chartId": "test001",
                    "mode": 4,
                    "rank": "S",
                    "count": 2
                }]
    assert rankhistory.selectChartByChartIdMode("test001", {4}) == success


def test_rank_three_data():
    befour_db_name = "test/db/rankhistory/test001_3_4.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    rankhistory.TETOCONE_DB_NAME = test_file_name
    success = [{
                    "chartId": "test001",
                    "mode": 3,
                    "rank": "B",
                    "count": 3
                },
                {
                    "chartId": "test001",
                    "mode": 3,
                    "rank": "S",
                    "count": 1
                },
                {
                    "chartId": "test001",
                    "mode": 4,
                    "rank": "S",
                    "count": 2
                }]
    assert rankhistory.selectChartByChartIdMode("test001", {1,2,3,4,5,6}) == success
