# -*- coding: utf-8 -*-
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.event import EventDispatcher

from model import createDataFile as crd


class AppCommonData(EventDispatcher):
    displayChartId = StringProperty()
    checkDbresult = NumericProperty(0)
    readOnlyFlg = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(AppCommonData, self).__init__(**kwargs)
        self.checkDbresult = crd.checkDbVersion()

    def setDisplayChartId(self, chartId):
        self.displayChartId = chartId

    def getDisplayChartId(self):
        return self.displayChartId


if __name__ == '__main__':
    pass
