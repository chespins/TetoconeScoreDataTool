# -*- coding: utf-8 -*-
import sqlite3
from constant.systemconstant import TETOCONE_DB_NAME


SELECT_SQL = """
    SELECT
        id, name, category, mission_label, created_at, updated_at
    FROM degrees WHERE 1 = 1 
"""

ORDER_BY_SQL = " ORDER BY id"

DELETE_SQL = "DELETE FROM degrees WHERE id IN ("

INSERT_SQL = "INSERT INTO degrees (id, name, category, mission_label, created_at, updated_at) VALUES "
INSERT_PARAM_SQL = "(?,?,?,?,?,?)"


def selectDegrees(category="", searchMissionLabel=""):
    degreesList = []
    paramList = []
    whereCategorySql = " AND category = ? "
    whereMissionLabelSql = " AND mission_label like '%' || ? || '%'"
    selectSql = SELECT_SQL

    if category != "":
        selectSql += whereCategorySql
        paramList.append(category)

    if searchMissionLabel != "":
        selectSql += whereMissionLabelSql
        paramList.append(searchMissionLabel)

    selectSql += ORDER_BY_SQL

    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(selectSql, paramList)
        for row in cur:
            degreesList.append({
                    "degreesId": row[0],
                    "degreesName": row[1],
                    "category": row[2],
                    "missionLabel": row[3],
                    "createdAt": row[4],
                    "updatedAt": row[5],
                })

    return degreesList


def insertDegrees(degreesList):
    deleteSql = DELETE_SQL
    insertSql = INSERT_SQL
    deleteParams = []
    insertParams = []

    for index, degrees in enumerate(degreesList):
        deleteParams.append(degrees["degreesId"])
        insertParams.append(degrees["degreesId"])
        insertParams.append(degrees["degreesName"])
        insertParams.append(degrees["category"])
        insertParams.append(degrees["missionLabel"])
        insertParams.append(degrees["createdAt"])
        insertParams.append(degrees["updatedAt"])
        deleteSql += "?"
        insertSql += INSERT_PARAM_SQL

        if (index != len(degreesList) - 1):
            deleteSql += ","
            insertSql += ","
        else:
            deleteSql += ")"

    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        conn.execute('BEGIN')
        try:
            conn.execute(deleteSql, deleteParams)
            conn.execute(insertSql, insertParams)
            conn.commit()

        except Exception as e:
            conn.rollback()
            raise e
        
    return
