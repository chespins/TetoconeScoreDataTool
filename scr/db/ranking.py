 # -*- coding: utf-8 -*-
import sqlite3
from constant.systemconstant import TETOCONE_DB_NAME

DELETE_SQL = "DELETE FROM score_ranking WHERE chart_id = ?"
INSERT_SQL = "INSERT INTO score_ranking (chart_id, ranking, get_date) VALUES (?, ?, ?)"
SELECT_CHART_SQL = "SELECT chart_id, ranking, get_date FROM score_ranking WHERE chart_id = ?"
SELECT_LIST_SQL = """
        SELECT ra.chart_id, ra.ranking, ra.get_date, mu.name, con.level_id
        FROM score_ranking AS ra
            INNER JOIN chart_constitution AS con ON con.chart_id = ra.chart_id
            INNER JOIN music AS mu ON con.music_id = mu.id
            INNER JOIN high_score AS sc ON sc.chart_id = con.chart_id
        WHERE sc.mode = 1 
"""
SELECT_LIST_ORDER_BY = "ORDER BY ra.chart_id"

def updateRanking(chartId, ranking, getDate):
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        conn.execute('BEGIN')
        try:
            conn.execute(DELETE_SQL, (chartId, ))
            conn.execute(INSERT_SQL, (chartId, ranking, getDate, ))
            conn.commit()
    
        except Exception as e:
            conn.rollback()
            raise e


def selectRankingForChartId(chartId):
    rankingList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_CHART_SQL, (chartId, ))
        for row in cur:
            rankingList.append({
                "chartId": row[0],
                "ranking": row[1],
                "getDate": row[2],
            })

    return rankingList


def selectRankingList(levelId=0, searchGenreId=""):
    paramList = []
    rankingList = []
    LEVEL_NAME_SQL = " AND con.level_id = ? "
    GENRE_NAME_SQL = " AND mu.genre_id = ? "

    SQL = SELECT_LIST_SQL
    if levelId != 0:
        SQL += LEVEL_NAME_SQL
        paramList.append(levelId)

    if searchGenreId != "":
        SQL += GENRE_NAME_SQL
        paramList.append(searchGenreId)

    SQL += SELECT_LIST_ORDER_BY

    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SQL, paramList)
        for row in cur:
            rankingData = {
                "chartId": row[0],
                "ranking": row[1],
                "getDate": row[2],
                "musicName": row[3],
                "levelId": row[4],
            }
        
            rankingList.append(rankingData)

        return rankingList


if __name__ == "main":
    pass
