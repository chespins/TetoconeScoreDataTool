# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen

from view import highScoreDetails as det
from variable.setappdata import AppCommonData

class BaseScoreListScreen(Screen):
    leaveFlg = False

    def __init__(self, commonData: AppCommonData, **kwargs):
        super(BaseScoreListScreen, self).__init__(**kwargs)
        self.commonData = commonData

    def on_leave(self, **kwargs):
        if self.leaveFlg: 
            self.manager.remove_widget(self)

        return super().on_leave(*kwargs)

    def switchingMenu(self):
        self.leaveFlg = True
        self.manager.current = 'menu'

    def switchingHighScoreDetails(self, targetChartId, sourceWidget):
        self.commonData.setHistoryData(targetChartId, sourceWidget)
        screenName = 'details'
        self.manager.add_widget(det.HighScoreDetailsScreen(name=screenName, comonData=self.commonData))
        self.manager.current = screenName


if __name__ == '__main__':
    pass
