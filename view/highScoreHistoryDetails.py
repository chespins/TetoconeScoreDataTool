# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from variable.setappdata import AppCommonData
from model import highscoredetails as score
from util import util

Builder.load_file(util.find_data_file('.\\kvfile\\highScoreHistoryDetails.kv'))


class HighScoreHistoryDetailsScreen(Screen):
    highScoreHistoryRv = ObjectProperty()
    chartId = StringProperty()
    allDisplayFlg = True

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(HighScoreHistoryDetailsScreen, self).__init__(**kwargs)
        self.commonData = comonData

    def on_pre_enter(self, **kwargs):
        if self.chartId == "":
            self.chartId = self.commonData.getDisplayChartId()

        musicInfo = score.getMusicName(self.chartId)
        self.ids.levelName.text = musicInfo["levelName"]
        self.ids.musicName.text = musicInfo["musicName"]
        self.highScoreHistoryRv.data = score.getHighScoreByMusic(self.chartId)

    def resetScreen(self, **kwargs):
        self.highScoreHistoryRv.data = []
        self.chartId = ""

    def switchScreen(self):
        if (self.allDisplayFlg):
            self.highScoreHistoryRv.data = score.getHighScoreByMusic(
                    self.chartId
                )


class highScoreHistory(BoxLayout):
    mode = StringProperty()
    highScore = StringProperty()
    maxCombo = StringProperty()
    updateTime = StringProperty()


if __name__ == '__main__':
    pass
