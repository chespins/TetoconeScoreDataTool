# coding:utf-8
import pytest
import sys
import os
import filecmp

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\..\\src\\'))
from db import dbversion


def test_ddlInsert(mocker):
    befour_db_name = "test/db/dbversion/dbUpdateFrom05/befour_data.db"
    test_file_name = common_db_setup.copy_file_db(befour_db_name)
    mocker.patch('constant.systemconstant.TETOCONE_DB_NAME', test_file_name)
    dbversion.dbUpdateFrom05()
    assert filecmp.cmp(test_file_name, "test/db/dbversion/dbUpdateFrom05/result_ok.db")
