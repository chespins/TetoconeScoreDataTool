# -*- coding: utf-8 -*-

from db import rankhistory as rah
from constant.distConstant import RANK_DIST

def getRankHistoryDataForChartId(chartId):
    margeRankHistoryDist = {}
    screenRankHistoryList = []
    rankHistoryList = rah.selectChartByChartId(chartId)

    for rankHistory in rankHistoryList:
        count = rankHistory["count"]
        rank = rankHistory["rank"]
        if rankHistory["rank"] in margeRankHistoryDist.keys():
            count += margeRankHistoryDist[rank]["count"]

        margeRankHistoryDist[rank] = {
                "rank": rankHistory["rank"],
                "count": count
            }

    for rank in RANK_DIST.keys():
        if rank in margeRankHistoryDist.keys():
            screenRankHistoryList.append({
                    "rank": RANK_DIST[rank],
                    "count": str(
                            margeRankHistoryDist[rank]["count"]
                        ) + "回"
            })

    return screenRankHistoryList


if __name__ == '__main__':
    pass
