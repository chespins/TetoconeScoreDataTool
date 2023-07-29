# -*- coding: utf-8 -*-
import csv
import copy

from constant import csvConstant as cv
from constant import messeges as ms


def makeScoreCsvFile(highScoreList, saveFileName, rankFlg, rankHistoryDist={}, modeMargeFlg=False):
    csvHeader = []
    headerBaseList = copy.copy(cv.CSV_SCORE_INFO_HEADER)

    if not modeMargeFlg:
        headerBaseList.append(cv.SCORE_HEADER_PLAY_MODE)

    headerBaseList += cv.CSV_SCORE_SCORE_HEADER

    if rankFlg:
        headerBaseList += cv.CSV_SCORE_RANK_HEADER

    headerBaseList.append(cv.SCORE_HEADER_UPDATE_TIME)

    for header in headerBaseList:
        csvHeader.append(header.headerName)
    
    csvDataList = [csvHeader]

    for highScore in highScoreList:
        csvDataRow = []
        chartId = highScore["chartId"]

        if rankFlg:
            rankKey = copy.copy(chartId)
            if not modeMargeFlg:
                rankKey += "_" + str(highScore["mode"])
            
            rankHistory = rankHistoryDist[rankKey]

        for header in headerBaseList:
            columnData = ""
            if header.sourceDataName == cv.SOURCE_HIGH_SCORE:
                columnData = header.outputData(highScore)
            elif header.sourceDataName == cv.SOURCE_RANK_HISTORY:
                columnData = header.outputData(rankHistory)

            csvDataRow.append(columnData)

        csvDataList.append(csvDataRow)

    if writeCsvFile(saveFileName, csvDataList):
        return ms.CSV_HIGH_SCORE_SUCCESS
    else:
        return ms.CSV_FILE_OUTPUT_ERROR


def writeCsvFile(saveFileName, csvDataList):
    try:
        with open(saveFileName, 'w', encoding='utf_8_sig', newline="") as csvFile:
            writer = csv.writer(csvFile, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(csvDataList)
            return True
        
    except:
        return False


if __name__ == '__main__':
    pass
