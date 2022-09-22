# -*- coding: utf-8 -*-
import os

from db import dbversion as dbv
from exception.dbversionError import DBVersionError
from constant.systemconstant import TETOCONE_DB_NAME
from constant.systemconstant import CURRENT_DB_VERSION


def checkDbVersion():
    if not os.path.isfile(TETOCONE_DB_NAME):
        dbv.ddlInsert()
        return 0

    try:
        readDbVersion = dbv.getDbVersion()
        if CURRENT_DB_VERSION == readDbVersion:
            return 0
        else:
            return -2

    except DBVersionError:
        return -1


def makeDataFile():
    os.remove(TETOCONE_DB_NAME)
    dbv.ddlInsert()
    return True


if __name__ == '__main__':
    pass
