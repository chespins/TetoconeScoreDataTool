# -*- coding: utf-8 -*-
import sqlite3
from constant.systemconstant import TETOCONE_DB_NAME


SELECT_SQL = """
        SELECT "chart_id","mode","rank","count" FROM "rank_history"
"""

SELECT_ID_SQL = """
        SELECT "chart_id","mode","rank","count" FROM "rank_history"
        WHERE "chart_id" = ? ORDER BY "rank", "mode"
"""


def selectMusic():
    chartList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_SQL)
        for row in cur:
            chartList.append({
                    "chartId": row[0],
                    "mode": row[1],
                    "rank": row[2],
                    "count": row[3]
                })

    return chartList


def selectChartByChartId(chartId):
    chartList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_ID_SQL, (chartId,))
        for row in cur:
            chartList.append({
                    "chartId": row[0],
                    "mode": row[1],
                    "rank": row[2],
                    "count": row[3]
                })

    return chartList


if __name__ == '__main__':
    pass
