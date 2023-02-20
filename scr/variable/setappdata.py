# -*- coding: utf-8 -*-
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.event import EventDispatcher
from constant.systemconstant import DB_VERSION_08

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

    def setDisplayChartId(self, chartId):
        self.displayChartId = chartId

    def getDisplayChartId(self):
        return self.displayChartId

    def clearSourceWidget(self):
        sourceWidget = self.sourceWidget
        self.sourceWidget = ""
        return sourceWidget

    def checkRankingData(self):
        if self.dbFileVersion == DB_VERSION_08:
            return True

        return False


if __name__ == '__main__':
    pass
