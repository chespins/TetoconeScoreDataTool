# -*- coding: utf-8 -*-
import os

from db import dbversion as dbv
from exception.dbversionError import DBVersionError
from constant.systemconstant import TETOCONE_DB_NAME
from constant.systemconstant import CURRENT_DB_VERSION
from constant.systemconstant import DB_SUCCESS
from constant.systemconstant import DB_ERROR_FILE_BREAK
from constant.systemconstant import DB_ERROR_UNKNOWN_FILE


def checkDbVersion():
    if not os.path.isfile(TETOCONE_DB_NAME):
        dbv.ddlInsert()
        return DB_SUCCESS

    try:
        readDbVersion = dbv.getDbVersion()
        if CURRENT_DB_VERSION == readDbVersion:
            return DB_SUCCESS
        else:
            return DB_ERROR_UNKNOWN_FILE

    except DBVersionError:
        return DB_ERROR_FILE_BREAK


def makeDataFile():
    os.remove(TETOCONE_DB_NAME)
    dbv.ddlInsert()
    return True


if __name__ == '__main__':
    pass
