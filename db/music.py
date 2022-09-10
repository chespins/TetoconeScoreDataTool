# -*- coding: utf-8 -*-
import sqlite3
from constant.systemconstant import TETOCONE_DB_NAME


SELECT_SQL = """
        SELECT "id","name","artist_id","genre_id","start_date",
            "new_date", "end_date", "release_month", "display_end_date"
        FROM "music"
"""

SELECT_ID_SQL = """
        SELECT "id","name","artist_id","genre_id","start_date",
            "new_date", "end_date", "release_month", "display_end_date"
        FROM "music" WHERE "id" = ?
"""


def selectMusic():
    musicList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_SQL)
        for row in cur:
            musicList.append({
                    "id": row[0],
                    "name": row[1],
                    "artistId": row[2],
                    "genreId": row[3],
                    "startDate": row[4],
                    "newDate": row[5],
                    "endDate": row[6],
                    "releaseMonth": row[7],
                    "displayEndDate": row[8]
                })

    return musicList


def selectMusicById(musicId):
    musicList = []
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(SELECT_ID_SQL, (musicId,))
        for row in cur:
            musicList.append({
                    "id": row[0],
                    "name": row[1],
                    "artistId": row[2],
                    "genreId": row[3],
                    "startDate": row[4],
                    "newDate": row[5],
                    "endDate": row[6],
                    "releaseMonth": row[7],
                    "displayEndDate": row[8]
                })

    return musicList


if __name__ == '__main__':
    pass
