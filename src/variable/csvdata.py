# -*- coding: utf-8 -*-
from util import util

from constant.distConstant import LEVEL_NAME_DIST
from constant.distConstant import MODE_NAME_DIST
from constant.distConstant import RANK_DIST
from util import util

class CsvSourseDataType():
    def __init__(self, sourceDataName: str, keyColumnName: str, keyDataFlg: bool):
        self.sourceDataName = sourceDataName
        self.keyColumnName = keyColumnName
        self.keyDataFlg = keyDataFlg


class CsvDataType():
    def __init__(self, rankFlg: bool, timeFlg: bool, levelFlg: bool, modeFlg: bool, countFlg: bool):
        self.rankFlg = rankFlg
        self.timeFlg = timeFlg
        self.levelFlg = levelFlg
        self.modeFlg = modeFlg
        self.countFlg = countFlg


class CsvDataHeader():
    def __init__(self, sourceDataName: str, columnName: (str), headerName: str, dataType: CsvSourseDataType):
        self.sourceDataName = sourceDataName
        self.columnName = columnName
        self.headerName = headerName
        self.dataType = dataType

    def outputData(self, rowData):
        if self.dataType.rankFlg:
            if self.columnName in rowData:
                return rowData[self.columnName]["count"]
            
            return 0
        
        else:
            columnData = rowData[self.columnName]
            try:
                if self.dataType.timeFlg:
                    return util.changeTimeZone(columnData)
        
                elif self.dataType.levelFlg:
                    return LEVEL_NAME_DIST[str(columnData)].name

                elif self.dataType.modeFlg:
                    return MODE_NAME_DIST[str(columnData)]
        
                elif self.dataType.countFlg:
                    return columnData
            except:
                print("解析エラー")

            return str(columnData)
