# -*- coding: utf-8 -*-
import sqlite3

from constant.systemconstant import TETOCONE_DB_NAME


def dbinserts(
        musicDist,
        chartDist,
        highScoreList,
        highScoreHistoryList,
        rankHistoryList):
    musicDeleteSql = "DELETE FROM music WHERE id IN"
    musicInsertSql = """
            INSERT INTO music (
                "id","name","artist_id","genre_id","start_date",
                "new_date", "end_date", "release_month", "display_end_date")
            values
        """

    chartConDeleteSql = """
            DELETE FROM "chart_constitution" WHERE "music_id" IN
        """

    chartConInsertSql = """
            INSERT INTO "chart_constitution"
                ("chart_id","music_id","level_id")
            values
        """

    highScoreDeleteSql = """
            DELETE FROM "high_score"
            WHERE ("chart_id","mode") IN
        """

    highScoreInsertSql = """
            INSERT INTO "high_score"
                ("chart_id","mode","music_id","high_score","max_combo","play_count",
                    "cleared_count","full_combo_count","perfect_count","update_time")
            values
        """

    highScoreHistoryInsertSql = """
        INSERT INTO high_score_history
            (chart_id, mode, high_score, max_combo, update_time)
        VALUES
    """

    rankHistoryDeleteSql = """
        DELETE FROM "rank_history" WHERE "chart_id" IN
    """

    rankHistoryInsertSql = """
        INSERT INTO "rank_history"("chart_id","mode","rank","count") VALUES
    """

    deleteWhereMusicId = " ("
    deleteWhereChartId = " ("
    deleteWhereChartMode = " ("

    # insert用パラメータ設定
    musicInsertParams = []
    chartInsertParams = []
    highScoreInsertParams = []
    chartModeDeleteParams = []
    highScoreHistoryParams = []
    rankhistoryParams = []

    for index, music in enumerate(musicDist.values()):
        musicInsertParams.append(music["id"])
        musicInsertParams.append(music["name"])
        musicInsertParams.append(music["artistId"])
        musicInsertParams.append(music["genreId"])
        musicInsertParams.append(music["startDate"])
        musicInsertParams.append(music["newDate"])
        musicInsertParams.append(music["endDate"])
        musicInsertParams.append(music["releaseMonth"])
        musicInsertParams.append(music["displayEndDate"])

        deleteWhereMusicId += "?"
        musicInsertSql += " (?,?,?,?,?,?,?,?,?)"

        if (index != len(musicDist.keys()) - 1):
            deleteWhereMusicId += ","
            musicInsertSql += ","
        else:
            deleteWhereMusicId += ")"

    for index, chart in enumerate(chartDist.values()):
        chartInsertParams.append(chart["chartId"])
        chartInsertParams.append(chart["musicId"])
        chartInsertParams.append(chart["levelId"])

        deleteWhereChartId += "?"
        chartConInsertSql += " (?,?,?)"

        if (index != len(chartDist.keys()) - 1):
            deleteWhereChartId += ","
            chartConInsertSql += ","
        else:
            deleteWhereChartId += ")"

    for index, highScore in enumerate(highScoreList):
        highScoreInsertParams.append(highScore["chartId"])
        highScoreInsertParams.append(highScore["mode"])
        highScoreInsertParams.append(highScore["musicId"])
        highScoreInsertParams.append(highScore["highScore"])
        highScoreInsertParams.append(highScore["maxCombo"])
        highScoreInsertParams.append(highScore["playCount"])
        highScoreInsertParams.append(highScore["clearedCount"])
        highScoreInsertParams.append(highScore["fullComboCount"])
        highScoreInsertParams.append(highScore["perfectCount"])
        highScoreInsertParams.append(highScore["updateTime"])

        chartModeDeleteParams.append(highScore["chartId"])
        chartModeDeleteParams.append(highScore["mode"])

        highScoreInsertSql += " (?,?,?,?,?,?,?,?,?,?)"
        deleteWhereChartMode += "(?,?)"

        if (index != len(highScoreList) - 1):
            deleteWhereChartMode += ","
            highScoreInsertSql += ","
        else:
            deleteWhereChartMode += ")"

    for index, highScore in enumerate(highScoreHistoryList):
        highScoreHistoryParams.append(highScore["chartId"])
        highScoreHistoryParams.append(highScore["mode"])
        highScoreHistoryParams.append(highScore["highScore"])
        highScoreHistoryParams.append(highScore["maxCombo"])
        highScoreHistoryParams.append(highScore["updateTime"])

        highScoreHistoryInsertSql += " (?,?,?,?,?)"

        if (index != len(highScoreHistoryList) - 1):
            highScoreHistoryInsertSql += ","

    for index, rankHistory in enumerate(rankHistoryList):
        rankhistoryParams.append(rankHistory["chartId"])
        rankhistoryParams.append(rankHistory["mode"])
        rankhistoryParams.append(rankHistory["rank"])
        rankhistoryParams.append(rankHistory["count"])

        rankHistoryInsertSql += " (?,?,?,?)"
        if (index != len(rankHistoryList) - 1):
            rankHistoryInsertSql += ","

    musicDeleteSql += deleteWhereMusicId
    chartConDeleteSql += deleteWhereMusicId
    highScoreDeleteSql += deleteWhereChartMode
    rankHistoryDeleteSql += deleteWhereChartId

    # 1トランザクションでDB更新を実行
    with sqlite3.connect(TETOCONE_DB_NAME) as conn:
        conn.execute('BEGIN')
        try:
            conn.execute(musicDeleteSql, list(musicDist.keys()))
            conn.execute(musicInsertSql, musicInsertParams)
            conn.execute(chartConDeleteSql, list(musicDist.keys()))
            conn.execute(chartConInsertSql, chartInsertParams)
            conn.execute(highScoreDeleteSql, chartModeDeleteParams)
            conn.execute(highScoreInsertSql, highScoreInsertParams)

            if len(highScoreHistoryList) != 0:
                conn.execute(highScoreHistoryInsertSql, highScoreHistoryParams)

            conn.execute(rankHistoryDeleteSql, list(chartDist.keys()))
            conn.execute(rankHistoryInsertSql, rankhistoryParams)

            conn.commit()

        except Exception as e:
            conn.rollback()
            raise e

    return


if __name__ == '__main__':
    pass
