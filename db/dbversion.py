# -*- coding: utf-8 -*-
import sqlite3

from constant import systemconstant as syco
from exception.dbversionError import DBVersionError
from util.util import readFileStr

SELECT_SQL = "SELECT version FROM db_version"

INSERT_SQL = "INSERT INTO db_version (version) VALUES (?)"

UPDATE_SQL = "UPDATE db_version SET version = ? WHERE version = ?"


def getDbVersion():
    with sqlite3.connect(syco.TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_SQL)
        results = cur.fetchall()
        if len(results) != 1:
            raise DBVersionError()
        
        return results[0][0]


def ddlInsert():
    insertDdlSql = readFileStr("./ddl/tetocone.ddl")
    with sqlite3.connect(syco.TETOCONE_DB_NAME) as conn:
        conn.execute('BEGIN')
        conn.executescript(insertDdlSql)
        conn.execute(INSERT_SQL, (syco.DB_VERSION_05, ))
        conn.commit()


def dbUpdateFrom05():
    insertDdlSql = readFileStr("./ddl/update_08.ddl")
    with sqlite3.connect(syco.TETOCONE_DB_NAME) as conn:
        conn.execute('BEGIN')
        conn.executescript(insertDdlSql)
        conn.execute(UPDATE_SQL, (syco.CURRENT_DB_VERSION, syco.DB_VERSION_05))
        conn.commit()
        

if __name__ == '__main__':
    pass
