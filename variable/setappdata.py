# -*- coding: utf-8 -*-
from kivy.properties import StringProperty
from kivy.event import EventDispatcher


class AppCommonData(EventDispatcher):
    displayChartId = StringProperty()

    def setDisplayChartId(self, chartId):
        self.displayChartId = chartId

    def getDisplayChartId(self):
        return self.displayChartId


if __name__ == '__main__':
    pass
