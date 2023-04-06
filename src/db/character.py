# -*- coding: utf-8 -*-
import sqlite3
from constant.systemconstant import TETOCONE_DB_NAME


SELECT_SQL = """
    SELECT id, name, introduction, dearness_rank, dearness_point, is_used, sort_index, costume_id, updated_at FROM character ORDER BY sort_index
"""

DELETE_SQL = "DELETE FROM character WHERE id IN ("

INSERT_SQL = "INSERT INTO character (id, name, introduction, dearness_rank, dearness_point, is_used, sort_index, costume_id, updated_at) VALUES "
INSERT_PARAM_SQL = "(?,?,?,?,?,?,?,?,?)"


def selectCharacter():
    characterList = []

    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_SQL, )
        for row in cur:
            characterList.append({
                    "characterId": row[0],
                    "characterName": row[1],
                    "introduction": row[2],
                    "dearnessRank": row[3],
                    "dearnessPoint": row[4],
                    "isUsed": row[5],
                    "sortIndex": row[6],
                    "costumeId": row[7],
                    "updatedAt": row[8],
                })

    return characterList


def insertCharacter(characterList):
    deleteSql = DELETE_SQL
    insertSql = INSERT_SQL
    deleteParams = []
    insertParams = []

    for index, character in enumerate(characterList):
        deleteParams.append(character["characterId"])
        insertParams.append(character["characterId"])
        insertParams.append(character["characterName"])
        insertParams.append(character["introduction"])
        insertParams.append(character["dearnessRank"])
        insertParams.append(character["dearnessPoint"])
        insertParams.append(character["isUsed"])
        insertParams.append(character["sortIndex"])
        insertParams.append(character["costumeId"])
        insertParams.append(character["updatedAt"])
        deleteSql += "?"
        insertSql += INSERT_PARAM_SQL

        if (index != len(characterList) - 1):
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
