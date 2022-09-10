# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from model import highscoreSerch as hsc
from variable.setappdata import AppCommonData
from util import util

Builder.load_file(util.find_data_file('.\\kvfile\\highScoreSelected.kv'))


class HighScoreSelectScreen(Screen):
    musicRv = ObjectProperty()

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(HighScoreSelectScreen, self).__init__(**kwargs)
        self.ids.LevelSpinnerId.values = hsc.makeLavalNamePulldown()
        self.ids.LevelSpinnerId.text = ""
        self.commonData = comonData

    def resetData(self):
        self.musicRv.data = []
        self.ids.searchMusicName.text = ""
        self.ids.LevelSpinnerId.text = ""

    def allMusic(self):
        serchLavelName = self.ids.LevelSpinnerId.text
        self.musicRv.data = hsc.serchMusic("", serchLavelName)
        self.ids.searchMusicName.text = ""

    def serchMusic(self):
        serchMusicName = self.ids.searchMusicName.text
        serchLavelName = self.ids.LevelSpinnerId.text
        self.musicRv.data = hsc.serchMusic(serchMusicName, serchLavelName)

    def setChartId(self, chartId):
        self.commonData.setDisplayChartId(chartId)


class SerchHighScore(BoxLayout):
    musicName = StringProperty()
    levelName = StringProperty()
    highScore = StringProperty()
    chartId = StringProperty()


if __name__ == '__main__':
    pass
