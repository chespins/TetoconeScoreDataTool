# -*- coding: utf-8 -*-
import os

from db import dbversion as dbv
from constant.systemconstant import TETOCONE_DB_NAME
from constant.systemconstant import CURRENT_DB_VERSION
from constant.systemconstant import DB_VERSION_05
from constant.systemconstant import DB_SUCCESS
from constant.systemconstant import DB_ERROR_FILE_BREAK
from constant.systemconstant import DB_ERROR_UNKNOWN_FILE
from constant.systemconstant import DB_UPDATE


def checkDbVersion():
    if not os.path.isfile(TETOCONE_DB_NAME):
        makeDbFile()
        return (DB_SUCCESS, CURRENT_DB_VERSION)

    try:
        readDbVersion = dbv.getDbVersion()
        if CURRENT_DB_VERSION == readDbVersion:
            return (DB_SUCCESS, readDbVersion)
        elif DB_VERSION_05 == readDbVersion:
            return (DB_UPDATE, readDbVersion)
        else:
            return (DB_ERROR_UNKNOWN_FILE, readDbVersion)

    except:
        return (DB_ERROR_FILE_BREAK, "")


def reMakeDataFile():
    os.remove(TETOCONE_DB_NAME)
    return makeDbFile()


def makeDbFile():
    dbv.ddlInsert()
    return dbUpdateFrom05()


def dbUpdateFrom05():
    dbv.dbUpdateFrom05()
    return True


if __name__ == '__main__':
    pass
