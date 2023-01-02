# -*- coding: utf-8 -*-
import sqlite3
from constant.systemconstant import TETOCONE_DB_NAME


SELECT_SQL = """
    SELECT "chart_id","music_id","level_id" FROM "chart_constitution"
        ORDER BY "chart_id"
"""

SELECT_ID_SQL = """
    SELECT "chart_id","music_id","level_id" FROM "chart_constitution"
        WHERE "music_id" = ?
"""

SELECT_NAME_ID_SQL = """
    SELECT ch."chart_id",ch."music_id",ch."level_id",mu."name",mu."genre_id"
        FROM "chart_constitution" ch
            INNER JOIN music AS mu on mu."id" = ch."music_id"
        WHERE ch.chart_id = ?
"""

SELECT_LEVEL_SQL = """
    SELECT ch."chart_id",ch."music_id",ch."level_id",mu."genre_id", hs."high_score"
        FROM "chart_constitution" ch
            INNER JOIN music AS mu ON mu."id" = ch."music_id"
            INNER JOIN high_score AS hs ON ch."chart_id" = hs."chart_id"
        WHERE hs."mode" = 1 AND ch.level_id IN 
"""


def selectMusic():
    chartList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_SQL)
        for row in cur:
            chartList.append(
                    {"chartId": row[0], "musicId": row[1], "levelId": row[2]}
            )

    return chartList


def selectChartByMusicId(musicId):
    chartList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_ID_SQL, (musicId, ))
        for row in cur:
            chartList.append(
                    {"chartId": row[0], "musicId": row[1], "levelId": row[2]}
            )

    return chartList


def selectChartByChartId(chartId):
    chartList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_NAME_ID_SQL, (chartId, ))
        for row in cur:
            chartList.append({
                    "chartId": row[0],
                    "musicId": row[1],
                    "levelId": row[2],
                    "musicName": row[3],
                    "genreId": row[4],
                })

    return chartList


def selectedLevelId(levelIdList):
    paramList = []
    chartList = []
    selectWherelevelIdSQL = SELECT_LEVEL_SQL + " ("

    for index, levelId in enumerate(levelIdList):
        paramList.append(levelId)
        selectWherelevelIdSQL += "?"

        if (index != len(levelIdList) - 1):
            selectWherelevelIdSQL += ","
        else:
            selectWherelevelIdSQL += ") "

    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(selectWherelevelIdSQL, paramList)
        for row in cur:
            chartList.append({
                    "chartId": row[0],
                    "musicId": row[1],
                    "levelId": row[2],
                    "genreId": row[3],
                    "highScore": row[4],
                })

    return chartList


if __name__ == '__main__':
    pass
