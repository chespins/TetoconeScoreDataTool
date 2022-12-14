# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from model.highscoreSearch import HighScoreSearch as hsc
from variable.setappdata import AppCommonData
from util import util

Builder.load_file(util.findDataFile('./kvfile/highScoreSelected.kv'))


class HighScoreSelectScreen(Screen):
    musicRv = ObjectProperty()
    unplayedFlg = BooleanProperty(False)

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(HighScoreSelectScreen, self).__init__(**kwargs)
        self.ids.LevelSpinnerId.values = hsc.makeLavalNamePulldown()
        self.ids.LevelSpinnerId.text = ""
        self.ids.genreSpinnerId.values = hsc.makeGenreNamePulldown()
        self.ids.genreSpinnerId.text = ""
        self.commonData = comonData

    def resetData(self):
        self.musicRv.data = []
        self.ids.searchMusicName.text = ""
        self.ids.LevelSpinnerId.text = ""
        self.ids.genreSpinnerId.text = ""
        self.unplayedFlg = False

    def allMusic(self):
        searchLavelName = self.ids.LevelSpinnerId.text
        searchGenreName = self.ids.genreSpinnerId.text
        unplayedFlg = self.unplayedFlg
        self.musicRv.data = hsc.searchMusic("", searchLavelName, searchGenreName, unplayedFlg)
        self.ids.searchMusicName.text = ""

    def searchMusic(self):
        searchMusicName = self.ids.searchMusicName.text
        searchLavelName = self.ids.LevelSpinnerId.text
        searchGenreName = self.ids.genreSpinnerId.text
        unplayedFlg = self.unplayedFlg
        self.musicRv.data = hsc.searchMusic(searchMusicName, searchLavelName, searchGenreName, unplayedFlg)

    def setChartId(self, chartId):
        self.commonData.setDisplayChartId(chartId)
    
    def checkboxCheck(self, checkbox):
        self.unplayedFlg = checkbox.active


class SearchHighScore(BoxLayout):
    musicName = StringProperty()
    levelName = StringProperty()
    highScore = StringProperty()
    playCount = StringProperty()
    chartId = StringProperty()
    detailsFlg = BooleanProperty()


if __name__ == '__main__':
    pass
