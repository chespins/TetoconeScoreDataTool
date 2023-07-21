# -*- coding: utf-8 -*-
import sqlite3
from constant.systemconstant import TETOCONE_DB_NAME


SELECT_SQL = """
        SELECT "chart_id","mode","rank","count" FROM "rank_history" ORDER BY "rank", "mode"
"""

SELECT_ID_SQL = """
        SELECT "chart_id","mode","rank","count" FROM "rank_history"
        WHERE "chart_id" = ? AND "mode" IN
"""

ORDER_BY_SQL = """
        ORDER BY "rank", "mode"
"""


def selectAllRankData():
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


def selectChartByChartIdMode(chartId, modeList):
    chartList = []
    paramList = [chartId]
    selectWhereModeSQL = SELECT_ID_SQL + " ("

    for index, mode in enumerate(modeList):
        paramList.append(mode)
        selectWhereModeSQL += "?"

        if (index != len(modeList) - 1):
            selectWhereModeSQL += ","
        else:
            selectWhereModeSQL += ") "


    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(selectWhereModeSQL, paramList)
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
