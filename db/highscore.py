# -*- coding: utf-8 -*-
import sqlite3
from constant.systemconstant import TETOCONE_DB_NAME


SELECT_SQL = """
    SELECT "chart_id","mode","music_id","high_score","max_combo","play_count",
        "cleared_count","full_combo_count","perfect_count","update_time"
    FROM "high_score"
    ORDER BY"chart_id","mode"
"""

SELECT_ID_SQL = """
    SELECT "chart_id","mode","music_id","high_score","max_combo","play_count",
        "cleared_count","full_combo_count","perfect_count","update_time"
    FROM "high_score" WHERE "chart_id" = ?
    ORDER BY"chart_id","mode"
"""

SELECT_MUSIC_LEVEL_NAME_SQL = """
    SELECT mu.name, ch.level_id, ifnull(sc.mode, 0), ifnull(sc.high_score, 0),
        ch.chart_id, ifnull(sc.full_combo_count, 0), ifnull(sc.perfect_count, 0),
        ifnull(sc.play_count, 0), ifnull(sc.cleared_count, 0)
    FROM chart_constitution AS ch
        LEFT JOIN high_score AS sc on ch.chart_id = sc.chart_id
        INNER JOIN music AS mu on mu.id = ch.music_id
    WHERE mu.name like '%' || ? || '%'
"""

SELECT_MUSIC_LEVEL_NAME_ORDER_SQL = """
    ORDER BY mu.genre_id, ch.music_id, ch.chart_id, sc.mode
"""


def selectHighScoreFullData():
    highScoreList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_SQL)
        for row in cur:
            highScoreList.append({
                    "chartId": row[0],
                    "mode": row[1],
                    "musicId": row[2],
                    "highScore": row[3],
                    "maxCombo": row[4],
                    "playCount": row[5],
                    "clearedCount": row[6],
                    "fullComboCount": row[7],
                    "perfectCount": row[8],
                    "updateTime": row[9]
            })

    return highScoreList


def selectHighScoreByChartId(chartId):
    highScoreList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_ID_SQL, (chartId,))
        for row in cur:
            highScoreList.append({
                    "chartId": row[0],
                    "mode": row[1],
                    "musicId": row[2],
                    "highScore": row[3],
                    "maxCombo": row[4],
                    "playCount": row[5],
                    "clearedCount": row[6],
                    "fullComboCount": row[7],
                    "perfectCount": row[8],
                    "updateTime": row[9]
                })

    return highScoreList


def selectHighScore(musicName, levelId=0):
    highScoreList = []
    LEVEL_NAME_SQL = " AND ch.level_id = ? "
    paramList = [musicName]
    SQL = SELECT_MUSIC_LEVEL_NAME_SQL
    if levelId != 0:
        SQL += LEVEL_NAME_SQL
        paramList.append(levelId)

    SQL += SELECT_MUSIC_LEVEL_NAME_ORDER_SQL

    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SQL, (paramList))
        for row in cur:
            highScoreList.append({
                    "musicName": row[0],
                    "levelId": row[1],
                    "mode": row[2],
                    "highScore": row[3],
                    "chartId": row[4],
                    "fullComboCount": row[5],
                    "perfectCount": row[6],
                    "playCount": row[7],
                    "clearedCount": row[8],
                })

    return highScoreList


if __name__ == '__main__':
    pass
