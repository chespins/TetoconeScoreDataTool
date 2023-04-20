# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from variable.setappdata import AppCommonData
from model.highScoreHistory import HighScoreHistory
from util import util
from constant.systemconstant import KIVY_CURRENT_DIR


Builder.load_file(util.findDataFile(KIVY_CURRENT_DIR + 'highScoreHistoryDetails.kv'))


class HighScoreHistoryDetailsScreen(Screen):
    highScoreHistoryRv = ObjectProperty()
    chartId = StringProperty()
    allDisplayFlg = True
    score = HighScoreHistory()

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(HighScoreHistoryDetailsScreen, self).__init__(**kwargs)
        self.commonData = comonData

    def on_pre_enter(self, **kwargs):
        if self.chartId == "":
            self.chartId = self.commonData.displayChartId

        musicInfo = self.score.getMusicName(self.chartId)
        self.ids.levelName.text = musicInfo["levelName"]
        self.ids.levelName.color = musicInfo["levelColor"]
        self.ids.musicName.text = musicInfo["musicName"]
        self.ids.genreName.text = musicInfo["genreName"]
        self.highScoreHistoryRv.data = self.score.getHighScoreHistoryByChartId(self.chartId)

    def on_leave(self, *args):
        self.manager.remove_widget(self)
        return super().on_leave(*args)

    def switchScreen(self):
        if self.allDisplayFlg:
            self.highScoreHistoryRv.data = self.score.getHighScoreHistoryByChartId(
                    self.chartId
                )

class highScoreHistory(BoxLayout):
    mode = StringProperty()
    highScore = StringProperty()
    maxCombo = StringProperty()
    updateTime = StringProperty()


if __name__ == '__main__':
    pass
