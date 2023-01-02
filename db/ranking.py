 # -*- coding: utf-8 -*-
import sqlite3
from constant.systemconstant import TETOCONE_DB_NAME

DELETE_SQL = "DELETE FROM score_ranking WHERE chart_id = ?"
INSERT_SQL = "INSERT INTO score_ranking (chart_id, ranking, get_date) VALUES (?, ?, ?)"


def updateranking(chartId, ranking, getDate):
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        conn.execute('BEGIN')
        try:
            conn.execute(DELETE_SQL, (chartId, ))
            conn.execute(INSERT_SQL, (chartId, ranking, getDate, ))
            conn.commit()
    
        except Exception as e:
            conn.rollback()
            raise e



