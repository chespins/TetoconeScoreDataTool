# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from variable.setappdata import AppCommonData

from model.highscoredetails import HighScoreFormusic as dataSet
from util import util

Builder.load_file(util.find_data_file('./kvfile/highScoreDetails.kv'))


class HighScoreDetailsScreen(Screen):
    chartId = StringProperty()

    def __init__(self, comonData: AppCommonData, **kwargs):
        super(HighScoreDetailsScreen, self).__init__(**kwargs)
        self.commonData = comonData

    def on_pre_enter(self, **kwargs):
        if self.chartId == "":
            self.chartId = self.commonData.getDisplayChartId()
            self.setMusicDate()
            modePulldownData = dataSet.makeModeNamePulldown(self.chartId)
            multiPlayFlg = len(modePulldownData) == 1
            self.ids.modeSpinnerId.values = modePulldownData
            self.ids.modeSpinnerId.text = modePulldownData[0]
            self.ids.modeSpinnerId.disabled = multiPlayFlg
            self.ids.changeModeBtn.disabled = multiPlayFlg
            self.setHighScoreData(modePulldownData[0])

    
    def resetScreen(self, **kwargs) :
        self.chartId = ""
        self.commonData.setDisplayChartId("")
        self.ids.historyButton.disabled = False

    def changeMode(self, **kwargs) :
        displayedMode = self.ids.modeSpinnerId.text
        self.setHighScoreData(displayedMode)

    def setMusicDate(self):
        musicInfo = dataSet.getMusicName(self.chartId)
        self.ids.levelName.text = musicInfo["levelName"]
        self.ids.levelName.color = musicInfo["levelColor"]
        self.ids.musicName.text = musicInfo["musicName"]
        self.ids.genreName.text = musicInfo["genreName"]

    def setHighScoreData(self, displayedMode):
        highScoreData = dataSet.getHighScoreByMusic(self.chartId, displayedMode)
        self.ids.highScore.text = highScoreData["highScore"]
        self.ids.maxCombo.text = highScoreData["maxCombo"]
        self.ids.playCount.text = highScoreData["playCount"]
        self.ids.clearedCount.text = highScoreData["clearedCount"]
        self.ids.fullComboCount.text = highScoreData["fullComboCount"]
        self.ids.perfectCount.text = highScoreData["perfectCount"]



class CharBlackLabel(Label):
    pass

if __name__ == '__main__':
    pass
