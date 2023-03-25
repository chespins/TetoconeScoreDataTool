# coding:utf-8
import sys
import os
import filecmp

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from db import chartconstitution


def test_selectChartByChartId_none():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    chartconstitution.TETOCONE_DB_NAME = test_file_name
    success = []
    assert chartconstitution.selectChartByChartId("test000_00") == success


def test_selectChartByChartId_one():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    chartconstitution.TETOCONE_DB_NAME = test_file_name
    success = [
        {
        "chartId": "test002_01",
        "musicId": "test002",
        "levelId": 2,
        "musicName": "テスト2",
        "genreId": "G002",
        },
    ]
    assert chartconstitution.selectChartByChartId("test002_01") == success



def test_selectedSingleChart_none_level():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    chartconstitution.TETOCONE_DB_NAME = test_file_name
    success = []
    assert chartconstitution.selectedSingleChart(levelIdList=[4]) == success


def test_selectedSingleChart_none_chartId():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    chartconstitution.TETOCONE_DB_NAME = test_file_name
    success = []
    assert chartconstitution.selectedSingleChart(chartId="test_000") == success


def test_selectedSingleChart_one_level():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    chartconstitution.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test001_00",
        "musicId": "test001",
        "levelId": 1,
        "genreId": "G001",
        "highScore": 1234567,
    }]
    assert chartconstitution.selectedSingleChart(levelIdList=[1]) == success


def test_selectedSingleChart_one_chart():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    chartconstitution.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test002_01",
        "musicId": "test002",
        "levelId": 2,
        "genreId": "G002",
        "highScore": 4234567,
    }]
    assert chartconstitution.selectedSingleChart(chartId="test002_01") == success


def test_selectedSingleChart_one_all():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    chartconstitution.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test003_01",
        "musicId": "test003",
        "levelId": 2,
        "genreId": "G003",
        "highScore": 6234567,
    }]
    assert chartconstitution.selectedSingleChart(levelIdList=[2], chartId="test003_01") == success


def test_selectedSingleChart_multi_level():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    chartconstitution.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test001_00",
        "musicId": "test001",
        "levelId": 1,
        "genreId": "G001",
        "highScore": 1234567,
        },
        {
        "chartId": "test001_02",
        "musicId": "test001",
        "levelId": 3,
        "genreId": "G001",
        "highScore": 3234567,
        },
    ]
    assert chartconstitution.selectedSingleChart(levelIdList=[1, 3, 5]) == success


def test_selectedSingleChart_noparam():
    befour_db_name = "test/db/befour_test.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    chartconstitution.TETOCONE_DB_NAME = test_file_name
    success = [{
        "chartId": "test001_00",
        "musicId": "test001",
        "levelId": 1,
        "genreId": "G001",
        "highScore": 1234567,
        },
        {
        "chartId": "test001_01",
        "musicId": "test001",
        "levelId": 2,
        "genreId": "G001",
        "highScore": 2234567,
        },
        {
        "chartId": "test001_02",
        "musicId": "test001",
        "levelId": 3,
        "genreId": "G001",
        "highScore": 3234567,
        },
        {
        "chartId": "test002_01",
        "musicId": "test002",
        "levelId": 2,
        "genreId": "G002",
        "highScore": 4234567,
        },
        {
        "chartId": "test003_01",
        "musicId": "test003",
        "levelId": 2,
        "genreId": "G003",
        "highScore": 6234567,
        },
    ]
    assert chartconstitution.selectedSingleChart() == success
