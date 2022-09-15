# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from variable.setappdata import AppCommonData

from model import highscoredetails as dataSet
from util import util

Builder.load_file(util.find_data_file('./kvfile/highScoreDetails.kv'))


class HighScoreDetailsScreen(Screen):
    highScoreRv = ObjectProperty()
    chartId = StringProperty()

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(HighScoreDetailsScreen, self).__init__(**kwargs)
        self.commonData = comonData

    def on_pre_enter(self, **kwargs):
        if self.chartId == "":
            self.chartId = self.commonData.getDisplayChartId()

        musicInfo = dataSet.getMusicName(self.chartId)
        self.ids.levelName.text = musicInfo["levelName"]
        self.ids.musicName.text = musicInfo["musicName"]
        self.highScoreRv.data = dataSet.getHighScoreByMusic(self.chartId)

    def resetScreen(self, **kwargs):
        self.chartId = ""
        self.commonData.setDisplayChartId("")
        self.highScoreRv.data = []


class highScore(BoxLayout):
    mode = StringProperty()
    highScore = StringProperty()
    maxCombo = StringProperty()
    playCount = StringProperty()
    clearedCount = StringProperty()
    fullComboCount = StringProperty()
    perfectCount = StringProperty()
    updateTime = StringProperty()


if __name__ == '__main__':
    pass
