# -*- coding: utf-8 -*-
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.event import EventDispatcher
from constant.systemconstant import DB_VERSION_08
from constant.systemconstant import DB_VERSION_09

from model import createDataFile as crd


class AppCommonData(EventDispatcher):
    displayChartId = StringProperty()
    checkDbresult = NumericProperty(0)
    readOnlyFlg = BooleanProperty(False)
    dbFileVersion = StringProperty()
    sourceWidget = StringProperty()

    def __init__(self, **kwargs):
        super(AppCommonData, self).__init__(**kwargs)
        (self.checkDbresult, self.dbFileVersion) = crd.checkDbVersion()

    def setHistoryData(self, chartId, sourceWidget):
        self.displayChartId = chartId
        self.sourceWidget = sourceWidget

    def clearSourceWidget(self):
        sourceWidget = self.sourceWidget
        self.displayChartId = ""
        self.sourceWidget = ""
        return sourceWidget
    
    def isWidgetRankingData(self):
        return self.sourceWidget == "rankingList"

    def checkRankingData(self):
        okVersionList = [DB_VERSION_08, DB_VERSION_09]
        if self.dbFileVersion in okVersionList:
            return True

        return False


if __name__ == '__main__':
    pass
