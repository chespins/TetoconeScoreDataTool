# coding:utf-8
import pytest
import sys
import os
import filecmp

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\'))
import common_db_setup

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\..\\..\\src\\'))
from db import dbversion

test_file_name = './pytest_data.db'


def test_ddlInsert(mocker):
    common_db_setup.remove_db_file(test_file_name)
    common_db_setup.set_test_db_name(test_file_name)
    mocker.patch('constant.systemconstant.TETOCONE_DB_NAME', test_file_name)
    dbversion.ddlInsert()
    assert filecmp.cmp(test_file_name, "test/db/dbversion/ddlInserts/result_ok.db")
