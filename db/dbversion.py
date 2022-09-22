# -*- coding: utf-8 -*-
import sqlite3
from tkinter import INSERT

from constant.systemconstant import TETOCONE_DB_NAME
from constant.systemconstant import CURRENT_DB_VERSION
from exception.dbversionError import DBVersionError
from util.util import readFileStr

SELECT_SQL = "SELECT version FROM db_version"

INSERT_SQL = "INSERT INTO db_version (version) VALUES (?)"


def getDbVersion():
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_SQL)
        results = cur.fetchall()
        if len(results) != 1:
            raise DBVersionError()
        
        return results[0][0]


def ddlInsert():
    insertDdlSql = readFileStr("./ddl/tetocone.ddl")
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        conn.execute('BEGIN')
        conn.executescript(insertDdlSql)
        conn.execute(INSERT_SQL, (CURRENT_DB_VERSION, ))
        conn.commit()

        
if __name__ == '__main__':
    pass
