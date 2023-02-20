# -*- coding: utf-8 -*-
import sqlite3
from constant.systemconstant import TETOCONE_DB_NAME


SELECT_MODE_SQL = """
        SELECT chart_id, mode, high_score, max_combo, update_time
        FROM high_score_history
        WHERE chart_id = ? AND mode = ?
        ORDER BY update_time DESC
    """

SELECT_SQL = """
        SELECT chart_id, mode, high_score, max_combo, update_time FROM high_score_history
        WHERE chart_id = ?
        ORDER BY update_time DESC
    """


def selectHighScoreHistoryByMode(chartId, mode):
    highScoreHistryList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_MODE_SQL,(chartId,mode,))
        for row in cur:
            highScoreHistryList.append({
                    "chartId": row[0],
                    "mode": row[1],
                    "highScore": row[2], 
                    "maxCombo": row[3], 
                    "updateTime": row[4]
                    })

    return highScoreHistryList


def selectHighScoreHistoryBychartId(chartId):
    highScoreHistryList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor() 
        cur.execute(SELECT_SQL, (chartId,))
        for row in cur:
            highScoreHistryList.append({
                    "chartId": row[0],
                    "mode": row[1],
                    "highScore": row[2], 
                    "maxCombo": row[3], 
                    "updateTime": row[4]
                })

    return highScoreHistryList


if __name__ == '__main__' :
    pass
