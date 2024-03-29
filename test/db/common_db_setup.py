# coding:utf-8
import sys
import shutil
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\..\\src\\'))
from constant import systemconstant

BACKUP_DB_NAME = systemconstant.TETOCONE_DB_NAME
test_file_name = './pytest_data.db'

def remove_db_file(fileName):
    if os.path.isfile(fileName):
        os.remove(fileName)


def remove_test_db_file():
    remove_db_file(test_file_name)


def copy_file_db(fileName):
    shutil.copy(fileName, test_file_name)
    return test_file_name


def getParamJson(fileName):
    f = open(os.path.join("test", "db", fileName), 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    return json.loads(data)

