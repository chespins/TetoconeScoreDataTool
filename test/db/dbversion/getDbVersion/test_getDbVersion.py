# coding:utf-8
import pytest
import sys
import os
from time import sleep

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\..\\src\\'))
from db import dbversion
from exception.dbversionError import DBVersionError


def test_version_none(mocker):
    befour_db_name = "test/db/dbversion/getDbVersion/befour_none.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    mocker.patch('constant.systemconstant.TETOCONE_DB_NAME', test_file_name)
    with pytest.raises(DBVersionError) as e:
        dbversion.getDbVersion()


def test_version_one(mocker):
    befour_db_name = "test/db/dbversion/getDbVersion/befour_one.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    mocker.patch('constant.systemconstant.TETOCONE_DB_NAME', test_file_name)
    assert dbversion.getDbVersion() == "v0.5"


def test_version_two(mocker):
    befour_db_name = "test/db/dbversion/getDbVersion/befour_two.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    mocker.patch('constant.systemconstant.TETOCONE_DB_NAME', test_file_name)
    with pytest.raises(DBVersionError) as e:
        dbversion.getDbVersion()
