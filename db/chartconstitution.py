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


if __name__ == '__main__':
    pass
